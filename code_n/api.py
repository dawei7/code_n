"""Player-facing API - the public interface players import in their scripts.

This module provides everything a player needs to solve challenges:
- Tracked data structures for the challenge INPUT (list, grid)
- The challenge runner
- Grid visualization helpers

Queue / stack / set are NOT provided - the player builds
their own (e.g. ``collections.deque`` or a plain list).
"""

from .tracked import TrackedList, TrackedGrid
from .counter import get_counter, reset_counter, ComplexityClass
from .grid import Grid, CellType
from .renderer import Renderer


__all__ = [
    "TrackedList",
    "TrackedGrid",
    "get_counter",
    "reset_counter",
    "ComplexityClass",
    "Grid",
    "CellType",
    "Renderer",
]
