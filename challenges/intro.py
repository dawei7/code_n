"""Introduction challenge - Hello Grid."""

import random
from typing import Any, Optional

from code_n.challenge import Challenge, ChallengeInfo
from code_n.branding import GAME_TITLE
from code_n.counter import ComplexityClass
from code_n.grid import Grid, CellType
from code_n.tracked import TrackedList


class IntroHelloGrid(Challenge):
    """First challenge: simply iterate through a list and find the maximum value."""

    def __init__(self):
        super().__init__()
        self._data: list[int] = []
        self._expected: int = 0

    @property
    def info(self) -> ChallengeInfo:
        return ChallengeInfo(
            id="intro_01",
            name="Hello Grid",
            description=(
                f"Welcome to {GAME_TITLE}!\n"
                "Your task: Find the maximum value in the grid's first row.\n"
                "Use normal Python indexing and comparisons - every read and compare counts.\n"
                "Requirement: Solve it in O(n) operations."
            ),
            category="intro",
            difficulty=1,
            required_complexity=ComplexityClass.O_N,
            hint="Simply iterate through the list once, keeping track of the max.",
        )

    def setup(self, n: int, seed: Optional[int] = None) -> dict[str, Any]:
        rng = random.Random(seed)
        self._data = [rng.randint(1, 99) for _ in range(n)]
        self._expected = max(self._data)

        # Set up the visual grid
        self.grid = Grid(n, 3)
        self.grid.fill_row(0, self._data, CellType.UNSORTED)

        # Return tracked data for the player
        return {"data": TrackedList(self._data)}

    def verify(self, result: Any) -> bool:
        return result == self._expected
