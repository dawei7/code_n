"""Player-facing API - the public interface players import in their scripts.

This module provides everything a player needs to solve challenges:
- Tracked data structures (lists, grids, queues, stacks)
- The challenge runner
- Grid visualization helpers
"""

from .tracked import TrackedList, TrackedGrid, TrackedQueue, TrackedStack, TrackedSet
from .counter import get_counter, reset_counter, ComplexityClass
from .grid import Grid, CellType
from .renderer import Renderer


__all__ = [
    "TrackedList",
    "TrackedGrid",
    "TrackedQueue",
    "TrackedStack",
    "TrackedSet",
    "get_counter",
    "reset_counter",
    "ComplexityClass",
    "Grid",
    "CellType",
    "Renderer",
]
