# Draft a "model shifts" note on /pk

## Context

Claude model releases occasionally reshape the primitives pk sits on — slash command dispatch, plan mode exit, auto mode permissioning, long-turn context retention. Tooling that assumed the previous behavior can silently regress. Opus 4.7 is the immediate example (long-session retention, cross-session memory, more autonomous auto mode, xhigh default), and a recent `pk preserve` race — caused when `/preserve` typed after `ExitPlanMode` sat queued behind autonomous work long enough for a parallel session's plan file to intercept mtime-based selection — is the concrete incident.

The fix for that race already landed. What's missing is expectation-setting on /pk so readers understand the shape of the situation rather than encountering it as a surprise: plankit rides on Claude Code's evolving semantics, the deterministic layer is the CLI (not the model's intra-turn behavior), and shifts that expose edges get answered by hardening the CLI layer further. This is a semi-disclaimer, dev-to-dev, no apologies, no version-naming.

## Scope

A single 2–3 paragraph section added to `site/pk/index.html`. No other files change. No notes entry, no new page, no prose elsewhere.

## Placement

Insert between the existing **Setup modes** section (ends at line 85) and **Docs** section (starts at line 87). That spot closes out the substantive content — install, features, commands, setup, expectations — before Docs pivots to navigation and the post-`<hr>` aside closes the page.

Alternatives considered:
- After "What it does" and before "Commands" — too early; disrupts the usage-information flow before readers have seen what pk actually does.
- After `<hr>` alongside the aside — the aside is a one-line italic post-script; a three-paragraph h2 section would overpower it and break the closing rhythm.

## Heading

**When the model shifts** — 4 words, active, developer-friendly, signals the topic without apologizing or promising. Matches the existing h2 voice on the page (short, declarative).

Alternate if the user prefers more neutral framing: **Model shifts and guarantees**.

## Draft prose

To insert as a new `<div class="section">` block between the `Setup modes` section (line 85) and the `Docs` section (line 87):

```html
  <div class="section">
    <h2>When the model shifts</h2>
    <p>pk runs on top of Claude Code&rsquo;s hooks, skills, slash commands, and plan mode. Those primitives evolve with each Claude release &mdash; how slash commands dispatch, how plan mode exits, how long-session context is retained, how auto mode proceeds without prompting. Tooling built around one version&rsquo;s assumptions can behave differently under the next.</p>
    <p>pk&rsquo;s guarantees live in the CLI layer, not in the model. Git mutation guards, managed-file protection, bounded hook timeouts, single-file plan staging &mdash; pure Go, no network, no model state. What Claude does inside a single turn &mdash; how it schedules work, what it holds in context &mdash; isn&rsquo;t something pk can guarantee, and doesn&rsquo;t try to.</p>
    <p>When a release exposes an edge case, the fix belongs in the CLI layer: reduce the model-dependence that let the bug in, so the next shift can&rsquo;t re-expose the same class of problem. That&rsquo;s the lifecycle, not an aberration from it. If you hit a surprise, <a href="https://github.com/markwharton/plankit/issues">open an issue</a> &mdash; don&rsquo;t paper over it.</p>
  </div>
```

Style notes:
- Uses `<div class="section">` + `<h2>` + plain `<p>` — the existing reusable pattern on the page.
- Em-dashes rendered as `&mdash;` and curly apostrophes as `&rsquo;` to match the surrounding markup.
- No `.aside` / `.features` / `.commands` list class — plain prose is the right shape for this content.
- Links: one outbound to the issues tracker (the "open an issue" nudge). No version numbers, no named bugs, no apology phrases ("we did our best", "despite our efforts"), and no paraphrase of Anthropic release copy.

## Critical files

- `site/pk/index.html` — insert the new section between line 85 (`</div>` closing Setup modes) and line 87 (`<div class="section">` opening Docs).

Nothing else changes. Footer chain is unchanged (this page is cross-register; the existing `plankit · pk · mcp-bridge · signals · privacy · github` line on line 116 stays). `scripts/check.py` runs undefined-class and internal-link checks; the only class used is `.section` (already defined) and the only new link is external (GitHub issues), so neither check is affected.

## Verification

1. Static checks — from repo root:
   ```
   python3 scripts/check.py
   ```
   Expect: exit 0. This confirms the stylesheet link, no inline `<style>`, no undefined classes, no broken internal links, and footer consistency on /pk.
2. Smoke — open `site/pk/index.html` locally in a browser (e.g. `open site/pk/index.html` on macOS, or serve with `python3 -m http.server` from `site/`) and confirm:
   - The new section renders between **Setup modes** and **Docs**.
   - H2 styling matches neighbouring section headings (uppercase, accent color, letter-spaced Inter).
   - Paragraph spacing is consistent with the rest of the page (20px between `<p>`, 56px between sections).
   - The GitHub issues link is accent-colored and underlines on hover.
   - Em-dashes and curly apostrophes render as glyphs, not entities.
3. Self-check on tone — reread the three paragraphs and ask: *does the reader leave thinking plankit is fragile?* If yes, revise before committing. The finished text should land as: there's a determinism boundary, it's honest, and the lifecycle is working as designed.

No test suite to run (static site). No deploy verification needed at plan stage — GitHub Pages builds from `main` on merge; this change lands on `develop` first.
