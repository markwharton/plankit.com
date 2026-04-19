#!/usr/bin/env python3
"""Static checks for the site.

Verifies:
  1. site/style.css exists, every page links it, no inline <style> blocks remain.
  2. Every class used in HTML is defined in style.css.
  3. Internal href/src links resolve to a real file under site/.
     External links (http://, https://, mailto:) are skipped.
  4. Doc subpages under site/pk/ all carry the same set of footer links
     (peer-page navigation drift detector).

Run from the repo root:
  python3 scripts/check.py
"""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parent.parent
SITE = REPO_ROOT / "site"
STYLE_CSS = SITE / "style.css"
PAGES = sorted(SITE.rglob("*.html"))

LINK_TAG_RE = re.compile(
    r'<link\s+rel="stylesheet"\s+href="/style\.css"\s*/?>',
    re.IGNORECASE,
)
STYLE_BLOCK_RE = re.compile(r"<style\b[^>]*>", re.IGNORECASE)
CLASS_ATTR_RE = re.compile(r'class="([^"]+)"')
CSS_CLASS_RE = re.compile(r"\.([a-zA-Z][\w-]*)")
FOOTER_BLOCK_RE = re.compile(
    r'<div\s+class="footer">(.*?)</div>', re.DOTALL | re.IGNORECASE
)
HREF_RE = re.compile(r'href="([^"]+)"')

LINK_ATTRS = {
    "a": "href",
    "link": "href",
    "img": "src",
    "script": "src",
    "source": "src",
}


class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_name = LINK_ATTRS.get(tag.lower())
        if not attr_name:
            return
        for name, value in attrs:
            if name == attr_name and value:
                self.links.append(value)


def collect_css_classes(css: str) -> set[str]:
    return set(CSS_CLASS_RE.findall(css))


def collect_used_classes(html: str) -> set[str]:
    used: set[str] = set()
    for chunk in CLASS_ATTR_RE.findall(html):
        used.update(chunk.split())
    return used


def collect_links(html: str) -> list[str]:
    parser = LinkCollector()
    parser.feed(html)
    return parser.links


def extract_footer_links(html: str) -> frozenset[str] | None:
    match = FOOTER_BLOCK_RE.search(html)
    if not match:
        return None
    return frozenset(HREF_RE.findall(match.group(1)))


def doc_subpages() -> list[Path]:
    """Pages under site/pk/ that aren't /pk/index.html itself."""
    pk_index = SITE / "pk" / "index.html"
    return sorted(
        p for p in (SITE / "pk").rglob("index.html") if p != pk_index
    )


def check_doc_footer_drift() -> list[str]:
    pages = doc_subpages()
    if len(pages) < 2:
        return []

    footers: dict[Path, frozenset[str] | None] = {
        p: extract_footer_links(p.read_text()) for p in pages
    }

    errors: list[str] = []
    for p, links in footers.items():
        if links is None:
            errors.append(
                f"{p.relative_to(REPO_ROOT)}: no <div class=\"footer\"> block found"
            )
    if errors:
        return errors

    canonical: set[str] = set()
    for links in footers.values():
        assert links is not None
        canonical |= links

    for p, links in footers.items():
        assert links is not None
        missing = canonical - links
        if missing:
            errors.append(
                f"{p.relative_to(REPO_ROOT)}: footer missing peer links: "
                f"{', '.join(sorted(missing))}"
            )
    return errors


def resolve_internal(link: str, page: Path) -> Path | None:
    """Resolve an internal href/src to a path under site/, or None if external/skip.

    Returns the target file path if resolvable, raises ValueError if it doesn't
    exist on disk. Returns None for links that should be skipped (external,
    fragment-only, mailto, etc).
    """
    parsed = urlparse(link)
    if parsed.scheme in ("http", "https", "mailto", "tel"):
        return None
    if not parsed.path and parsed.fragment:
        return None  # same-page anchor — fragment validation is a future check

    raw_path = parsed.path
    if raw_path.startswith("/"):
        target = SITE / raw_path.lstrip("/")
    else:
        target = (page.parent / raw_path).resolve()

    if target.is_dir() or raw_path.endswith("/"):
        candidate = target / "index.html"
        if candidate.exists():
            return candidate
        raise ValueError(f"directory has no index.html: {target}")

    if target.exists():
        return target

    # Try .html extension as a fallback (clean URLs without trailing slash).
    html_candidate = target.with_suffix(target.suffix + ".html") if target.suffix else target.parent / (target.name + ".html")
    if html_candidate.exists():
        return html_candidate

    raise ValueError(f"path does not exist: {target}")


def check() -> list[str]:
    errors: list[str] = []

    if not STYLE_CSS.exists():
        return [f"missing: {STYLE_CSS.relative_to(REPO_ROOT)}"]

    if not PAGES:
        return [f"no HTML pages found under {SITE.relative_to(REPO_ROOT)}/"]

    css_classes = collect_css_classes(STYLE_CSS.read_text())

    for page in PAGES:
        rel = page.relative_to(REPO_ROOT)
        html = page.read_text()

        if STYLE_BLOCK_RE.search(html):
            errors.append(f"{rel}: contains an inline <style> block")

        if not LINK_TAG_RE.search(html):
            errors.append(f'{rel}: missing <link rel="stylesheet" href="/style.css">')

        missing_classes = sorted(collect_used_classes(html) - css_classes)
        if missing_classes:
            errors.append(
                f"{rel}: classes used but not defined in style.css: "
                f"{', '.join(missing_classes)}"
            )

        for link in collect_links(html):
            try:
                resolve_internal(link, page)
            except ValueError as e:
                errors.append(f"{rel}: broken link {link!r} ({e})")

    errors.extend(check_doc_footer_drift())
    return errors


def main() -> int:
    errors = check()
    if errors:
        print("FAIL")
        for err in errors:
            print(f"  - {err}")
        return 1
    print(
        f"OK — {len(PAGES)} pages, /style.css linked everywhere, "
        f"no inline <style>, all classes defined, internal links resolve, "
        f"doc-page footers consistent"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
