"""Entry point for the PyInstaller-bundled cOde(n) server.

This module is the script PyInstaller bundles into ``coden-server.exe``.
It runs the FastAPI app on a random free port and writes the
bound port to a file (path from ``CODEN_PORT_FILE`` env var) so
the Electron launcher can discover it without parsing stdout.

The stdout-based port-parsing (the older approach) is unreliable
when this exe is spawned by a GUI-subsystem Electron app: the
PyInstaller bootloader's stdout doesn't always reach the parent's
pipe. The port file is the canonical signal. The Electron launcher
in ``electron/src/server-process.ts`` polls for the file with a
10s deadline, then polls ``/api/health`` for liveness.

For dev (``python -m uvicorn server.app.main:app``) the env var
is unset so the port-file step is a no-op — uvicorn's normal
stdout logging is enough.

Exit code: 0 on clean shutdown, non-zero if uvicorn fails to
start or the app fails to import.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

import uvicorn


# Read the env at import time so the port-file callback (and
# uvicorn.run) see the same value.
CODEN_PORT_FILE = os.environ.get("CODEN_PORT_FILE")
HOST = os.environ.get("CODEN_HOST", "127.0.0.1")
# Port 0 = "pick a free port"; the actual bound port goes to
# stdout AND to the port file (so both dev and Electron can pick
# it up).
INITIAL_PORT = int(os.environ.get("CODEN_PORT", "0"))


class PortWritingServer(uvicorn.Server):
    """A uvicorn.Server subclass that writes the bound port to a
    file once the socket is bound. The file-based signalling is
    more reliable than parsing stdout when the parent process is
    a Windows GUI subsystem app (Electron).

    Implementation note: ``super().startup(sockets)`` is the
    standard uvicorn startup coroutine; after it returns,
    ``self.servers`` is populated with the bound server instances
    and the actual port is in ``sockets[0].getsockname()[1]``.
    """

    actual_port: int | None = None

    async def startup(self, sockets=None):  # type: ignore[override]
        await super().startup(sockets)
        if self.servers:
            sock = self.servers[0].sockets[0]
            self.actual_port = sock.getsockname()[1]
            print(f"[coden-server] bound to 127.0.0.1:{self.actual_port}")
            if CODEN_PORT_FILE:
                try:
                    Path(CODEN_PORT_FILE).write_text(
                        str(self.actual_port), encoding="utf-8"
                    )
                    print(f"[coden-server] wrote port to {CODEN_PORT_FILE}")
                except OSError as exc:
                    print(f"[coden-server] could not write port file: {exc}")


def main() -> int:
    try:
        from server.app.main import app
    except ImportError as exc:
        print(f"[coden-server] failed to import app: {exc}", file=sys.stderr)
        return 1

    config = uvicorn.Config(
        app,
        host=HOST,
        port=INITIAL_PORT,
        log_level="info",
    )
    server = PortWritingServer(config=config)
    server.run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
