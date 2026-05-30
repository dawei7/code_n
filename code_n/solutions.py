"""Utilities for the player's saved solution scripts."""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from typing import Optional


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
    if challenge_id == "sort_01":
        return (
            f'"""Solution for {heading}.\n\n'
            f'{safe_description}\n\n'
            'Inputs passed to solve():\n'
            '    data: TrackedList containing n random integers.\n'
            '    n: number of items in data.\n\n'
            'Goal:\n'
            '    Sort data in ascending order, in place.\n\n'
            'Allowed operations for this challenge:\n'
            '    data.compare(i, i + 1)  # compare adjacent items\n'
            '    data.swap(i, i + 1)     # swap adjacent items\n\n'
            'Return:\n'
            '    The same TrackedList object after it is sorted.\n'
            '"""\n\n'
            'from code_n.api import TrackedList\n\n\n'
            'def solve(data: TrackedList, n: int) -> TrackedList:\n'
            '    """Sort the received TrackedList and return it.\n\n'
            '    data.compare(i, j) returns:\n'
            '        -1 if data[i] < data[j]\n'
            '         0 if data[i] == data[j]\n'
            '         1 if data[i] > data[j]\n\n'
            '    For Bubble Sort, only compare and swap neighboring indices:\n'
            '        i and i + 1\n'
            '    """\n'
            '    raise NotImplementedError("Write your bubble sort here")\n'
        )

    return (
        f'"""Solution for {heading}.\n\n'
        f'{safe_description}\n'
        f'"""\n\n'
        'from code_n.api import TrackedList, TrackedGrid, TrackedQueue, TrackedStack, TrackedSet, get_counter\n\n\n'
        'def solve(**kwargs):\n'
        '    """Implement your algorithm here.\n\n'
        '    Run challenge info with:\n'
        f'        python main.py info {challenge_id}\n'
        '    """\n'
        '    raise NotImplementedError("Write your solution here")\n'
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
