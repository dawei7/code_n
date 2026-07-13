# Number of Enclaves

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1020 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-enclaves](https://leetcode.com/problems/number-of-enclaves/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-enclaves/).

### Goal
Given a binary grid where `1` means land and `0` means water, count land cells that cannot reach the grid boundary by moving up, down, left, or right through land.

### Function Contract
**Inputs**

- `grid`: List[List[int]]

**Return value**

int - number of enclosed land cells

### Examples
**Example 1**

- Input: `grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]`
- Output: `3`

**Example 2**

- Input: `grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]`
- Output: `0`

**Example 3**

- Input: `grid = [[1,1,1],[1,1,1],[1,1,1]]`
- Output: `0`

---

## Solution
### Approach
Boundary flood fill.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(m * n)` worst-case recursion/stack space

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1020: Number of Enclaves."""

from collections import deque


def solve(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue: deque[tuple[int, int]] = deque()

    for r in range(rows):
        for c in (0, cols - 1):
            if grid[r][c] == 1:
                grid[r][c] = 0
                queue.append((r, c))
    for c in range(cols):
        for r in (0, rows - 1):
            if grid[r][c] == 1:
                grid[r][c] = 0
                queue.append((r, c))

    while queue:
        r, c = queue.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 0
                queue.append((nr, nc))

    return sum(sum(row) for row in grid)
```
</details>
