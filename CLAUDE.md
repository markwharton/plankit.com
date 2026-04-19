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
- **Page tree:** `site/index.html` (landing), `site/pk/` (product) with `start/`, `guide/`, `notes/`, `site/mcp-bridge/` with `notes/`, `site/signals/`. Update `site/sitemap.xml` when adding a page.

### Design system

- **Typography:** Source Serif 4 (body) + Inter (UI/labels), loaded from Google Fonts.
- **Color tokens:** `--bg #faf8f5`, `--text #2c2825`, `--muted #7a726a`, `--accent #b8510d`, `--rule #e0dbd5`, `--code-bg #f0ece7`.
- **Layout:** `--max-width: 720px`, single-column. Top mark → h1 → italic subtitle. Footer line: `plankit · pk · mcp-bridge · signals · github`.
- **List patterns:** `.tools` for the landing-page tool grid (16px Inter title, 20px row padding); `.features` for in-page title-and-description lists (15px Inter title, 16px padding); `.commands` for mono command + description rows; `.steps` for numbered counter lists. All use `<strong>` for the title and `<span>` for the description.

### Page conventions

- Every page sets `<title>`, `meta name="description"`, `og:title`/`og:description`/`og:url`/`og:type`, and `<link rel="canonical">`.
- Internal links use absolute paths (`/pk/`, `/`), not relative.
- Favicon uses `/favicon.svg`. Alternates exist (`favicon-green.svg`, `favicon-leather.svg`, `favicon-rust.svg`, `favicon-terminal.svg`) — keep them, don't delete.

### Voice and naming

The goal is grammatically correct and easy to read. Page names appear in different registers — labels (cards, footers, `<title>`), h1, subtitle, inline prose — and they don't all need to match.

- **Within a register, prefer matching.** A Docs card linking to /pk/start/ should say "Get started" if the page's h1 says "Get started" — same role, same wording. Drift between labels for the same page is the kind of inconsistency worth fixing.
- **Between registers, prefer good English over forced consistency.** "Methodology" works as a card label; "the methodology guide" reads better in a sentence. Both are right because they serve different jobs.

### Branches and releases

- **All work goes through `develop`** — never commit directly to `main`. Releases merge to `main`, which triggers the Pages deploy.
- `.pk.json` configures `pk guard` to block writes on `main` and `pk release` to push to `main`.

### CI and dependencies

- **GitHub Actions are pinned to commit SHAs** (e.g. `actions/checkout@de0fac…`). Never replace a SHA with a mutable tag — Dependabot bumps the SHA when a new release lands.
- **Dependabot watches GitHub Actions weekly** and opens PRs against `develop` (`.github/dependabot.yml`).

### Verification

- **Static checks in CI** — `scripts/check.py` runs via `.github/workflows/check.yml` on every push and PR. Catches stylesheet wiring drift, footer drift in both registers (cross-tool and tool-scoped), broken internal links, and undefined CSS classes.
- **No automated functional tests.** Smoke check: open the changed page in a browser, confirm links resolve, meta tags render, and sitemap entries match the page tree.
- The Pages workflow filters on `site/**`, so changes outside `site/` do not deploy and need no smoke check.
