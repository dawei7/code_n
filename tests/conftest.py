"""Test helpers shared across the cOde(n) test suite.

Run with:
    .venv/Scripts/python.exe -m unittest discover -s tests -v
"""
from __future__ import annotations

import sys
from pathlib import Path

# Ensure project root is importable so `import code_n` works when running tests
# from any directory.
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
