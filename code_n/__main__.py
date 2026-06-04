"""Entry point for `python -m code_n`.

This is a thin wrapper that delegates to the same handlers as `main.py`
so the package can be invoked as a module from the command line, from
test runners, or from a packaged build.

Usage:
    python -m code_n                       # show menu
    python -m code_n nav                   # open Pygame navigator
    python -m code_n info <id>             # show challenge details
    python -m code_n name <name>           # set student name
    python -m code_n reset                 # reset progress
"""
from __future__ import annotations

import sys


def main() -> int:
    # Reuse main.py's CLI dispatch by calling its main() with our argv.
    # main.py prepends the project root to sys.path before importing
    # registry/progress/etc, so the import order is preserved.
    import main as _main

    # main.main() calls sys.exit indirectly; we mirror its return.
    try:
        _main.main()
        return 0
    except SystemExit as exit_exc:
        return int(exit_exc.code or 0)


if __name__ == "__main__":
    raise SystemExit(main())
