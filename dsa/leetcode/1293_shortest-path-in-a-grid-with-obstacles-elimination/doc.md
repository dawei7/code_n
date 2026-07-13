# Shortest Path in a Grid with Obstacles Elimination

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1293 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [shortest-path-in-a-grid-with-obstacles-elimination](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/).

### Goal
Move from the top-left to the bottom-right of a grid in the fewest steps. You may pass through at most `k` obstacle cells by eliminating them.

### Function Contract
**Inputs**

- `grid`: binary matrix where `1` is an obstacle.
- `k`: maximum number of obstacles that may be removed.

**Return value**

The shortest path length, or `-1` if the target cannot be reached.

### Examples
**Example 1**

- Input: `grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]`, `k = 1`
- Output: `6`

**Example 2**

- Input: `grid = [[0,1,1],[1,1,1],[1,0,0]]`, `k = 1`
- Output: `-1`

**Example 3**

- Input: `grid = [[0,1],[0,0]]`, `k = 0`
- Output: `2`

---

## Solution
### Approach
Breadth-first search with remaining-resource state.

### Complexity Analysis
- **Time Complexity**: `O(m * n * (k + 1))`
- **Space Complexity**: `O(m * n * (k + 1))`

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import deque


def solve(grid, k):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    if rows == 1 and cols == 1:
        return 0
    if k >= rows + cols - 3:
        return rows + cols - 2

    queue = deque([(0, 0, k, 0)])
    best_remaining = {(0, 0): k}
    while queue:
        r, c, remaining, steps = queue.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            next_remaining = remaining - grid[nr][nc]
            if next_remaining < 0:
                continue
            if nr == rows - 1 and nc == cols - 1:
                return steps + 1
            if best_remaining.get((nr, nc), -1) >= next_remaining:
                continue
            best_remaining[(nr, nc)] = next_remaining
            queue.append((nr, nc, next_remaining, steps + 1))
    return -1
```
</details>
