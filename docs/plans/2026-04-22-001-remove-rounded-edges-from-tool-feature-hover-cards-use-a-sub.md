# Remove rounded edges from tool/feature hover cards; use a subtle top-to-bottom gradient

## Context

Commit `b4e171d feat(site): hover tint and whole-card click on tool/feature cards` introduced a hover affordance on `.tools` and `.features` list rows: a solid warm tint (`--hover-bg: #f3ede4`) with a 6px `border-radius` and a full-row `::after` click overlay. The tint reads as a bit "button-like" — too pronounced for this otherwise flat, typographic site.

The user wants:
1. **Drop the rounded corners.** Let the row extend as a full-width band consistent with the hard-edged page aesthetic.
2. **Replace the solid tint with a top-to-bottom gradient** that fades the tint out toward the bottom of the row, so the hover state reads as a soft "rise" rather than a filled block.

Outcome: the hover cue is still clearly present, but quieter.

## Changes

Single file: `site/style.css`.

### 1. Remove `border-radius`

Delete line 204:

```css
border-radius: 6px;
```

### 2. Swap solid background for a vertical gradient

Replace line 211:

```css
background: var(--hover-bg);
```

with:

```css
background: linear-gradient(to bottom, var(--hover-bg), transparent);
```

- Reuses the existing `--hover-bg` token (no new tokens needed).
- The gradient goes from tinted at the top → transparent at the bottom, so the bottom of the card fades into the page `--bg` color.
- Naturally subtler than a flat fill because half the row is effectively untinted.

### 3. Add a matching zero-alpha base gradient so the transition animates

The existing `transition: background var(--transition)` on the base rule (line 199) does not animate cleanly between "no background" and a gradient — browsers interpolate gradients only when both sides are gradients of the same shape. Add a transparent-to-transparent base gradient so the hover fade-in/out is smooth:

In the `.tools > li:has(a), .features > li:has(a)` block (lines 196–205), after removing `border-radius`, add:

```css
background: linear-gradient(to bottom, transparent, transparent);
```

### 4. Update the explanatory comment

Rewrite lines 193–195 (drop the corner-radius rationale, describe the gradient):

```css
/* Linkable tool/feature cards: whole row tints on hover and the link covers the full row.
   A small negative margin + matching padding eases the tint off the hard content edges.
   The tint is a top-to-bottom gradient that fades into the page background, keeping the
   affordance subtle on this otherwise flat layout. */
```

## Files

- `site/style.css` (lines 193–212)

## Blast radius

Every page using `.tools` or `.features`. No HTML changes required.

- `site/index.html` — `.tools`
- `site/pk/index.html` — `.features`
- `site/pk/start/index.html` — `.features`
- `site/signals/index.html` — `.features`
- `site/mcp-bridge/index.html` — `.features`

## Verification

**Automated:**
```
python3 scripts/check.py
```
Expected: passes (no selectors added/removed, no new classes referenced).

**Smoke — open each page locally and hover the cards:**
```
python3 -m http.server -d site 8000
```
Then in a browser:
- `http://localhost:8000/` — hover each `.tools` row.
- `http://localhost:8000/pk/` — hover each `.features` row.
- `http://localhost:8000/pk/start/`, `/signals/`, `/mcp-bridge/` — hover `.features` rows.

Confirm for each:
- No rounded corners on hover.
- Tint is strongest at the top of the row and fades toward the bottom.
- Fade in/out is smooth (0.2s), not a pop.
- Whole row remains clickable (the `::after` overlay still covers the card).
- Underline on the title is still suppressed on hover (tint is the affordance).

Negative case: hover a `.commands` or `.steps` row on any page and confirm no tint appears there (the rule is scoped to `.tools` and `.features` only).
