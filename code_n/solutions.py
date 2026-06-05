"""Utilities for the player's saved solution scripts."""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from typing import Optional

from .samples import sample_doc


def _app_root() -> str:
    if getattr(sys, "frozen", False):
        return os.path.dirname(os.path.abspath(sys.executable))
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


PROJECT_ROOT = _app_root()
SOLUTIONS_DIR = os.path.join(PROJECT_ROOT, "solutions")


@dataclass(frozen=True)
class SolutionPath:
    challenge_id: str
    path: str
    exists: bool


def ensure_solutions_dir() -> str:
    os.makedirs(SOLUTIONS_DIR, exist_ok=True)
    return SOLUTIONS_DIR


def default_solution_path(challenge_id: str) -> str:
    return os.path.join(ensure_solutions_dir(), f"{challenge_id}.py")


def resolve_solution_path(challenge_id: str, explicit_path: Optional[str] = None) -> SolutionPath:
    path = explicit_path or default_solution_path(challenge_id)
    return SolutionPath(challenge_id=challenge_id, path=path, exists=os.path.exists(path))


def solution_hint(challenge_id: str) -> str:
    path = default_solution_path(challenge_id)
    rel_path = os.path.relpath(path, PROJECT_ROOT)
    return (
        f"Create your solution at {rel_path}. "
        f"Then run: python run_challenge.py {challenge_id}"
    )


# Per-challenge template metadata. Each entry is (parameter list,
# input descriptions, return description). The template generator
# below uses this to build a clean stub with the EXACT parameter
# names from the challenge's setup() method - never **kwargs.
_CHALLENGE_TEMPLATES: dict[str, dict] = {
    "intro_01": {
        "params": ["data"],
        "inputs": {
            "data": "list-like of n integers. Read with data[i].",
        },
        "returns": "the maximum value in data.",
    },
    "sort_01": {
        "params": ["data", "n"],
        "inputs": {
            "data": "list-like of n random integers. Mutate in place.",
            "n": "length of data.",
        },
        "returns": "the same data object, sorted in place (in ascending order).",
    },
    "sort_02": {
        "params": ["data", "n"],
        "inputs": {
            "data": "list-like of n random integers. Mutate in place.",
            "n": "length of data.",
        },
        "returns": "the same data object, sorted in place (in ascending order).",
    },
    "sort_03": {
        "params": ["data", "n"],
        "inputs": {
            "data": "list-like of n random integers. Mutate in place.",
            "n": "length of data.",
        },
        "returns": "the same data object, sorted in place (in ascending order).",
    },
    "sort_04": {
        "params": ["data", "n"],
        "inputs": {
            "data": "list-like of n random integers. Mutate in place.",
            "n": "length of data.",
        },
        "returns": "the same data object, sorted in place (in ascending order).",
    },
    "sort_05": {
        "params": ["data", "n"],
        "inputs": {
            "data": "list-like of n random integers. Mutate in place.",
            "n": "length of data.",
        },
        "returns": "the same data object, sorted in place (in ascending order).",
    },
    "search_01": {
        "params": ["data", "target"],
        "inputs": {
            "data": "list-like of n random integers.",
            "target": "value to find in data.",
        },
        "returns": "the index of target in data, or -1 if not found.",
    },
    "search_02": {
        "params": ["data", "target", "n"],
        "inputs": {
            "data": "sorted list-like of n random integers.",
            "target": "value to find in data.",
            "n": "length of data.",
        },
        "returns": "the index of target in data, or -1 if not found.",
    },
    "search_03": {
        "params": ["grid", "start", "goal", "size"],
        "inputs": {
            "grid": "2D list-like. 0 = walkable, 1 = wall. Read with grid[row][column].",
            "start": "(row, column) start position.",
            "goal": "(row, column) goal position.",
            "size": "width and height of the square grid.",
        },
        "returns": "the length of the shortest path from start to goal in steps. The challenge always has a path.",
    },
    "search_04": {
        "params": ["grid", "start", "size"],
        "inputs": {
            "grid": "2D list-like. 0 = walkable, 1 = wall. Read with grid[row][column].",
            "start": "(row, column) start position.",
            "size": "width and height of the square grid.",
        },
        "returns": "the number of walkable cells reachable from start (including start).",
    },
    "graph_01": {
        "params": ["num_nodes", "edges"],
        "inputs": {
            "num_nodes": "number of nodes in the graph.",
            "edges": "list-like of (u, v) tuples representing undirected edges.",
        },
        "returns": "a dict mapping each node to a sorted list of its neighbors.",
    },
    "graph_04": {
        "params": ["num_nodes", "edges", "start"],
        "inputs": {
            "num_nodes": "number of nodes in the graph.",
            "edges": "list-like of (u, v, weight) tuples for directed edges.",
            "start": "source node.",
        },
        "returns": "a dict mapping each node to its shortest distance from start. Unreachable nodes get -1.",
    },
    "dp_01": {
        "params": ["n"],
        "inputs": {
            "n": "index of the Fibonacci number to compute.",
        },
        "returns": "the n-th Fibonacci number (fib(0)=0, fib(1)=1).",
    },
    "dp_02": {
        "params": ["n"],
        "inputs": {
            "n": "number of stairs.",
        },
        "returns": "the number of distinct ways to climb n stairs (1 or 2 steps at a time).",
    },
    "dp_03": {
        "params": ["weights", "values", "capacity", "n"],
        "inputs": {
            "weights": "list-like of item weights (length n).",
            "values": "list-like of item values (length n).",
            "capacity": "knapsack capacity.",
            "n": "number of items.",
        },
        "returns": "the maximum total value of items that fit in the knapsack.",
    },
    "dp_04": {
        "params": ["seq_a", "seq_b"],
        "inputs": {
            "seq_a": "first string (or list-like of characters).",
            "seq_b": "second string (or list-like of characters).",
        },
        "returns": "the length of the longest common subsequence of seq_a and seq_b.",
    },
}


def _solution_template(challenge_id: str, heading: str, description: str) -> str:
    """Build a starter file for the player.

    Every challenge now has a template with EXPLICIT parameter
    names (no more ``def solve(**kwargs):``). The templates live
    in ``_CHALLENGE_TEMPLATES``; the per-challenge entry says
    what the args are, what they mean, and what the function
    should return. The starter file is the same shape so the
    player can read the docstring, fill in the body, and not
    have to guess.
    """
    safe_description = description.replace('"""', "'''")
    samples = sample_doc(challenge_id)
    sample_section = f"\n{samples}" if samples else ""
    info = _CHALLENGE_TEMPLATES.get(challenge_id)
    if info is None:
        # Unknown challenge - fall back to a generic stub. Shouldn't
        # happen in practice; registry.py enumerates the supported
        # IDs.
        return (
            f'"""Solution for {heading}.\n\n'
            f'{safe_description}\n'
            f'{sample_section}'
            f'"""\n\n'
            'def solve():\n'
            '    # Write your code here.\n'
            '    return None\n'
        )

    params = info["params"]
    inputs = info["inputs"]
    returns = info["returns"]

    sig = "def solve(" + ", ".join(params) + "):"
    input_lines = []
    for name in params:
        if name in inputs:
            input_lines.append(f"    {name}: {inputs[name]}")
        else:
            input_lines.append(f"    {name}: (see description above)")

    return (
        f'"""Solution for {heading}.\n\n'
        f'{safe_description}\n\n'
        f'Inputs passed to solve():\n'
        + "\n".join(input_lines) + "\n\n"
        f'Goal:\n'
        f'    {returns}\n\n'
        f'{samples}'
        '"""\n\n'
        f'{sig}\n'
        f'    # Write your code here.\n'
        f'    return None\n'
    )


def create_solution_file(challenge_id: str, title: str = "", description: str = "") -> str:
    """Create the saved solution script for a challenge if it does not exist."""
    path = default_solution_path(challenge_id)
    if os.path.exists(path):
        return path

    heading = f"{challenge_id}: {title}" if title else challenge_id
    content = _solution_template(challenge_id, heading, description)
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)
    return path
