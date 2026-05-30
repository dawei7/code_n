"""Double-click launcher for cOde(n).

Source mode:
    python play.py

Packaged mode:
    cOde(n).exe
"""

from __future__ import annotations

import os
import sys

APP_ROOT = os.path.dirname(os.path.abspath(sys.executable if getattr(sys, "frozen", False) else __file__))
if APP_ROOT not in sys.path:
    sys.path.insert(0, APP_ROOT)


def _configure_stdio():
    """Avoid PyInstaller error dialogs when Windows streams cannot encode UI text."""
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure:
            try:
                reconfigure(errors="replace")
            except (OSError, ValueError):
                pass


def _bundle_dynamic_imports():
    """Keep PyInstaller aware of modules loaded by player solution scripts."""
    import code_n.api  # noqa: F401
    import code_n.counter  # noqa: F401
    import code_n.execution_trace  # noqa: F401
    import code_n.grid  # noqa: F401
    import code_n.pygame_renderer  # noqa: F401
    import code_n.tracked  # noqa: F401


def main() -> int:
    _configure_stdio()
    _bundle_dynamic_imports()

    if len(sys.argv) > 1 and sys.argv[1] == "--run-challenge":
        from run_challenge import main as run_challenge_main

        sys.argv = ["run_challenge.py", *sys.argv[2:]]
        run_challenge_main()
        return 0

    from code_n.navigation import launch_navigation

    launch_navigation()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
