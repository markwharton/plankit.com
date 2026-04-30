# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [v0.3.1] - 2026-04-30

### Documentation

- add v0.15.1 release notes for pk (ec9e470)

### Maintenance

- update pk-managed files for v0.15.1 (a44fa1f)

## [v0.3.0] - 2026-04-29

### Added

- mark external links with NE arrow icon (8412988)

## [v0.2.9] - 2026-04-28

### Documentation

- add Knuth's Claude's Cycles paper to references (eba38f5)
- add vibe-coding journal entry to pk design.txt (143ff61)
- add Aquino-Michaels' Completing Claude's Cycles paper to references (be1fcf3)
- add formalism journal entry to pk design.txt (8d36afb)
- add v0.15.0 release notes for pk (51e7a25)

## [v0.2.8] - 2026-04-25

### Documentation

- add landing intro; rename workshop section to 'More tools' (f83147e)
- add v0.14.2–v0.14.3 sandbox note to pk v0.14.1 release entry (bd2da28)

### Maintenance

- update pk-managed files for v0.14.2 (bc40ea4)
- update pk-managed files for v0.14.3 (e60196d)

## [v0.2.7] - 2026-04-24

### Documentation

- add v0.14.0 release notes for pk (883e25a)
- add v0.14.1 release notes for pk (5e7b179)

### Maintenance

- update managed files for v0.14.1 (d7c62dd)

## [v0.2.6] - 2026-04-23

### Changed

- split landing page into core tool and workshop sections (fae0abc)

### Documentation

- disclose Bunny Fonts CDN on privacy page (d4e1ea8)

### Maintenance

- update managed files for v0.14.0 (1e625af)

## [v0.2.5] - 2026-04-23

### Changed

- unify footer across all pages (e1df962)
- align install section across tool pages (b163b69)

### Documentation

- update CLAUDE.md for brochure-era conventions (a5e61e1)

## [v0.2.4] - 2026-04-23

### Changed

- trim to brochure, link docs to GitHub (21e2f95)

## [v0.2.3] - 2026-04-22

### Changed

- promote pk docs to landing, simplify labels (0c041db)

### Maintenance

- regenerate pk-managed files for v0.13.1 (0d14859)

## [v0.2.2] - 2026-04-22

### Documentation

- add "When the model shifts" section to /pk (334d0c5)
- add v0.13.1 notes entry (178c8ec)

## [v0.2.1] - 2026-04-22

### Maintenance

- soften tool/feature hover with top-to-bottom gradient (23a1aa6)

## [v0.2.0] - 2026-04-21

### Added

- hover tint and whole-card click on tool/feature cards (b4e171d)

### Documentation

- list /ship skill alongside /changelog and /release (063d912)
- add pk v0.13.0 release notes (4944cd5)

### Maintenance

- regenerate pk-managed files for v0.13.0 (7970811)

## [v0.1.3] - 2026-04-21

### Documentation

- add pk v0.12.0 release notes (fcfd200)

## [v0.1.2] - 2026-04-20

### Fixed

- drop data-endpoint from beacon; rely on script-origin fallback (729c99d)

## [v0.1.1] - 2026-04-20

### Fixed

- drop defer from beacon, mark /404.html with data-kind="404" (edd249a)

## [v0.1.0] - 2026-04-19

### Added

- embed signals beacon and add privacy page (38fc79b)

## [v0.0.3] - 2026-04-19

### Fixed

- give landing-page tool cards a clear link affordance (99f8eb0)

### Changed

- tokenize style.css and swap fonts to Bunny (0db6182)

## [v0.0.2] - 2026-04-19

### Changed

- extract inline styles to shared site/style.css (66c88bb)

### Documentation

- add notes from the workshop page at /pk/notes/ (5fd815f)
- link /pk/notes/ from pk Docs section and doc-page footers (2fb86ee)
- align pk Docs card label with page h1 (bc2908b)
- add voice and naming convention to CLAUDE.md (9332f0e)
- add mcp-bridge and signals tool landing pages (c4c4db3)
- expand landing page for the workshop; cross-tool footer on top-level pages (3278659)
- add mcp-bridge notes page with v0.1.0 first release (6569c7e)
- link notes from mcp-bridge landing via Docs section (81f3d28)

### Maintenance

- add serve and check scripts for local site work (cd383e9)
- add favicon.ico and apple-touch-icon to silence browser probes (adfd920)
- add doc-page footer drift detector to check.py (40cd611)
- run scripts/check.py on push and pull_request (0bf37b3)
- add 404.html for not-found pages; serve.py supports it locally (64936aa)
- extend check.py drift detector for two-register footer policy (f797f39)
- drop example URL list from serve.py startup banner (d114e59)
- regenerate pk-managed files (877d5fb)

## [v0.0.1] - 2026-04-19

### Documentation

- add project conventions to CLAUDE.md and pk guard/release config (c6e7a5c)
- document pk setup --baseline on start page (1751fd2)

### Maintenance

- add Pages deploy workflow and Dependabot for github-actions (a9ba11c)
- add .gitignore with editor/OS and scratch patterns (1c5c170)
- sync .claude/ rules and skills via pk setup (0e2ab2f)

[v0.0.1]: https://github.com/markwharton/plankit.com/compare/v0.0.0...v0.0.1
[v0.0.2]: https://github.com/markwharton/plankit.com/compare/v0.0.1...v0.0.2
[v0.0.3]: https://github.com/markwharton/plankit.com/compare/v0.0.2...v0.0.3
[v0.1.0]: https://github.com/markwharton/plankit.com/compare/v0.0.3...v0.1.0
[v0.1.1]: https://github.com/markwharton/plankit.com/compare/v0.1.0...v0.1.1
[v0.1.2]: https://github.com/markwharton/plankit.com/compare/v0.1.1...v0.1.2
[v0.1.3]: https://github.com/markwharton/plankit.com/compare/v0.1.2...v0.1.3
[v0.2.0]: https://github.com/markwharton/plankit.com/compare/v0.1.3...v0.2.0
[v0.2.1]: https://github.com/markwharton/plankit.com/compare/v0.2.0...v0.2.1
[v0.2.2]: https://github.com/markwharton/plankit.com/compare/v0.2.1...v0.2.2
[v0.2.3]: https://github.com/markwharton/plankit.com/compare/v0.2.2...v0.2.3
[v0.2.4]: https://github.com/markwharton/plankit.com/compare/v0.2.3...v0.2.4
[v0.2.5]: https://github.com/markwharton/plankit.com/compare/v0.2.4...v0.2.5
[v0.2.6]: https://github.com/markwharton/plankit.com/compare/v0.2.5...v0.2.6
[v0.2.7]: https://github.com/markwharton/plankit.com/compare/v0.2.6...v0.2.7
[v0.2.8]: https://github.com/markwharton/plankit.com/compare/v0.2.7...v0.2.8
[v0.2.9]: https://github.com/markwharton/plankit.com/compare/v0.2.8...v0.2.9
[v0.3.0]: https://github.com/markwharton/plankit.com/compare/v0.2.9...v0.3.0
[v0.3.1]: https://github.com/markwharton/plankit.com/compare/v0.3.0...v0.3.1
