"""Sorting challenges."""

import random
from typing import Any, Optional

from code_n.challenge import Challenge, ChallengeInfo
from code_n.counter import ComplexityClass
from code_n.grid import Grid, CellType
from code_n.tracked import TrackedList, unwrap_tracked


def _is_sorted_result(result: Any, expected_data: list[int], working_data: TrackedList | None = None) -> bool:
    expected = sorted(expected_data)
    if result is None and working_data is not None:
        return working_data.raw == expected
    if isinstance(result, TrackedList):
        return result.raw == expected
    if isinstance(result, (list, tuple)):
        values = [unwrap_tracked(value) for value in result]
        return values == expected
    return False


class BubbleSortChallenge(Challenge):
    """Sort the array with normal Python indexing and assignment."""

    def __init__(self):
        super().__init__()
        self._data: list[int] = []
        self._working_data: TrackedList | None = None

    @property
    def info(self) -> ChallengeInfo:
        return ChallengeInfo(
            id="sort_01",
            name="Bubble Sort",
            description=(
                "Sort the array using normal Python indexing and assignment.\n"
                "Requirement: O(n²) - just get it sorted correctly!"
            ),
            category="sorting",
            difficulty=2,
            required_complexity=ComplexityClass.O_N2,
            hint="Move larger values toward the end of the list, one pass at a time.",
        )

    def setup(self, n: int, seed: Optional[int] = None) -> dict[str, Any]:
        rng = random.Random(seed)
        self._data = [rng.randint(1, 99) for _ in range(n)]

        self.grid = Grid(n, 3)
        self.grid.fill_row(0, self._data, CellType.UNSORTED)

        self._working_data = TrackedList(self._data)
        return {"data": self._working_data, "n": n}

    def verify(self, result: Any) -> bool:
        return _is_sorted_result(result, self._data, self._working_data)


class SelectionSortChallenge(Challenge):
    """Sort by repeatedly finding the minimum."""

    def __init__(self):
        super().__init__()
        self._data: list[int] = []
        self._working_data: TrackedList | None = None

    @property
    def info(self) -> ChallengeInfo:
        return ChallengeInfo(
            id="sort_02",
            name="Selection Sort",
            description=(
                "Sort the array by finding the minimum element and placing it.\n"
                "For each position, find the minimum in the remaining unsorted portion.\n"
                "Requirement: O(n²)"
            ),
            category="sorting",
            difficulty=2,
            required_complexity=ComplexityClass.O_N2,
            hint="For each index i, find min in [i..n-1] and swap it to position i.",
        )

    def setup(self, n: int, seed: Optional[int] = None) -> dict[str, Any]:
        rng = random.Random(seed)
        self._data = [rng.randint(1, 99) for _ in range(n)]

        self.grid = Grid(n, 3)
        self.grid.fill_row(0, self._data, CellType.UNSORTED)

        self._working_data = TrackedList(self._data)
        return {"data": self._working_data, "n": n}

    def verify(self, result: Any) -> bool:
        return _is_sorted_result(result, self._data, self._working_data)


class InsertionSortChallenge(Challenge):
    """Sort by inserting each element into its correct position."""

    def __init__(self):
        super().__init__()
        self._data: list[int] = []
        self._working_data: TrackedList | None = None

    @property
    def info(self) -> ChallengeInfo:
        return ChallengeInfo(
            id="sort_03",
            name="Insertion Sort",
            description=(
                "Sort the array by inserting each element into the sorted portion.\n"
                "Requirement: O(n²) worst case, but aim for fewer ops on nearly-sorted data."
            ),
            category="sorting",
            difficulty=3,
            required_complexity=ComplexityClass.O_N2,
            hint="For each element, shift larger elements right to make room.",
        )

    def setup(self, n: int, seed: Optional[int] = None) -> dict[str, Any]:
        rng = random.Random(seed)
        self._data = [rng.randint(1, 99) for _ in range(n)]

        self.grid = Grid(n, 3)
        self.grid.fill_row(0, self._data, CellType.UNSORTED)

        self._working_data = TrackedList(self._data)
        return {"data": self._working_data, "n": n}

    def verify(self, result: Any) -> bool:
        return _is_sorted_result(result, self._data, self._working_data)


class MergeSortChallenge(Challenge):
    """Sort efficiently using divide and conquer."""

    def __init__(self):
        super().__init__()
        self._data: list[int] = []
        self._working_data: TrackedList | None = None

    @property
    def info(self) -> ChallengeInfo:
        return ChallengeInfo(
            id="sort_04",
            name="Merge Sort",
            description=(
                "Sort the array in O(n log n) time using divide and conquer.\n"
                "Split the array in half, sort each half, then merge.\n"
                "Requirement: O(n log n) - quadratic solutions will FAIL!"
            ),
            category="sorting",
            difficulty=5,
            required_complexity=ComplexityClass.O_N_LOG_N,
            hint="Recursively split, then merge two sorted halves with a two-pointer technique.",
        )

    def setup(self, n: int, seed: Optional[int] = None) -> dict[str, Any]:
        rng = random.Random(seed)
        self._data = [rng.randint(1, 99) for _ in range(n)]

        self.grid = Grid(n, 5)
        self.grid.fill_row(0, self._data, CellType.UNSORTED)

        self._working_data = TrackedList(self._data)
        return {"data": self._working_data, "n": n}

    def verify(self, result: Any) -> bool:
        return _is_sorted_result(result, self._data, self._working_data)


class QuickSortChallenge(Challenge):
    """Sort using a pivot-based partition scheme."""

    def __init__(self):
        super().__init__()
        self._data: list[int] = []
        self._working_data: TrackedList | None = None

    @property
    def info(self) -> ChallengeInfo:
        return ChallengeInfo(
            id="sort_05",
            name="Quick Sort",
            description=(
                "Sort the array using partitioning around a pivot.\n"
                "Choose a pivot, partition elements around it, recurse.\n"
                "Requirement: O(n log n) average case."
            ),
            category="sorting",
            difficulty=5,
            required_complexity=ComplexityClass.O_N_LOG_N,
            hint="Pick a pivot, put smaller elements left and larger right, then recurse.",
        )

    def setup(self, n: int, seed: Optional[int] = None) -> dict[str, Any]:
        rng = random.Random(seed)
        self._data = [rng.randint(1, 99) for _ in range(n)]

        self.grid = Grid(n, 5)
        self.grid.fill_row(0, self._data, CellType.UNSORTED)

        self._working_data = TrackedList(self._data)
        return {"data": self._working_data, "n": n}

    def verify(self, result: Any) -> bool:
        return _is_sorted_result(result, self._data, self._working_data)
