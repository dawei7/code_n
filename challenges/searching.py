"""Searching challenges."""

import random
from typing import Any, Optional

from code_n.challenge import Challenge, ChallengeInfo
from code_n.counter import ComplexityClass
from code_n.grid import Grid, CellType
from code_n.tracked import TrackedList, TrackedGrid, TrackedQueue, TrackedStack


class LinearSearchChallenge(Challenge):
    """Find a target value in an unsorted array."""

    def __init__(self):
        super().__init__()
        self._data: list[int] = []
        self._target: int = 0
        self._expected: int = -1

    @property
    def info(self) -> ChallengeInfo:
        return ChallengeInfo(
            id="search_01",
            name="Linear Search",
            description=(
                "Find the index of the target value in the array.\n"
                "The array is NOT sorted.\n"
                "Return the index, or -1 if not found.\n"
                "Requirement: O(n)"
            ),
            category="searching",
            difficulty=1,
            required_complexity=ComplexityClass.O_N,
            hint="Check each element one by one until you find it.",
        )

    def setup(self, n: int, seed: Optional[int] = None) -> dict[str, Any]:
        rng = random.Random(seed)
        self._data = [rng.randint(1, 99) for _ in range(n)]
        # Pick a random target that exists
        target_idx = rng.randint(0, n - 1)
        self._target = self._data[target_idx]
        self._expected = target_idx

        self.grid = Grid(n, 3)
        self.grid.fill_row(0, self._data, CellType.VALUE)
        # Mark the target
        self.grid.set(target_idx, 0, CellType.GOAL, self._target)

        return {"data": TrackedList(self._data), "target": self._target}

    def verify(self, result: Any) -> bool:
        # Accept any index where the value matches
        if isinstance(result, int) and 0 <= result < len(self._data):
            return self._data[result] == self._target
        return result == -1 and self._target not in self._data


class BinarySearchChallenge(Challenge):
    """Find a target in a SORTED array efficiently."""

    def __init__(self):
        super().__init__()
        self._data: list[int] = []
        self._target: int = 0
        self._expected: int = -1

    @property
    def info(self) -> ChallengeInfo:
        return ChallengeInfo(
            id="search_02",
            name="Binary Search",
            description=(
                "Find the index of the target value in a SORTED array.\n"
                "The array is sorted in ascending order.\n"
                "Return the index, or -1 if not found.\n"
                "Requirement: O(log n) - linear search will FAIL!"
            ),
            category="searching",
            difficulty=3,
            required_complexity=ComplexityClass.O_LOG_N,
            hint="Check the middle element. If target is smaller, search left half; if larger, search right half.",
        )

    def setup(self, n: int, seed: Optional[int] = None) -> dict[str, Any]:
        rng = random.Random(seed)
        self._data = sorted(rng.sample(range(1, n * 3), n))
        target_idx = rng.randint(0, n - 1)
        self._target = self._data[target_idx]
        self._expected = target_idx

        self.grid = Grid(n, 3)
        self.grid.fill_row(0, self._data, CellType.SORTED)
        self.grid.set(target_idx, 0, CellType.GOAL, self._target)

        return {"data": TrackedList(self._data), "target": self._target, "n": n}

    def verify(self, result: Any) -> bool:
        if isinstance(result, int) and 0 <= result < len(self._data):
            return self._data[result] == self._target
        return False


class BFSGridChallenge(Challenge):
    """Find shortest path in a 2D grid using BFS."""

    def __init__(self):
        super().__init__()
        self._grid_data: list[list[int]] = []
        self._start: tuple[int, int] = (0, 0)
        self._goal: tuple[int, int] = (0, 0)
        self._expected_length: int = 0

    @property
    def info(self) -> ChallengeInfo:
        return ChallengeInfo(
            id="search_03",
            name="BFS Grid",
            description=(
                "Find the shortest path from START to GOAL in a 2D grid.\n"
                "0 = walkable, 1 = wall. Move in 4 directions (up/down/left/right).\n"
                "Return the path length (number of steps), or -1 if no path.\n"
                "Requirement: O(n²) where n = grid side length."
            ),
            category="searching",
            difficulty=5,
            required_complexity=ComplexityClass.O_N2,
            hint="Use a queue. Start from START, explore all neighbors level by level.",
        )

    def setup(self, n: int, seed: Optional[int] = None) -> dict[str, Any]:
        rng = random.Random(seed)
        size = max(5, int(n ** 0.5) + 2)
        self._n = size

        # Generate a grid with some walls (30% wall density)
        self._grid_data = [
            [1 if rng.random() < 0.3 else 0 for _ in range(size)]
            for _ in range(size)
        ]

        # Ensure start and goal are open
        self._start = (0, 0)
        self._goal = (size - 1, size - 1)
        self._grid_data[0][0] = 0
        self._grid_data[size - 1][size - 1] = 0

        # Ensure a path exists by carving one
        x, y = 0, 0
        while x < size - 1 or y < size - 1:
            self._grid_data[y][x] = 0
            if x < size - 1 and (y >= size - 1 or rng.random() < 0.5):
                x += 1
            else:
                y += 1
        self._grid_data[size - 1][size - 1] = 0

        # Calculate expected shortest path with BFS
        self._expected_length = self._bfs_solve(size)

        # Visual grid
        self.grid = Grid(size, size)
        for gy in range(size):
            for gx in range(size):
                if self._grid_data[gy][gx] == 1:
                    self.grid.set(gx, gy, CellType.WALL)
                else:
                    self.grid.set(gx, gy, CellType.EMPTY)
        self.grid.set(0, 0, CellType.START, "S")
        self.grid.set(size - 1, size - 1, CellType.GOAL, "G")

        grid = TrackedGrid(size, size)
        for gy in range(size):
            for gx in range(size):
                grid._data[gy][gx] = self._grid_data[gy][gx]

        return {
            "grid": grid,
            "start": self._start,
            "goal": self._goal,
            "size": size,
        }

    def _bfs_solve(self, size: int) -> int:
        from collections import deque
        q = deque([(0, 0, 0)])
        visited = {(0, 0)}
        while q:
            x, y, dist = q.popleft()
            if (x, y) == self._goal:
                return dist
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < size and 0 <= ny < size and (nx, ny) not in visited and self._grid_data[ny][nx] == 0:
                    visited.add((nx, ny))
                    q.append((nx, ny, dist + 1))
        return -1

    def verify(self, result: Any) -> bool:
        return result == self._expected_length


class DFSGridChallenge(Challenge):
    """Explore all reachable cells in a grid using DFS."""

    def __init__(self):
        super().__init__()
        self._grid_data: list[list[int]] = []
        self._expected_count: int = 0

    @property
    def info(self) -> ChallengeInfo:
        return ChallengeInfo(
            id="search_04",
            name="DFS Grid",
            description=(
                "Count all reachable cells from the top-left corner.\n"
                "0 = walkable, 1 = wall. Move in 4 directions.\n"
                "Return the total number of reachable cells (including start).\n"
                "Requirement: O(n²) where n = grid side length."
            ),
            category="searching",
            difficulty=4,
            required_complexity=ComplexityClass.O_N2,
            hint="Use a stack (or recursion). Mark cells as visited and explore neighbors.",
        )

    def setup(self, n: int, seed: Optional[int] = None) -> dict[str, Any]:
        rng = random.Random(seed)
        size = max(5, int(n ** 0.5) + 2)
        self._n = size

        self._grid_data = [
            [1 if rng.random() < 0.25 else 0 for _ in range(size)]
            for _ in range(size)
        ]
        self._grid_data[0][0] = 0

        # Count reachable
        self._expected_count = self._dfs_count(size)

        self.grid = Grid(size, size)
        for gy in range(size):
            for gx in range(size):
                if self._grid_data[gy][gx] == 1:
                    self.grid.set(gx, gy, CellType.WALL)
                else:
                    self.grid.set(gx, gy, CellType.EMPTY)
        self.grid.set(0, 0, CellType.START, "S")

        grid = TrackedGrid(size, size)
        for gy in range(size):
            for gx in range(size):
                grid._data[gy][gx] = self._grid_data[gy][gx]

        return {"grid": grid, "start": (0, 0), "size": size}

    def _dfs_count(self, size: int) -> int:
        visited = set()
        stack = [(0, 0)]
        while stack:
            x, y = stack.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < size and 0 <= ny < size and (nx, ny) not in visited and self._grid_data[ny][nx] == 0:
                    stack.append((nx, ny))
        return len(visited)

    def verify(self, result: Any) -> bool:
        return result == self._expected_count
