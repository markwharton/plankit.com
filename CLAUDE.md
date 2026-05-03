# CLAUDE.md

IMPORTANT: Follow these rules at all times.

## Critical Rules

- NEVER take shortcuts without asking — STOP, ASK, WAIT for approval.
- NEVER force push — make a new commit to fix mistakes.
- NEVER commit secrets to version control.
- Only do what was asked — no scope creep.
- Understand existing code before changing it.
- If you don't know, say so — never guess.
- Test before and after every change.
- Surface errors clearly — no silent fallbacks.

## Project Conventions

### Stack and structure

- **Static HTML/CSS site** — no build system, no framework, no JavaScript. All deployed content lives in `site/`.
- **GitHub Pages deploys from `main`** via `.github/workflows/pages.yml`, filtered on `site/**` path changes. Custom domain in `site/CNAME` (plankit.com).
- **One shared stylesheet** at `site/style.css`, linked by every page. Design tokens live in `:root`. No inline `<style>` blocks — `scripts/check.py` enforces this.
- **Page tree:** `site/index.html` (landing); tool landings at `site/pk/`, `site/mcp-bridge/`, `site/signals/`, each with an optional `notes/` sub-page for release notes; plus `site/references/`, `site/privacy/`, and `site/404.html`. Update `site/sitemap.xml` when adding a page.

### Design system

- **Typography:** Source Serif 4 (body) + Inter (UI/labels) + SF Mono (code), referenced via `--font-body`, `--font-ui`, `--font-mono` tokens. Web fonts load from Bunny Fonts (privacy-respecting drop-in for Google Fonts) — preconnect + stylesheet `<link>` go in each page's `<head>` before `/style.css`.
- **Tokens:** colors (`--bg`, `--text`, `--muted`, `--accent`, `--rule`, `--code-bg`); type scale (`--text-xs`…`--text-3xl`, plus `--text-body` 18px); spacing scale (`--space-1` 4px through `--space-11` 120px); plus `--max-width` 720px and `--transition` 0.2s. Reach for tokens before literals.
- **Layout:** `--max-width: 720px`, single-column. Top mark → h1 → italic subtitle. Footer line (unified across all pages): `home · pk · mcp-bridge · signals · references · privacy`.
- **List patterns:** `.tools` for the landing-page tool grid (`--text-base` Inter title, `--space-4` row padding); `.features` for in-page title-and-description lists (`--text-md` Inter title, `--space-3` padding); `.commands` for mono command + description rows; `.steps` for numbered counter lists. The list scaffold (no bullets, top/bottom row borders) is shared via comma-separated selectors. `.features` and `.tools` use `<strong>` for the title and `<span>` for the description; descriptions match `> li > span` only, so don't nest other spans inside list rows.
- **Link affordance:** the global `a` rule provides accent color, transparent border-bottom, and a `:hover` / `:focus-visible` underline. Don't redeclare it on per-region rules — only override what differs (e.g. `.mark a` overrides color to muted).

### Page conventions

- Every page sets `<title>`, `meta name="description"`, `og:title`/`og:description`/`og:url`/`og:type`, and `<link rel="canonical">`.
- Internal links use absolute paths (`/pk/`, `/`), not relative.
- Favicon uses `/favicon.svg`. Alternates exist (`favicon-green.svg`, `favicon-leather.svg`, `favicon-rust.svg`, `favicon-terminal.svg`) — keep them, don't delete.

### Brochure pattern

The site is a brochure, not a reading experience. Deep docs live in the per-tool GitHub repos; site pages are tool pitches and release notes that link out.

- **Tool landings** (/pk/, /mcp-bridge/, /signals/) follow a consistent shape: intro → Install → (optional tool-specific section, e.g. signals' Two modes) → What it does → closing paragraph.
- **Install blocks are boilerplate.** Install command + releases-page fallback, nothing else. No size, runtime-dep, or post-install-command prose — those belong in the intro or the repo README. signals substitutes an in-development status message in the same slot until a real release exists.
- **Closing paragraph on tool landings** contains: a GitHub link (wording varies per tool — `Full docs, install, and source on GitHub` for pk, `Source and releases on GitHub` for mcp-bridge, `Source on GitHub` for signals), `— MIT licensed`, and (where a notes page exists) a `What's new in <tool>` link to /notes/.
- **MIT appears once per page**, in the closing paragraph next to the Source link. Don't repeat it in the intro.
- **Release notes pages** (/<tool>/notes/) use `<h1>Release notes</h1>` + subtitle `What's new in <tool>, and how to use it.` Each version is an `<h2>` block with version + date + short tag line. Close with one line linking to the CHANGELOG on GitHub. `<meta name="description">` and `og:description` match the subtitle.
- **og:title on tool landings** uses a pitch — `<name> — <h1 pitch>` (e.g. `pk — plan-driven development toolkit`). Other pages (privacy, release notes, 404) use `<name> — plankit`.

### Voice and naming

The goal is grammatically correct and easy to read. Page names appear in different registers — labels (cards, footers, `<title>`), h1, subtitle, inline prose — and they don't all need to match.

- **Within a register, prefer matching.** A card linking to /pk/notes/ should say "Release notes" if the page's h1 says "Release notes" — same role, same wording. Drift between labels for the same page is the kind of inconsistency worth fixing.
- **Between registers, prefer good English over forced consistency.** "Methodology" works as a card label; "the methodology guide" reads better in a sentence. Both are right because they serve different jobs.
- **GitHub docs are the register model.** Favor concrete specifics over aphorism. Avoid pull-quotes and abstracted claims. The site refactored away from a denser, marketing-leaning voice because it drifted from the GitHub originals' credibility.

### Branches and releases

- **All work goes through `develop`** — never commit directly to `main`. Releases merge to `main`, which triggers the Pages deploy.
- `.pk.json` configures `pk guard` to block writes on `main` and `pk release` to push to `main`.

### CI and dependencies

- **GitHub Actions are pinned to commit SHAs** (e.g. `actions/checkout@de0fac…`). Never replace a SHA with a mutable tag — Dependabot bumps the SHA when a new release lands.
- **Dependabot watches GitHub Actions weekly** and opens PRs against `develop` (`.github/dependabot.yml`).

### Verification

- **Static checks in CI** — `scripts/check.py` runs via `.github/workflows/check.yml` on every push and PR. Catches stylesheet wiring drift, footer drift against the single shared chain, broken internal links, and undefined CSS classes.
- **No automated functional tests.** Smoke check: open the changed page in a browser, confirm links resolve, meta tags render, and sitemap entries match the page tree.
- The Pages workflow filters on `site/**`, so changes outside `site/` do not deploy and need no smoke check.
