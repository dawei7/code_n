"""Entry point for the PyInstaller-bundled cOde(n) server.

This module is the script PyInstaller bundles into ``coden-server.exe``.
It runs the FastAPI app on a random free port, then prints the
``Uvicorn running on http://127.0.0.1:PORT`` line on stdout — same as
``python -m uvicorn ...`` would. The Electron launcher (in dev) and
the packaged desktop app (in production) both parse that line out of
stdout to discover the chosen port, then poll ``/api/health``.

The host is hard-coded to ``127.0.0.1`` (loopback only) — the server
is a local helper, never a network service.

Exit code: 0 on clean shutdown, non-zero if uvicorn fails to start.
"""
from __future__ import annotations

import os
import sys

import uvicorn


def main() -> int:
    # The bundled server is invoked by the Electron desktop app.
    # In dev (`python -m uvicorn server.app.main:app`) the module
    # path is importable as `server.app.main`; in the bundle the
    # import works the same because PyInstaller preserves sys.path.
    host = os.environ.get("CODEN_HOST", "127.0.0.1")
    # Port 0 = "pick a free port"; the Electron launcher reads the
    # actual port from uvicorn's stdout.
    port = int(os.environ.get("CODEN_PORT", "0"))

    try:
        from server.app.main import app
    except ImportError as exc:
        print(f"[coden-server] failed to import app: {exc}", file=sys.stderr)
        return 1

    uvicorn.run(app, host=host, port=port, log_level="info")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
