"""Introduction algorithms - the first thing every player sees.

This category is intentionally tiny. Its job is to teach the
basic ``solve(args) -> result`` contract without forcing the
player to think about any specific algorithm yet.

The bit-manipulation specs (bit_01..bit_09, previously
mis-filed here) have been extracted to their own
``bit_manipulation`` category (see challenges/algorithms/
bit_manipulation.py).
"""


from __future__ import annotations

import random
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.branding import GAME_TITLE
from code_n.counter import ComplexityClass
from code_n.grid import Grid, CellType


# --- Setup / verify helpers (module-level so they're picklable,
# testable in isolation, and never accidentally close over
# per-instance state).

def _setup_hello_grid(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    challenge._data = [rng.randint(1, 99) for _ in range(n)]
    challenge._expected = max(challenge._data)

    challenge.grid = Grid(n, 3)
    challenge.grid.fill_row(0, challenge._data, CellType.UNSORTED)

    # The player receives the same list reference the engine
    # keeps in challenge._data — so the verifier can read
    # any in-place mutations via challenge._data. The old
    # TrackedList wrapper (removed in v0.8.5) just made the
    # reference explicit; a plain list works the same way.
    return {"data": challenge._data}


def _verify_hello_grid(challenge, result: Any) -> bool:
    return result == challenge._expected


# --- Specs ---

INTRO_01_SOURCE = '''\
"""Optimal solution for intro_01: Hello Grid.

Find the maximum value in a list-like input. O(n) solution.
"""


def solve(data):
    """Iterate once, track the running maximum."""
    n = len(data)
    best = data[0]
    for i in range(1, n):
        value = data[i]
        if value > best:
            best = value
    return best
'''


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="intro_01",
        name="Hello Grid",
        category="intro",
        difficulty=1,
        required_complexity=ComplexityClass.O_N,
        description=(
            f"Welcome to {GAME_TITLE}!\n"
            "Your task: Find the maximum value in the grid's first row.\n"
            "Use normal Python indexing and comparisons - every read and compare counts.\n"
            "Requirement: Solve it in O(n) operations."
        ),
        source_url="",  # Game-original, not a GFG article
        params=["data"],
        inputs={
            "data": "list-like of n integers. Read with data[i].",
        },
        returns="the maximum value in data.",
        source=INTRO_01_SOURCE,
        setup_fn=_setup_hello_grid,
        verify_fn=_verify_hello_grid,
        hint="Simply iterate through the list once, keeping track of the max.",
        samples=[
            Sample("data = [4, 9, 2]", "9"),
            Sample("data = [7]", "7"),
            Sample("data = [1, 5, 5, 3]", "5"),
        ],
        children=["sort_01", "search_01", "graph_01", "dp_01"],
    ),
]
