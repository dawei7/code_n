"""Searching algorithms.

Eight algorithms from GFG's "Searching Algorithms" catalog:

  01 Linear Search   - scan left-to-right, O(n)
  02 Binary Search   - halve the sorted range, O(log n)
  03 BFS Grid        - shortest path on a 2D maze, O(n^2)
  04 DFS Grid        - count reachable cells, O(n^2)
  05 Ternary Search  - split into three, O(log_3 n)
  06 Jump Search     - block-jump + linear, O(sqrt(n))
  07 Exponential     - find upper bound, then binary, O(log n)
  08 Interpolation   - estimate position by value, O(log log n) avg

The first two work on a flat list with a ``target``. The next two
work on a 2D grid (a richer setup). The last four cover the
classic O(log n)-ish variants from GFG's catalog.
"""

from __future__ import annotations

import random
from collections import deque
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.challenge import OP_AT_LEAST, OP_AT_MOST, OperationConstraint
from code_n.counter import ComplexityClass, get_counter
from code_n.grid import Grid, CellType
from code_n.tracked import TrackedGrid, TrackedList


# --- 1D search helpers shared by linear/binary/ternary/jump/
# exponential/interpolation. ---


def _setup_flat_search(
    challenge,
    n: int,
    seed: Optional[int],
    *,
    sorted_data: bool,
) -> dict[str, Any]:
    rng = random.Random(seed)
    if sorted_data == "rotated":
        base = sorted(rng.sample(range(1, max(2, n) * 3), n))
        # Rotate at a random pivot (always non-trivial for n > 1).
        if n > 1:
            pivot = rng.randint(1, n - 1)
            challenge._data = base[pivot:] + base[:pivot]
        else:
            challenge._data = base
    elif sorted_data:
        challenge._data = sorted(rng.sample(range(1, max(2, n) * 3), n))
    else:
        challenge._data = [rng.randint(1, 99) for _ in range(n)]
    if n > 0:
        target_idx = rng.randint(0, n - 1)
        challenge._target = challenge._data[target_idx]
        challenge._expected = target_idx
    else:
        challenge._target = 0
        challenge._expected = -1

    challenge.grid = Grid(n, 3)
    cell_type = CellType.SORTED if sorted_data else CellType.VALUE
    challenge.grid.fill_row(0, challenge._data, cell_type)
    if n > 0:
        challenge.grid.set(challenge._expected, 0, CellType.GOAL, challenge._target)

    out: dict[str, Any] = {
        "data": TrackedList(challenge._data),
        "target": challenge._target,
    }
    if sorted_data:
        out["n"] = n
    return out


def _verify_flat_search(challenge, result: Any) -> bool:
    # Linear search accepts any matching index; the others do too
    # in practice (the engine doesn't punish a player for finding
    # a duplicate of the target at a different position).
    if isinstance(result, int) and 0 <= result < len(challenge._data):
        return challenge._data[result] == challenge._target
    return result == -1 and challenge._target not in challenge._data


# --- 2D BFS / DFS shared helpers. ---


def _shortest_path_length(grid_data: list[list[int]], size: int, start: tuple[int, int], goal: tuple[int, int]) -> int:
    q: deque = deque([(start[0], start[1], 0)])
    visited = {start}
    while q:
        row, col, distance = q.popleft()
        if (row, col) == goal:
            return distance
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < size and 0 <= nc < size and (nr, nc) not in visited and grid_data[nr][nc] == 0:
                visited.add((nr, nc))
                q.append((nr, nc, distance + 1))
    return -1


def _generate_difficult_maze(
    challenge,
    size: int,
    rng: random.Random,
    goal: tuple[int, int],
) -> tuple[list[list[int]], int]:
    minimum_length = challenge._minimum_maze_length(size)
    attempts = 32 if size <= 150 else 12
    best_grid: list[list[int]] = []
    best_length = -1
    for _ in range(attempts):
        attempt_rng = random.Random(rng.randrange(2**63))
        grid_data = challenge._generate_maze_grid(size, attempt_rng, goal)
        path_length = _shortest_path_length(grid_data, size, (0, 0), goal)
        if path_length > best_length:
            best_grid = grid_data
            best_length = path_length
        if path_length >= minimum_length:
            return grid_data, path_length
    return best_grid, best_length


def _generate_maze_grid(challenge, size: int, rng: random.Random, goal: tuple[int, int]) -> list[list[int]]:
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
    challenge._connect_goal_to_maze(grid_data, size, cell_rows, cell_columns, goal)
    challenge._add_maze_cycles(grid_data, size, rng)
    return grid_data


def _connect_goal_to_maze(
    grid_data: list[list[int]],
    size: int,
    cell_rows: int,
    cell_columns: int,
    goal: tuple[int, int],
) -> None:
    goal_row, goal_column = goal
    anchor_row = (cell_rows - 1) * 2
    anchor_column = (cell_columns - 1) * 2
    for row in range(anchor_row, goal_row + 1):
        grid_data[row][anchor_column] = 0
    for column in range(anchor_column, goal_column + 1):
        grid_data[goal_row][column] = 0


def _add_maze_cycles(grid_data: list[list[int]], size: int, rng: random.Random) -> None:
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


# Module-level aliases so the spec factories can pass them in.
def _minimum_maze_length(self, size: int) -> int:
    if size < 15:
        return 0
    direct_corner_distance = (size - 1) * 2
    return max(direct_corner_distance * 5, size * 8)


# Bind the BFS/DFS helpers onto the challenge instance so the
# original class methods can be invoked as ``self._method``.
def _bind_2d_helpers(challenge):
    challenge._minimum_maze_length = _minimum_maze_length.__get__(challenge)
    challenge._generate_difficult_maze = _generate_difficult_maze.__get__(challenge)
    challenge._generate_maze_grid = _generate_maze_grid.__get__(challenge)
    challenge._connect_goal_to_maze = _connect_goal_to_maze
    challenge._add_maze_cycles = _add_maze_cycles


# --- 1D-search canonical sources. ---


SEARCH_01_SOURCE = '''\
"""Optimal solution for search_01: Linear Search.

Walk the array until the target is found or the end is reached.
O(n) time.
"""


def solve(data, target):
    for index in range(len(data)):
        if data[index] == target:
            return index
    return -1
'''

SEARCH_02_SOURCE = '''\
"""Optimal solution for search_02: Binary Search.

Sorted array; halve the search space each step. O(log n) time.
"""


def solve(data, target, n):
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        value = data[mid]
        if value == target:
            return mid
        if value < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
'''

SEARCH_05_SOURCE = '''\
"""Optimal solution for search_05: Ternary Search.

Sorted array; split the search range into three equal parts and
keep the one that can contain the target. O(log_3 n) time, but
with a higher constant factor than binary search - useful when
the comparison function is much cheaper than halving would imply.
"""


def solve(data, target, n):
    low, high = 0, n - 1
    while low <= high:
        third = (high - low) // 3
        mid1 = low + third
        mid2 = high - third
        if data[mid1] == target:
            return mid1
        if data[mid2] == target:
            return mid2
        if target < data[mid1]:
            high = mid1 - 1
        elif target > data[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1
    return -1
'''

SEARCH_06_SOURCE = '''\
"""Optimal solution for search_06: Jump Search.

Sorted array; jump ahead by a fixed block size m = sqrt(n) until
the block could contain the target, then linear-scan inside it.
O(sqrt(n)) time, O(1) extra space. Useful when jumping back is
expensive (e.g. rotating media).
"""


def solve(data, target, n):
    import math
    step = max(1, int(math.sqrt(n)))
    prev = 0
    # Find the block where the target could be.
    while prev < n and data[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    # Linear scan inside the block.
    for index in range(prev, min(step, n)):
        if data[index] == target:
            return index
    return -1
'''

SEARCH_07_SOURCE = '''\
"""Optimal solution for search_07: Exponential Search.

For unbounded / infinite arrays: double the index until the upper
bound is past the target, then binary-search inside it. O(log n)
time, no need to know n up front.
"""


def solve(data, target, n):
    if n == 0 or data[0] > target:
        return -1
    bound = 1
    while bound < n and data[bound] <= target:
        bound *= 2
    # Binary search in [bound/2, min(bound, n-1)].
    low, high = bound // 2, min(bound, n - 1)
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
'''

SEARCH_08_SOURCE = '''\
"""Optimal solution for search_08: Interpolation Search.

Like binary search, but the probe position is estimated from the
target's value, not the midpoint: pos = low + (target - data[low])
* (high - low) / (data[high] - data[low]). O(log log n) average
on uniformly distributed data; degenerates to O(n) otherwise.
"""


def solve(data, target, n):
    low, high = 0, n - 1
    while low <= high and data[low] <= target <= data[high]:
        if data[high] == data[low]:
            if data[low] == target:
                return low
            return -1
        # Probe position estimated from the target's value.
        pos = low + (target - data[low]) * (high - low) // (data[high] - data[low])
        if pos < low or pos > high:
            return -1
        value = data[pos]
        if value == target:
            return pos
        if value < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1
'''


SEARCH_09_SOURCE = '''\
"""Optimal solution for search_09: Fibonacci Search.

Sorted array; uses Fibonacci numbers to split the range. Always
shrinks by at least one Fibonacci number, so the loop runs in
O(log n) time. Like binary search, the range is split by index
(not value), but the split point is computed as Fib(m-2)/Fib(m)
of the range rather than the midpoint.
"""


def solve(data, target, n):
    if n == 0:
        return -1
    # Initialise the smallest Fibonacci >= n.
    fib2, fib1 = 0, 1
    fib = fib1 + fib2
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2
    offset = -1
    while fib > 1:
        i = min(offset + fib2, n - 1)
        if data[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif data[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i
    if fib1 and offset + 1 < n and data[offset + 1] == target:
        return offset + 1
    return -1
'''


SEARCH_10_SOURCE = '''\
"""Optimal solution for search_10: Sublist Search.

Find the first index where ``sub`` appears in ``data`` as a
contiguous run, or -1 if it never does. Sliding window: align
``data[i..i+m-1]`` with ``sub`` for every i in [0..n-m].
O(n * m) worst case.
"""


def solve(data, sub, n, m):
    if m == 0:
        return 0
    if m > n:
        return -1
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if data[i + j] != sub[j]:
                match = False
                break
        if match:
            return i
    return -1
'''


SEARCH_11_SOURCE = '''\
"""Optimal solution for search_11: Count Occurrences (Sorted).

Sorted array; count how many times ``target`` appears. Two
binary searches: one for the first occurrence, one for the
last. Difference + 1 = count (or 0 if target is missing).
O(log n) time.
"""


def solve(data, target, n):
    if n == 0:
        return 0

    def lower_bound(lo, hi, t):
        while lo < hi:
            mid = (lo + hi) // 2
            if data[mid] < t:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def upper_bound(lo, hi, t):
        while lo < hi:
            mid = (lo + hi) // 2
            if data[mid] <= t:
                lo = mid + 1
            else:
                hi = mid
        return lo

    first = lower_bound(0, n, target)
    if first == n or data[first] != target:
        return 0
    last = upper_bound(first, n, target)
    return last - first
'''


SEARCH_12_SOURCE = '''\
"""Optimal solution for search_12: Search in Rotated Sorted Array.

A sorted array that has been rotated at some unknown pivot.
Find the index of ``target`` (or -1) in O(log n) time.

Two-step: find the pivot (smallest element), then binary-search
the half that could contain the target.
"""


def solve(data, target, n):
    if n == 0:
        return -1
    low, high = 0, n - 1
    # Find the rotation pivot: the smallest element.
    while low < high:
        mid = (low + high) // 2
        if data[mid] > data[high]:
            low = mid + 1
        else:
            high = mid
    pivot = low
    # Decide which half to search.
    if pivot == 0:
        low, high = 0, n - 1
    elif data[0] <= target <= data[pivot - 1]:
        # Target is in the upper half (data[0..pivot-1]).
        low, high = 0, pivot - 1
    else:
        # Target is in the lower half (data[pivot..n-1]).
        low, high = pivot, n - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
'''


# --- 2D BFS / DFS sources. ---


SEARCH_03_SOURCE = '''\
"""Optimal solution for search_03: BFS on a 2D grid.

Find the shortest path from START to GOAL by exploring the grid
level by level with a FIFO queue. O(n^2) for an n x n grid
since every cell is visited at most once.

The engine no longer ships a TrackedQueue AND the user
chose not to use ``collections.deque`` - the player
brings their own queue from basic Python (a plain list
with ``pop(0)``).
"""


def solve(grid, start, goal, size):
    frontier = []
    frontier.append((start[0], start[1], 0))
    visited = set()
    while frontier:
        row, col, distance = frontier.pop(0)
        if (row, col) in visited:
            continue
        visited.add((row, col))
        if (row, col) == goal:
            return distance
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < size and 0 <= nc < size and (nr, nc) not in visited:
                if grid[nr][nc] == 0:
                    frontier.append((nr, nc, distance + 1))
    return -1
'''

SEARCH_04_SOURCE = '''\
"""Optimal solution for search_04: DFS on a 2D grid.

Explore reachable cells depth-first using a LIFO stack.
O(n^2) for an n x n grid.

The engine no longer ships a TrackedStack - the player
brings their own (a plain list with .append() / .pop()
gives the standard LIFO semantics).
"""


def solve(grid, start, size):
    visited = set()
    stack = [start]
    while stack:
        row, col = stack.pop()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < size and 0 <= nc < size and (nr, nc) not in visited and grid[nr][nc] == 0:
                stack.append((nr, nc))
    return len(visited)
'''


# --- 2D setup/verify. ---


def _setup_bfs(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    size = max(5, n)
    challenge._n = size
    challenge._start = (0, 0)
    challenge._goal = (size - 1, size - 1)

    _bind_2d_helpers(challenge)
    challenge._grid_data, challenge._expected_length = _generate_difficult_maze(
        challenge, size, rng, challenge._goal,
    )

    challenge.grid = Grid(size, size)
    for gy in range(size):
        for gx in range(size):
            if challenge._grid_data[gy][gx] == 1:
                challenge.grid.set(gx, gy, CellType.WALL)
            else:
                challenge.grid.set(gx, gy, CellType.EMPTY)
    challenge.grid.set(0, 0, CellType.START, "S")
    challenge.grid.set(size - 1, size - 1, CellType.GOAL, "G")

    grid = TrackedGrid(size, size)
    for gy in range(size):
        for gx in range(size):
            grid._data[gy][gx] = challenge._grid_data[gy][gx]

    return {
        "grid": grid,
        "start": challenge._start,
        "goal": challenge._goal,
        "size": size,
    }


def _verify_bfs(challenge, result: Any) -> bool:
    return result == challenge._expected_length and get_counter().stats.reads > 0


def _setup_dfs(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    size = max(5, n)
    challenge._n = size
    challenge._grid_data = [
        [1 if rng.random() < 0.25 else 0 for _ in range(size)]
        for _ in range(size)
    ]
    challenge._grid_data[0][0] = 0
    challenge._expected_count = _dfs_count(challenge._grid_data, size, (0, 0))

    challenge.grid = Grid(size, size)
    for gy in range(size):
        for gx in range(size):
            if challenge._grid_data[gy][gx] == 1:
                challenge.grid.set(gx, gy, CellType.WALL)
            else:
                challenge.grid.set(gx, gy, CellType.EMPTY)
    challenge.grid.set(0, 0, CellType.START, "S")

    grid = TrackedGrid(size, size)
    for gy in range(size):
        for gx in range(size):
            grid._data[gy][gx] = challenge._grid_data[gy][gx]

    return {"grid": grid, "start": (0, 0), "size": size}


def _verify_dfs(challenge, result: Any) -> bool:
    return result == challenge._expected_count and get_counter().stats.reads > 0


def _dfs_count(grid_data: list[list[int]], size: int, start: tuple[int, int]) -> int:
    visited: set[tuple[int, int]] = set()
    stack: list[tuple[int, int]] = [start]
    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size and (nx, ny) not in visited and grid_data[ny][nx] == 0:
                stack.append((nx, ny))
    return len(visited)


# --- Spec factory. ---


def _flat_search_spec(
    *,
    spec_id: str,
    name: str,
    difficulty: int,
    required_complexity: ComplexityClass,
    description: str,
    source_url: str,
    source: str,
    hint: str,
    sorted_data: bool,
    samples: list[Sample],
    parents: list[str],
    children: list[str],
) -> AlgorithmSpec:
    params: list[str]
    inputs: dict[str, str]
    if sorted_data:
        params = ["data", "target", "n"]
        inputs = {
            "data": "sorted list-like of n random integers.",
            "target": "value to find in data.",
            "n": "length of data.",
        }
    else:
        params = ["data", "target"]
        inputs = {
            "data": "list-like of n random integers.",
            "target": "value to find in data.",
        }
    return AlgorithmSpec(
        id=spec_id,
        name=name,
        category="searching",
        difficulty=difficulty,
        required_complexity=required_complexity,
        description=description,
        source_url=source_url,
        params=params,
        inputs=inputs,
        returns="the index of target in data, or -1 if not found.",
        source=source,
        setup_fn=lambda challenge, n, seed, _sd=sorted_data: _setup_flat_search(challenge, n, seed, sorted_data=_sd),
        verify_fn=_verify_flat_search,
        samples=samples,
        hint=hint,
        parents=parents,
        children=children,
    )


# --- search_10 Sublist Search helpers. ---


def _setup_sublist(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(1, n)
    data = [rng.randint(1, 9) for _ in range(n)]
    # Pick a sublist that's guaranteed to appear in data: copy a
    # contiguous window from data itself.
    m = min(rng.randint(1, max(1, n)), n)
    start = rng.randint(0, n - m)
    sub = list(data[start:start + m])
    challenge._data = data
    challenge._sub = sub
    challenge._m = m
    return {
        "data": TrackedList(data),
        "sub": TrackedList(sub),
        "n": n,
        "m": m,
    }


def _verify_sublist(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    if result == -1:
        return not any(
            challenge._data[i:i + challenge._m] == challenge._sub
            for i in range(len(challenge._data) - challenge._m + 1)
        )
    if result < 0 or result + challenge._m > len(challenge._data):
        return False
    return challenge._data[result:result + challenge._m] == challenge._sub


# --- search_11 Count Occurrences helpers. ---


def _setup_count_occurrences(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    if n <= 0:
        data, target = [], 0
    else:
        # Sorted array with some duplicates.
        data = sorted(rng.sample(range(1, max(2, n) * 3), n))
        target = data[rng.randint(0, n - 1)]
    challenge._data = data
    challenge._target = target
    return {
        "data": TrackedList(data),
        "target": target,
        "n": n,
    }


def _verify_count_occurrences(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    return result == challenge._data.count(challenge._target)


SPECS: list[AlgorithmSpec] = [
    _flat_search_spec(
        spec_id="search_01",
        name="Linear Search",
        difficulty=1,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Find the index of the target value in the array.\n"
            "The array is NOT sorted.\n"
            "Return the index, or -1 if not found.\n"
            "Requirement: O(n)\n"
            "Source: https://www.geeksforgeeks.org/linear-search/"
        ),
        source_url="https://www.geeksforgeeks.org/linear-search/",
        source=SEARCH_01_SOURCE,
        hint="Check each element one by one until you find it.",
        sorted_data=False,
        samples=[
            Sample("data = [8, 3, 5], target = 3", "1"),
            Sample("data = [4, 6, 9], target = 7", "-1"),
            Sample("data = [2, 2, 5], target = 2", "0 or 1"),
        ],
        parents=["intro_01"],
        children=["search_02"],
    ),
    _flat_search_spec(
        spec_id="search_02",
        name="Binary Search",
        difficulty=3,
        required_complexity=ComplexityClass.O_LOG_N,
        description=(
            "Find the index of the target value in a SORTED array.\n"
            "The array is sorted in ascending order.\n"
            "Return the index, or -1 if not found.\n"
            "Requirement: O(log n) - linear search will FAIL!\n"
            "Source: https://www.geeksforgeeks.org/binary-search/"
        ),
        source_url="https://www.geeksforgeeks.org/binary-search/",
        source=SEARCH_02_SOURCE,
        hint="Check the middle element. If target is smaller, search left half; if larger, search right half.",
        sorted_data=True,
        samples=[
            Sample("data = [2, 4, 7, 9], target = 7", "2"),
            Sample("data = [1, 5, 8, 12], target = 3", "-1"),
            Sample("data = [10, 20, 30], target = 10", "0"),
        ],
        parents=["search_01"],
        children=["search_03", "search_04"],
    ),
    AlgorithmSpec(
        id="search_03",
        name="BFS Grid",
        category="searching",
        difficulty=5,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Find the shortest path from START to GOAL in a 2D grid.\n"
            "0 = walkable, 1 = wall. Move in 4 directions (up/down/left/right).\n"
            "The generated maze always has a route, but dense walls make guessing impossible.\n"
            "Use Python row/column indexing: grid[row][column].\n"
            "Rows go down the screen; columns go left to right.\n"
            "Return the shortest path length in steps.\n"
            "Requirement: O(n^2) where n = grid side length.\n"
            "Source: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/"
        ),
        source_url="https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/",
        params=["grid", "start", "goal", "size"],
        inputs={
            "grid": "2D list-like. 0 = walkable, 1 = wall. Read with grid[row][column].",
            "start": "(row, column) start position.",
            "goal": "(row, column) goal position.",
            "size": "width and height of the square grid.",
        },
        returns="the length of the shortest path from start to goal in steps. The challenge always has a path.",
        source=SEARCH_03_SOURCE,
        setup_fn=_setup_bfs,
        verify_fn=_verify_bfs,
        samples=[
            Sample("grid = [[0, 0, 0]], start = (0, 0), goal = (0, 2)", "2"),
            Sample("grid = [[0, 0]], start = (0, 0), goal = (0, 1)", "1"),
            Sample("grid = [[0, 1, 0], [0, 0, 0], [1, 1, 0]], start = (0, 0), goal = (0, 2)", "4"),
        ],
        max_n=35,  # MAX_2D_N
        hint="Use a queue. Start from START, explore all neighbors level by level.",
        parents=["search_02"],
        children=["search_05"],
        # The BFS used to require queue.enqueue / queue.dequeue
        # (the TrackedQueue ops), but TrackedQueue was removed
        # from the engine. The fingerprint for BFS is now
        # implicit: BFS visits every reachable cell exactly once
        # (the O(n^2) grid-read budget is the real gate). We
        # drop the queue-op fingerprint here.
    ),
    AlgorithmSpec(
        id="search_04",
        name="DFS Grid",
        category="searching",
        difficulty=4,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Count all reachable cells from the top-left corner.\n"
            "0 = walkable, 1 = wall. Move in 4 directions.\n"
            "Use Python row/column indexing: grid[row][column].\n"
            "Rows go down the screen; columns go left to right.\n"
            "Return the total number of reachable cells (including start).\n"
            "Requirement: O(n^2) where n = grid side length.\n"
            "Source: https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/"
        ),
        source_url="https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/",
        params=["grid", "start", "size"],
        inputs={
            "grid": "2D list-like. 0 = walkable, 1 = wall. Read with grid[row][column].",
            "start": "(row, column) start position.",
            "size": "width and height of the square grid.",
        },
        returns="the number of walkable cells reachable from start (including start).",
        source=SEARCH_04_SOURCE,
        setup_fn=_setup_dfs,
        verify_fn=_verify_dfs,
        samples=[
            Sample("grid = [[0, 0], [0, 0]], start = (0, 0)", "4"),
            Sample("grid = [[0, 1], [1, 0]], start = (0, 0)", "1"),
            Sample("grid = [[0, 0, 1]], start = (0, 0)", "2"),
        ],
        max_n=35,  # MAX_2D_N
        hint="Use a stack (or recursion). Mark cells as visited and explore neighbors.",
        parents=["search_02"],
        children=["search_05"],
        # DFS used to forbid queue ops and require stack.push.
        # TrackedQueue / TrackedStack are gone from the engine,
        # so the queue-forbid constraints are meaningless. The
        # DFS fingerprint was always weak (it can't tell DFS
        # from BFS that uses a deque) - we drop it entirely.
    ),
    _flat_search_spec(
        spec_id="search_05",
        name="Ternary Search",
        difficulty=3,
        required_complexity=ComplexityClass.O_LOG_N,
        description=(
            "Like binary search, but split the sorted range into three equal parts "
            "at each step. Two comparisons, three possible next ranges.\n"
            "Requirement: O(log_3 n) time.\n"
            "Source: https://www.geeksforgeeks.org/ternary-search/"
        ),
        source_url="https://www.geeksforgeeks.org/ternary-search/",
        source=SEARCH_05_SOURCE,
        hint="Compute two midpoints at low + (high-low)/3 and high - (high-low)/3.",
        sorted_data=True,
        samples=[
            Sample("data = [1, 3, 5, 7, 9, 11, 13], target = 7", "3"),
            Sample("data = [1, 3, 5, 7, 9, 11, 13], target = 4", "-1"),
            Sample("data = [1, 3, 5, 7], target = 1", "0"),
        ],
        parents=["search_03", "search_04"],
        children=["search_06"],
    ),
    _flat_search_spec(
        spec_id="search_06",
        name="Jump Search",
        difficulty=3,
        required_complexity=ComplexityClass.O_LOG_N,
        description=(
            "Sorted array; jump ahead by a fixed block size m = sqrt(n) until "
            "the block could contain the target, then linear-scan inside it.\n"
            "O(sqrt(n)) time, O(1) extra space. Useful when 'jump back' is "
            "expensive (e.g. rotating media).\n"
            "Source: https://www.geeksforgeeks.org/jump-search/"
        ),
        source_url="https://www.geeksforgeeks.org/jump-search/",
        source=SEARCH_06_SOURCE,
        hint="Use step = sqrt(n). Jump forward until you overshoot, then linear-scan the last block.",
        sorted_data=True,
        samples=[
            Sample("data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], target = 7", "7"),
            Sample("data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], target = 10", "-1"),
            Sample("data = [5, 10, 15, 20, 25], target = 20", "3"),
        ],
        parents=["search_05"],
        children=["search_07"],
    ),
    _flat_search_spec(
        spec_id="search_07",
        name="Exponential Search",
        difficulty=4,
        required_complexity=ComplexityClass.O_LOG_N,
        description=(
            "For unbounded / infinite sorted arrays: double the index until the "
            "upper bound is past the target, then binary-search inside it. O(log n) "
            "time, no need to know n up front.\n"
            "Source: https://www.geeksforgeeks.org/exponential-search/"
        ),
        source_url="https://www.geeksforgeeks.org/exponential-search/",
        source=SEARCH_07_SOURCE,
        hint="Find the smallest bound where data[bound] > target, then binary-search [bound/2, bound].",
        sorted_data=True,
        samples=[
            Sample("data = [2, 4, 6, 8, 10, 12, 14], target = 10", "4"),
            Sample("data = [2, 4, 6, 8, 10, 12, 14], target = 1", "-1"),
            Sample("data = [2, 4, 6, 8, 10, 12, 14], target = 14", "6"),
        ],
        parents=["search_06"],
        children=["search_08"],
    ),
    _flat_search_spec(
        spec_id="search_08",
        name="Interpolation Search",
        difficulty=5,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Like binary search, but the probe position is estimated from the "
            "target's value, not the midpoint. O(log log n) average on uniformly "
            "distributed data; degenerates to O(n) on pathological inputs.\n"
            "Source: https://www.geeksforgeeks.org/interpolation-search/"
        ),
        source_url="https://www.geeksforgeeks.org/interpolation-search/",
        source=SEARCH_08_SOURCE,
        hint="pos = low + (target - data[low]) * (high - low) / (data[high] - data[low]).",
        sorted_data=True,
        samples=[
            Sample("data = [10, 20, 30, 40, 50], target = 30", "2"),
            Sample("data = [10, 20, 30, 40, 50], target = 35", "-1"),
            Sample("data = [10, 20, 30, 40, 50], target = 10", "0"),
        ],
        parents=["search_07"],
        children=["search_09"],
    ),
    _flat_search_spec(
        spec_id="search_09",
        name="Fibonacci Search",
        difficulty=4,
        required_complexity=ComplexityClass.O_LOG_N,
        description=(
            "Sorted array; uses Fibonacci numbers to split the range. Always\n"
            "shrinks by at least one Fibonacci number, so the loop runs in\n"
            "O(log n) time. The split is by index, not value, so the only\n"
            "operation is the standard '<=' comparison.\n"
            "Source: https://www.geeksforgeeks.org/fibonacci-search/"
        ),
        source_url="https://www.geeksforgeeks.org/fibonacci-search/",
        source=SEARCH_09_SOURCE,
        hint="Use Fibonacci numbers Fib(m-2)/Fib(m) of the range as the split point.",
        sorted_data=True,
        samples=[
            Sample("data = [1, 4, 7, 9, 12, 15, 18, 22, 25, 30], target = 22", "7"),
            Sample("data = [1, 4, 7, 9, 12, 15, 18, 22, 25, 30], target = 13", "-1"),
            Sample("data = [1, 4, 7, 9, 12, 15, 18, 22, 25, 30], target = 1", "0"),
        ],
        parents=["search_08"],
        children=[],
    ),
    AlgorithmSpec(
        id="search_10",
        name="Sublist Search",
        category="searching",
        difficulty=3,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Find the first index where ``sub`` appears as a contiguous run\n"
            "in ``data``, or -1 if it never does. Sliding window of length m\n"
            "scanned across an n-length list.\n"
            "Source: https://www.geeksforgeeks.org/search-an-element-in-a-list/"
        ),
        source_url="https://www.geeksforgeeks.org/search-an-element-in-a-list/",
        params=["data", "sub", "n", "m"],
        inputs={
            "data": "list-like of n random integers.",
            "sub": "list-like of m integers to find inside data.",
            "n": "length of data.",
            "m": "length of sub (m <= n).",
        },
        returns="the first index i where data[i:i+m] == sub, or -1 if not present.",
        source=SEARCH_10_SOURCE,
        setup_fn=_setup_sublist,
        verify_fn=_verify_sublist,
        samples=[
            Sample("data = [1, 2, 3, 4, 5, 6], sub = [3, 4, 5], n = 6, m = 3", "2"),
            Sample("data = [1, 2, 3, 4, 5], sub = [4, 5, 6], n = 5, m = 3", "-1"),
            Sample("data = [1, 2, 3], sub = [1, 2, 3], n = 3, m = 3", "0"),
        ],
        hint="Slide a window of length m across data. Compare element by element.",
        parents=["search_01"],
        children=["search_11"],
    ),
    AlgorithmSpec(
        id="search_11",
        name="Count Occurrences (Sorted)",
        category="searching",
        difficulty=3,
        required_complexity=ComplexityClass.O_LOG_N,
        description=(
            "Count how many times ``target`` appears in a sorted array.\n"
            "Two binary searches (first and last occurrence) give the count\n"
            "in O(log n) time, no scan of duplicates needed.\n"
            "Source: https://www.geeksforgeeks.org/count-number-of-occurrences-in-a-sorted-array/"
        ),
        source_url="https://www.geeksforgeeks.org/count-number-of-occurrences-in-a-sorted-array/",
        params=["data", "target", "n"],
        inputs={
            "data": "sorted list-like of n random integers (with duplicates possible).",
            "target": "value to count.",
            "n": "length of data.",
        },
        returns="the number of times target appears in data.",
        source=SEARCH_11_SOURCE,
        setup_fn=_setup_count_occurrences,
        verify_fn=_verify_count_occurrences,
        samples=[
            Sample("data = [1, 2, 2, 2, 3, 4, 5], target = 2, n = 7", "3"),
            Sample("data = [1, 2, 3, 4, 5], target = 6, n = 5", "0"),
            Sample("data = [5, 5, 5, 5], target = 5, n = 4", "4"),
        ],
        hint="Find the first occurrence (lower_bound) and one-past-the-last (upper_bound). Difference = count.",
        parents=["search_10"],
        children=["search_12"],
    ),
    _flat_search_spec(
        spec_id="search_12",
        name="Search in Rotated Sorted Array",
        difficulty=5,
        required_complexity=ComplexityClass.O_LOG_N,
        description=(
            "A sorted array that has been rotated at some unknown pivot.\n"
            "Find the index of ``target`` (or -1) in O(log n) time. First\n"
            "find the pivot (the smallest element), then binary-search the\n"
            "half that could contain the target.\n"
            "Source: https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/"
        ),
        source_url="https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/",
        source=SEARCH_12_SOURCE,
        hint="Find the rotation pivot first, then binary-search the half that could contain the target.",
        sorted_data="rotated",
        samples=[
            Sample("data = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4], target = 6", "1"),
            Sample("data = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4], target = 3", "8"),
            Sample("data = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4], target = 30", "-1"),
        ],
        parents=["search_11"],
        children=[],
    ),
]
