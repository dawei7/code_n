"""Test helpers shared across the cOde(n) test suite.

Run with:
    .venv/Scripts/python.exe -m pytest tests
"""
from __future__ import annotations

import sys
from pathlib import Path

# Ensure project root is importable so `import engine` works when running tests
# from any directory.
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
