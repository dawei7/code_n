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


def _solution_template(challenge_id: str, heading: str, description: str) -> str:
    safe_description = description.replace('"""', "'''")
    samples = sample_doc(challenge_id)
    sample_section = f"\n{samples}" if samples else ""
    if challenge_id == "sort_01":
        return (
            f'"""Solution for {heading}.\n\n'
            f'{safe_description}\n\n'
            'Inputs passed to solve():\n'
            '    data: list-like object containing n random integers.\n'
            '    n: number of items in data.\n\n'
            'Goal:\n'
            '    Sort data in ascending order, in place.\n\n'
            f'{samples}'
            'Return:\n'
            '    The same data object after it is sorted.\n'
            '"""\n\n'
            'def solve(data, n):\n'
            '    # Write your code here.\n'
            '    return data\n'
        )

    if challenge_id == "search_03":
        return (
            f'"""Solution for {heading}.\n\n'
            f'{safe_description}\n\n'
            'Inputs passed to solve():\n'
            '    grid: 2D list-like object. Read a cell with grid[row][column].\n'
            '          0 means walkable, 1 means wall.\n'
            '    start: (row, column) start position.\n'
            '    goal: (row, column) goal position.\n'
            '    size: width and height of the square grid.\n\n'
            'Index meaning:\n'
            '    The first number is the row. Rows go down the screen.\n'
            '    The second number is the column. Columns go left to right.\n'
            '    So [0][2] means row 0, column 2.\n\n'
            'Cell access:\n'
            '    row, column = start\n'
            '    value = grid[row][column]\n'
            '    # value == 0 means walkable; value == 1 means wall.\n\n'
            'Neighbor check:\n'
            '    if 0 <= next_row < size and 0 <= next_column < size and grid[next_row][next_column] == 0:\n'
            '        # [next_row][next_column] is inside the grid and walkable.\n\n'
            f'{samples}'
            'Return:\n'
            '    The shortest path length in steps. The generated challenge always has a path.\n'
            '"""\n\n'
            'def solve(grid, start, goal, size):\n'
            '    # Write your code here.\n'
            '    return None\n'
        )

    if challenge_id == "search_04":
        return (
            f'"""Solution for {heading}.\n\n'
            f'{safe_description}\n\n'
            'Inputs passed to solve():\n'
            '    grid: 2D list-like object. Read a cell with grid[row][column].\n'
            '          0 means walkable, 1 means wall.\n'
            '    start: (row, column) start position.\n'
            '    size: width and height of the square grid.\n\n'
            'Index meaning:\n'
            '    The first number is the row. Rows go down the screen.\n'
            '    The second number is the column. Columns go left to right.\n'
            '    So [0][2] means row 0, column 2.\n\n'
            'Cell access:\n'
            '    row, column = start\n'
            '    value = grid[row][column]\n'
            '    # value == 0 means walkable; value == 1 means wall.\n\n'
            'Neighbor check:\n'
            '    if 0 <= next_row < size and 0 <= next_column < size and grid[next_row][next_column] == 0:\n'
            '        # [next_row][next_column] is inside the grid and walkable.\n\n'
            f'{samples}'
            'Return:\n'
            '    The number of reachable walkable cells, including the start cell.\n'
            '"""\n\n'
            'def solve(grid, start, size):\n'
            '    # Write your code here.\n'
            '    return None\n'
        )

    return (
        f'"""Solution for {heading}.\n\n'
        f'{safe_description}\n'
        f'{sample_section}'
        f'"""\n\n'
        'def solve(**kwargs):\n'
        '    # Write your code here.\n'
        '    return None\n'
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
