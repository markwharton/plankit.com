#!/usr/bin/env python3
"""Serve the static site locally for preview.

Usage:
  python3 scripts/serve.py [PORT]

Defaults to port 8000. Serves from the repo's site/ directory.
Press Ctrl+C to stop.
"""

from __future__ import annotations

import functools
import http.server
import socketserver
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SITE = REPO_ROOT / "site"
DEFAULT_PORT = 8000


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def copyfile(self, source, outputfile):
        try:
            super().copyfile(source, outputfile)
        except (BrokenPipeError, ConnectionResetError):
            pass


def main() -> int:
    port = DEFAULT_PORT
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"error: PORT must be an integer, got {sys.argv[1]!r}")
            return 2

    if not SITE.is_dir():
        print(f"error: site directory not found at {SITE}")
        return 1

    handler = functools.partial(QuietHandler, directory=str(SITE))

    with socketserver.TCPServer(("", port), handler) as httpd:
        base = f"http://localhost:{port}"
        print(f"Serving {SITE.relative_to(REPO_ROOT)}/ on {base}")
        print(f"  {base}/")
        print(f"  {base}/pk/")
        print(f"  {base}/pk/start/")
        print(f"  {base}/pk/guide/")
        print("Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print()
            return 0


if __name__ == "__main__":
    sys.exit(main())
