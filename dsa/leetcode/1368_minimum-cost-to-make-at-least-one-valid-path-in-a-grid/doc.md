# Minimum Cost to Make at Least One Valid Path in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1368 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-cost-to-make-at-least-one-valid-path-in-a-grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/).

### Goal
Each grid cell points in one of four directions. Moving in the indicated direction costs `0`; changing direction for a move costs `1`. Find the minimum total cost needed so there is at least one valid path from the top-left cell to the bottom-right cell.

### Function Contract
**Inputs**

- `grid`: an `m x n` matrix whose values encode directions: right, left, down, and up.

**Return value**

The minimum number of direction changes needed to make a path reach the destination.

### Examples
**Example 1**

- Input: `grid = [[1,1,3],[3,2,2],[1,1,4]]`
- Output: `0`

**Example 2**

- Input: `grid = [[1,1,1],[2,2,2],[1,1,1]]`
- Output: `1`

**Example 3**

- Input: `grid = [[4]]`
- Output: `0`

---

## Solution
### Approach
0-1 BFS on the grid graph. Edges that follow the cell arrow have weight `0`; the other three outgoing directions have weight `1`, so a deque-based shortest path search gives the minimum change count.

### Complexity Analysis
- **Time Complexity**: `O(mn)`
- **Space Complexity**: `O(mn)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1368: Minimum Cost to Make at Least One Valid Path in a Grid."""

from collections import deque


def solve(grid: list[list[int]]) -> int:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    rows, cols = len(grid), len(grid[0])
    dist = [[10**9] * cols for _ in range(rows)]
    dist[0][0] = 0
    queue: deque[tuple[int, int]] = deque([(0, 0)])

    while queue:
        r, c = queue.popleft()
        for index, (dr, dc) in enumerate(directions, start=1):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                cost = 0 if grid[r][c] == index else 1
                new_dist = dist[r][c] + cost
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    if cost == 0:
                        queue.appendleft((nr, nc))
                    else:
                        queue.append((nr, nc))
    return dist[-1][-1]
```
</details>
