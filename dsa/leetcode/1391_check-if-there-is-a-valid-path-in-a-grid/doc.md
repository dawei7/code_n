# Check if There is a Valid Path in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1391 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [check-if-there-is-a-valid-path-in-a-grid](https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/).

### Goal
Each cell contains a street shape connecting two directions. Starting at the top-left cell, decide whether the street connections allow travel to the bottom-right cell without crossing an incompatible edge.

### Function Contract
**Inputs**

- `grid`: an `m x n` matrix of street type ids from `1` to `6`.

**Return value**

`true` if there is a connected valid path from `(0, 0)` to `(m - 1, n - 1)`, otherwise `false`.

### Examples
**Example 1**

- Input: `grid = [[2,4,3],[6,5,2]]`
- Output: `true`

**Example 2**

- Input: `grid = [[1,2,1],[1,2,1]]`
- Output: `false`

**Example 3**

- Input: `grid = [[1,1,2]]`
- Output: `false`

---

## Solution
### Approach
Graph traversal with compatibility checks. Map each street type to its open directions, move only along open exits, and require the neighboring street to have the opposite opening.

### Complexity Analysis
- **Time Complexity**: `O(mn)`
- **Space Complexity**: `O(mn)` for visited state or traversal queue/stack.

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1391: Check if There is a Valid Path in a Grid."""

from collections import deque


def solve(grid: list[list[int]]) -> bool:
    openings = {
        1: [(0, -1), (0, 1)],
        2: [(-1, 0), (1, 0)],
        3: [(0, -1), (1, 0)],
        4: [(0, 1), (1, 0)],
        5: [(0, -1), (-1, 0)],
        6: [(0, 1), (-1, 0)],
    }
    rows, cols = len(grid), len(grid[0])
    queue: deque[tuple[int, int]] = deque([(0, 0)])
    seen = {(0, 0)}

    while queue:
        r, c = queue.popleft()
        if r == rows - 1 and c == cols - 1:
            return True
        for dr, dc in openings[grid[r][c]]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < rows and 0 <= nc < cols) or (nr, nc) in seen:
                continue
            if (-dr, -dc) in openings[grid[nr][nc]]:
                seen.add((nr, nc))
                queue.append((nr, nc))
    return False
```
</details>
