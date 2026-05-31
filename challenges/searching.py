"""Searching challenges."""

import random
from typing import Any, Optional

from code_n.challenge import Challenge, ChallengeInfo
from code_n.counter import ComplexityClass, get_counter
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
                "The generated maze always has a route, but dense walls make guessing impossible.\n"
                "Use Python row/column indexing: grid[row][column].\n"
                "Rows go down the screen; columns go left to right.\n"
                "Return the shortest path length in steps.\n"
                "Requirement: O(n²) where n = grid side length."
            ),
            category="searching",
            difficulty=5,
            required_complexity=ComplexityClass.O_N2,
            hint="Use a queue. Start from START, explore all neighbors level by level.",
        )

    def setup(self, n: int, seed: Optional[int] = None) -> dict[str, Any]:
        rng = random.Random(seed)
        size = max(5, n)
        self._n = size
        self._start = (0, 0)
        self._goal = (size - 1, size - 1)

        self._grid_data, self._expected_length = self._generate_difficult_maze(size, rng)

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

    def _generate_difficult_maze(self, size: int, rng: random.Random) -> tuple[list[list[int]], int]:
        minimum_length = self._minimum_maze_length(size)
        attempts = 32 if size <= 150 else 12
        best_grid: list[list[int]] = []
        best_length = -1

        for _ in range(attempts):
            attempt_rng = random.Random(rng.randrange(2**63))
            grid_data = self._generate_maze_grid(size, attempt_rng)
            path_length = self._shortest_path_length(grid_data, size)
            if path_length > best_length:
                best_grid = grid_data
                best_length = path_length
            if path_length >= minimum_length:
                return grid_data, path_length

        return best_grid, best_length

    def _minimum_maze_length(self, size: int) -> int:
        if size < 15:
            return 0
        direct_corner_distance = (size - 1) * 2
        return max(direct_corner_distance * 5, size * 8)

    def _generate_maze_grid(self, size: int, rng: random.Random) -> list[list[int]]:
        grid_data = [[1 for _ in range(size)] for _ in range(size)]
        cell_rows = (size + 1) // 2
        cell_columns = (size + 1) // 2
        stack = [(0, 0)]
        visited = {(0, 0)}
        grid_data[0][0] = 0

        while stack:
            row_cell, column_cell = stack[-1]
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            rng.shuffle(directions)

            for row_step, column_step in directions:
                next_row_cell = row_cell + row_step
                next_column_cell = column_cell + column_step
                next_cell = (next_row_cell, next_column_cell)
                if not (0 <= next_row_cell < cell_rows and 0 <= next_column_cell < cell_columns):
                    continue
                if next_cell in visited:
                    continue

                grid_data[row_cell * 2 + row_step][column_cell * 2 + column_step] = 0
                grid_data[next_row_cell * 2][next_column_cell * 2] = 0
                visited.add(next_cell)
                stack.append(next_cell)
                break
            else:
                stack.pop()

        self._connect_goal_to_maze(grid_data, size, cell_rows, cell_columns)
        self._add_maze_cycles(grid_data, size, rng)
        return grid_data

    def _connect_goal_to_maze(
        self,
        grid_data: list[list[int]],
        size: int,
        cell_rows: int,
        cell_columns: int,
    ) -> None:
        goal_row, goal_column = self._goal
        anchor_row = (cell_rows - 1) * 2
        anchor_column = (cell_columns - 1) * 2

        for row in range(anchor_row, goal_row + 1):
            grid_data[row][anchor_column] = 0
        for column in range(anchor_column, goal_column + 1):
            grid_data[goal_row][column] = 0

    def _add_maze_cycles(self, grid_data: list[list[int]], size: int, rng: random.Random) -> None:
        candidates: list[tuple[int, int]] = []
        for row in range(1, size - 1):
            for column in range(1, size - 1):
                if grid_data[row][column] != 1:
                    continue
                vertical_join = (
                    grid_data[row - 1][column] == 0
                    and grid_data[row + 1][column] == 0
                    and grid_data[row][column - 1] == 1
                    and grid_data[row][column + 1] == 1
                )
                horizontal_join = (
                    grid_data[row][column - 1] == 0
                    and grid_data[row][column + 1] == 0
                    and grid_data[row - 1][column] == 1
                    and grid_data[row + 1][column] == 1
                )
                if vertical_join or horizontal_join:
                    candidates.append((row, column))

        rng.shuffle(candidates)
        cycle_count = min(len(candidates), max(1, size // 25, int(len(candidates) * 0.003)))
        for row, column in candidates[:cycle_count]:
            grid_data[row][column] = 0

    def _shortest_path_length(self, grid_data: list[list[int]], size: int) -> int:
        from collections import deque

        q = deque([(self._start[0], self._start[1], 0)])
        visited = {self._start}
        while q:
            row, column, distance = q.popleft()
            if (row, column) == self._goal:
                return distance
            for row_step, column_step in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_row = row + row_step
                next_column = column + column_step
                next_position = (next_row, next_column)
                if (
                    0 <= next_row < size
                    and 0 <= next_column < size
                    and next_position not in visited
                    and grid_data[next_row][next_column] == 0
                ):
                    visited.add(next_position)
                    q.append((next_row, next_column, distance + 1))
        return -1

    def _bfs_solve(self, size: int) -> int:
        return self._shortest_path_length(self._grid_data, size)

    def verify(self, result: Any) -> bool:
        return result == self._expected_length and get_counter().stats.reads > 0


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
                "Use Python row/column indexing: grid[row][column].\n"
                "Rows go down the screen; columns go left to right.\n"
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
        size = max(5, n)
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
        return result == self._expected_count and get_counter().stats.reads > 0
