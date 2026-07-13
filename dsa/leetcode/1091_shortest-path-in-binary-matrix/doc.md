# Shortest Path in Binary Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1091 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [shortest-path-in-binary-matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/shortest-path-in-binary-matrix/).

### Goal
In a square binary grid, find the length of the shortest clear path from the top-left cell to the bottom-right cell. A path may move in any of the eight neighboring directions, and it may only step on cells containing `0`.

### Function Contract
**Inputs**

- `grid`: an `n x n` matrix of `0` and `1` values.

**Return value**

The number of cells in the shortest valid path, or `-1` if no path exists.

### Examples
**Example 1**

- Input: `grid = [[0,1],[1,0]]`
- Output: `2`

**Example 2**

- Input: `grid = [[0,0,0],[1,1,0],[1,1,0]]`
- Output: `4`

**Example 3**

- Input: `grid = [[1,0,0],[1,1,0],[1,1,0]]`
- Output: `-1`

---

## Solution
### Approach
Breadth-first search on an unweighted grid graph.

### Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n^2)` for the BFS queue in the worst case.

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1091: Shortest Path in Binary Matrix."""

from collections import deque


def solve(grid: list[list[int]]) -> int:
    n = len(grid)
    if grid[0][0] or grid[-1][-1]:
        return -1
    queue: deque[tuple[int, int, int]] = deque([(0, 0, 1)])
    grid[0][0] = 1
    while queue:
        r, c, dist = queue.popleft()
        if r == n - 1 and c == n - 1:
            return dist
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    queue.append((nr, nc, dist + 1))
    return -1
```
</details>
