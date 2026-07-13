"""Server configuration.

All paths and tunables are resolved from environment variables at import
time, with sensible defaults that match the project layout in dev. The
Electron desktop wrapper sets ``CODEN_HOME`` to ``app.getPath('userData')``
in production so that progress and personal solutions live in the user's
writable app data directory. ``CODEN_WEB_DIST`` points to the
bundled React build (``resources/web-dist/``) so the FastAPI server
can mount the UI at ``/``.
"""
from __future__ import annotations

import os
import shutil
from pathlib import Path

# Project root: two parents up from this file (server/app/config.py -> server/app -> server -> repo).
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# User-writable home. Development uses an ignored local data directory;
# Electron supplies ``app.getPath('userData')`` for installed builds. Keeping
# this separate from PROJECT_ROOT prevents personal work from being mistaken
# for canonical challenge data or committed to Git.
CODEN_HOME = Path(os.environ.get("CODEN_HOME", str(PROJECT_ROOT / ".coden-data")))

# Server / data paths.
PROGRESS_FILE = Path(os.environ.get("CODEN_PROGRESS_FILE", str(CODEN_HOME / "progress.json")))

# Writable overlay for per-user LeetCode work. It mirrors canonical package
# names while remaining physically separate from the read-only DSA resources:
#   <user-data>/dsa/leetcode/1_two-sum/user_solutions/python_v1.py
USER_DSA_ROOT = Path(os.environ.get("CODEN_USER_DSA_DIR", str(CODEN_HOME / "dsa")))
USER_LEETCODE_ROOT = Path(
    os.environ.get("CODEN_USER_LEETCODE_DIR", str(USER_DSA_ROOT / "leetcode"))
)

# Pre-overlay releases stored files under <user-data>/solutions. This path is
# read only by the one-time migration and is never used for new saves.
LEGACY_SOLUTIONS_DIR = Path(
    os.environ.get("CODEN_LEGACY_SOLUTIONS_DIR", str(CODEN_HOME / "solutions"))
)

# Bundled React build: where the FastAPI server serves the UI from.
# In dev: defaults to <repo>/web/dist. In production (Electron):
# the Electron main process sets CODEN_WEB_DIST to the absolute path
# of ``resources/web-dist/`` (the extraResource).
WEB_DIST = Path(os.environ.get("CODEN_WEB_DIST", str(PROJECT_ROOT / "web" / "dist")))

# Product overview shown by the Reference tab. Per-problem documentation lives
# with each canonical LeetCode package rather than in a parallel docs tree.
OVERVIEW_DOC = Path(
    os.environ.get("CODEN_OVERVIEW_DOC", str(PROJECT_ROOT / "README.md"))
)

# Canonical data-structures-and-algorithms dataset packages.
DSA_ROOT = Path(os.environ.get("CODEN_DSA_DIR", str(PROJECT_ROOT / "dsa")))

# Canonical LeetCode challenge packages. Each challenge owns its docs, cases,
# benchmarks, metadata, and language-specific optimal solutions in one folder.
LEETCODE_ROOT = Path(os.environ.get("CODEN_LEETCODE_DIR", str(DSA_ROOT / "leetcode")))

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

    Called once at server startup. The user LeetCode overlay stores the three
    versioned files edited from the in-app editor
    (``PUT /api/solutions/{id}``). Canonical challenge assets stay read-only.
    """
    CODEN_HOME.mkdir(parents=True, exist_ok=True)
    USER_LEETCODE_ROOT.mkdir(parents=True, exist_ok=True)
    # Development previously wrote progress.json at the repository root.
    # Preserve it when moving to the ignored .coden-data profile. Installed
    # builds already keep the same appData path across upgrades.
    default_dev_home = (PROJECT_ROOT / ".coden-data").resolve()
    legacy_progress = PROJECT_ROOT / "progress.json"
    if (
        CODEN_HOME.resolve() == default_dev_home
        and not PROGRESS_FILE.exists()
        and legacy_progress.is_file()
    ):
        PROGRESS_FILE.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(legacy_progress, PROGRESS_FILE)
