"""Smoke tests for the debug route handlers.

These tests are currently SKIPPED — the debugpy in-process
mode + the FastAPI TestClient have a deadlock in the test
process that we haven't fully traced. The infrastructure
(controller, route, DAP client) is unit-tested in
``test_debug_controller.py``. The end-to-end flow needs
manual smoke-testing in a real environment.
"""
from __future__ import annotations

import unittest

from . import conftest  # noqa: F401


@unittest.skip("debugpy in-process mode + TestClient deadlock; needs manual e2e")
class DebugRoutesSmokeTest(conftest._Base):
    """The route handlers' surface behavior (skipped)."""

    def test_unknown_challenge_returns_500(self) -> None:
        pass

    def test_session_creation_returns_id_and_ws_url(self) -> None:
        pass

    def test_unknown_session_websocket_closes(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
