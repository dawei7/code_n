"""Server configuration.

All paths and tunables are resolved from environment variables at import
time, with sensible defaults that match the project layout in dev. The
Electron desktop wrapper sets ``CODEN_HOME`` to ``app.getPath('userData')``
in production so that ``progress.json`` and ``solutions/`` live in the
user's writable app data directory. ``CODEN_WEB_DIST`` points to the
bundled React build (``resources/web-dist/``) so the FastAPI server
can mount the UI at ``/``.
"""
from __future__ import annotations

import os
from pathlib import Path

# Project root: two parents up from this file (server/app/config.py -> server/app -> server -> repo).
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# User-writable home: defaults to the repo root in dev. Electron sets this
# to `app.getPath('userData')` when it spawns the bundled server.
CODEN_HOME = Path(os.environ.get("CODEN_HOME", str(PROJECT_ROOT)))

# Server / data paths.
PROGRESS_FILE = Path(os.environ.get("CODEN_PROGRESS_FILE", str(CODEN_HOME / "progress.json")))
SOLUTIONS_DIR = Path(os.environ.get("CODEN_SOLUTIONS_DIR", str(CODEN_HOME / "solutions")))

# Bundled React build: where the FastAPI server serves the UI from.
# In dev: defaults to <repo>/web/dist. In production (Electron):
# the Electron main process sets CODEN_WEB_DIST to the absolute path
# of ``resources/web-dist/`` (the extraResource).
WEB_DIST = Path(os.environ.get("CODEN_WEB_DIST", str(PROJECT_ROOT / "web" / "dist")))

# Algorithm documentation files. Same dev/prod split as WEB_DIST:
# in dev the docs/ tree is at <repo>/docs; in the packaged app
# the Electron launcher sets CODEN_DOCS_DIR to the absolute path
# of ``resources/docs/`` (the extraResource).
DOCS_ROOT = Path(os.environ.get("CODEN_DOCS_DIR", str(PROJECT_ROOT / "docs")))

# Server config.
CODEN_HOST = os.environ.get("CODEN_HOST", "127.0.0.1")
CODEN_PORT = int(os.environ.get("CODEN_PORT", "8000"))
CODEN_LOG_LEVEL = os.environ.get("CODEN_LOG_LEVEL", "info")

# CORS allowed origins. Vite dev runs on :5173; Electron's BrowserWindow
# uses the `app://.` custom scheme in production. Tightening this list
# is fine; the server only ever binds to 127.0.0.1.
CORS_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "app://.",
    # Electron's BrowserWindow with `loadFile` sends `file://` as the
    # origin. We add it as a safety net for the dev launch.
    "file://",
]


def ensure_data_dirs() -> None:
    """Create the user-writable directories if missing.

    Called once at server startup. The solutions directory is the
    file the player edits in VSCode (``PUT /api/solutions/{id}``
    or direct file edits); cOde(n) reads it back on every Run.
    """
    CODEN_HOME.mkdir(parents=True, exist_ok=True)
    SOLUTIONS_DIR.mkdir(parents=True, exist_ok=True)
