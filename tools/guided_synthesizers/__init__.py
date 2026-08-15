"""Specialized pedagogical synthesizers for algorithmic problem archetypes.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def detect_archetype(meta: dict[str, Any]) -> str:
    topics = {t.get("name", "").lower() for t in meta.get("topics", []) if isinstance(t, dict)}
    category = meta.get("category", "").lower()

    if "linked list" in topics or "doubly-linked list" in topics:
        return "linked_list"
    if "monotonic stack" in topics or "monotonic queue" in topics:
        return "monotonic_stack"
    if "sliding window" in topics:
        return "sliding_window"
    if "two pointers" in topics:
        return "two_pointers"
    if "binary search" in topics:
        return "binary_search"
    if "tree" in topics or "binary tree" in topics or "binary search tree" in topics:
        return "tree"
    if "graph" in topics or "breadth-first search" in topics or "depth-first search" in topics or "topological sort" in topics or "union find" in topics:
        return "graph"
    if "dynamic programming" in topics or "memoization" in topics:
        return "dynamic_programming"
    if "greedy" in topics:
        return "greedy"
    if "backtracking" in topics:
        return "backtracking"
    return "general"
