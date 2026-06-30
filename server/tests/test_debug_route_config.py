"""Tests for packaged debugger runtime selection."""
from __future__ import annotations

import os
import sys
import unittest
from unittest.mock import patch

from . import conftest  # noqa: F401
from server.app.routes import debug


class DebugRouteConfigTest(unittest.TestCase):
    def test_packaged_debug_uses_configured_runtime(self) -> None:
        with patch.dict(
            os.environ,
            {
                "CODEN_PACKAGED_SERVER": "1",
                "CODEN_DEBUG_PYTHON": sys.executable,
            },
        ):
            self.assertEqual(debug._debug_python_exe(), sys.executable)

    def test_packaged_debug_does_not_fall_back_to_system_python(self) -> None:
        with patch.dict(
            os.environ,
            {
                "CODEN_PACKAGED_SERVER": "1",
                "CODEN_DEBUG_PYTHON": r"C:\missing\python.exe",
            },
        ):
            with self.assertRaises(debug.DebugPythonUnavailable) as ctx:
                debug._debug_python_exe()
        self.assertIn("bundled debug Python runtime", str(ctx.exception))

    def test_dev_debug_uses_current_interpreter(self) -> None:
        with patch.dict(
            os.environ,
            {
                "CODEN_PACKAGED_SERVER": "",
                "CODEN_DEBUG_PYTHON": "",
                "CODEN_PYTHON_EXE": "",
            },
        ):
            self.assertEqual(debug._debug_python_exe(), sys.executable)
