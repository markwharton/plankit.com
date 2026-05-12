# Rename /init to /conventions on pk landing page

## Context
The `/init` skill was renamed to `/conventions` in plankit to avoid a name collision with Claude Code's built-in `/init` skill. The site's pk landing page still references the old name.

## Change
**File:** `site/pk/index.html` (line 51)

Replace:
```html
<span><code>/init</code>, <code>/preserve</code>, <code>/ship</code> &mdash; slash commands for common workflows.</span>
```
With:
```html
<span><code>/conventions</code>, <code>/preserve</code>, <code>/ship</code> &mdash; slash commands for common workflows.</span>
```

Release notes in `site/pk/notes/index.html` are historical and stay as-is.

## Verification
1. Run `python3 scripts/check.py` — should pass.
2. Open `site/pk/index.html` in a browser and confirm the slash-command list reads `/conventions, /preserve, /ship`.
