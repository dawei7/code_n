"""Test fixtures for the server tests.

Sets the ``CODEN_PROGRESS_FILE`` and ``CODEN_SOLUTIONS_DIR`` env
vars to per-process temp paths before any ``server.app`` import,
so the tests never touch the real ``progress.json`` or
``solutions/`` directory.

The :class:`fastapi.testclient.TestClient` fixture is exposed as
a module-level singleton because creating the FastAPI app (which
imports the challenge registry) is expensive — on the order of a
few hundred ms — and the 6 test modules below reuse the same
client.
"""
from __future__ import annotations

import os
import sys
import tempfile
import unittest
from pathlib import Path


# ---------------------------------------------------------------------------
# Resolve the repo root and set the per-process env vars BEFORE importing
# any ``server.app`` module. ``config.py`` reads the env at import time.
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
assert (REPO_ROOT / "code_n").is_dir(), f"Could not find engine at {REPO_ROOT / 'code_n'}"
assert (REPO_ROOT / "challenges").is_dir(), f"Could not find challenges at {REPO_ROOT / 'challenges'}"


# Make the project root importable so `from server.app...` works in tests.
sys.path.insert(0, str(REPO_ROOT))

# Per-process temp home so progress.json + solutions/ don't pollute the repo.
_TEST_HOME = Path(tempfile.mkdtemp(prefix="coden-server-tests-"))
_TEST_PROGRESS = _TEST_HOME / "progress.json"
_TEST_SOLUTIONS = _TEST_HOME / "solutions"
_TEST_SOLUTIONS.mkdir(parents=True, exist_ok=True)
os.environ["CODEN_HOME"] = str(_TEST_HOME)
os.environ["CODEN_PROGRESS_FILE"] = str(_TEST_PROGRESS)
os.environ["CODEN_SOLUTIONS_DIR"] = str(_TEST_SOLUTIONS)


# Now safe to import the FastAPI app.
from fastapi.testclient import TestClient  # noqa: E402

from server.app.main import app  # noqa: E402


# Single shared client — creating the app is expensive (registry import).
CLIENT = TestClient(app)


class _Base(unittest.TestCase):
    """Base class for all server tests.

    Provides a self-attached :class:`TestClient` and ensures the
    progress file is reset before each test.
    """

    def setUp(self) -> None:
        self.client = CLIENT
        # Reset progress between tests so PUT state doesn't leak.
        if _TEST_PROGRESS.exists():
            _TEST_PROGRESS.unlink()
        # Clean up any solution files written by previous tests.
        for child in _TEST_SOLUTIONS.iterdir():
            if child.is_file():
                child.unlink()

    def tearDown(self) -> None:
        # Best-effort cleanup. The test runner's tmp dir is wiped on
        # process exit anyway, so we don't need to be aggressive.
        pass
