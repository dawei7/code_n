# Coloring A Border

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1034 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [coloring-a-border](https://leetcode.com/problems/coloring-a-border/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/coloring-a-border/).

### Goal
Starting from a cell in a grid, find its connected component of equal-colored cells. Recolor only the border cells of that component.

### Function Contract
**Inputs**

- `grid`: List[List[int]]
- `row`: int starting row
- `col`: int starting column
- `color`: int new border color

**Return value**

List[List[int]] - updated grid

### Examples
**Example 1**

- Input: `grid = [[1,1],[1,2]], row = 0, col = 0, color = 3`
- Output: `[[3,3],[3,2]]`

**Example 2**

- Input: `grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3`
- Output: `[[1,3,3],[2,3,3]]`

**Example 3**

- Input: `grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2`
- Output: `[[2,2,2],[2,1,2],[2,2,2]]`

---

## Solution
### Approach
DFS component traversal with border detection.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(m * n)` worst-case visited/recursion space

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1034: Coloring A Border."""


def solve(grid: list[list[int]], row: int, col: int, color: int) -> list[list[int]]:
    rows, cols = len(grid), len(grid[0])
    original = grid[row][col]
    seen: set[tuple[int, int]] = set()
    border: list[tuple[int, int]] = []

    def dfs(r: int, c: int) -> None:
        seen.add((r, c))
        is_border = r in (0, rows - 1) or c in (0, cols - 1)
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != original:
                is_border = True
            elif (nr, nc) not in seen:
                dfs(nr, nc)
        if is_border:
            border.append((r, c))

    dfs(row, col)
    for r, c in border:
        grid[r][c] = color
    return grid
```
</details>
