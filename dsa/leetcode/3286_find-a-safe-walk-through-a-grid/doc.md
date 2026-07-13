# Find a Safe Walk Through a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3286 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-a-safe-walk-through-a-grid](https://leetcode.com/problems/find-a-safe-walk-through-a-grid/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-a-safe-walk-through-a-grid/).

### Goal
Determine if there exists a path from the top-left cell (0, 0) to the bottom-right cell (m-1, n-1) of a grid such that the total sum of the values of the cells visited is strictly less than a given health threshold `health`. Cells containing a `1` reduce your health by 1, while cells containing a `0` do not. You can only move in the four cardinal directions.

### Function Contract
**Inputs**

- `grid`: A 2D list of integers where 0 represents a safe cell and 1 represents a hazardous cell.
- `health`: An integer representing the initial health points.

**Return value**

- A boolean: `True` if a path exists where the total health cost is less than the initial `health`, otherwise `False`.

### Examples
**Example 1**

- Input: `grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1`
- Output: `True`

**Example 2**

- Input: `grid = [[0,1,1],[1,1,1],[1,1,0]], health = 3`
- Output: `False`

**Example 3**

- Input: `grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5`
- Output: `True`

---

## Solution
### Approach
This problem is a shortest-path problem on a weighted graph where edge weights are either 0 or 1. Dijkstra's algorithm or 0-1 Breadth-First Search (using a deque) are optimal. Since we want to minimize the total cost (sum of 1s encountered), 0-1 BFS is preferred for its O(V + E) efficiency.

### Complexity Analysis
- **Time Complexity**: O(m * n), where m is the number of rows and n is the number of columns, as each cell is visited at most once.
- **Space Complexity**: O(m * n) to store the distance matrix and the queue.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import deque

def solve(grid: list[list[int]], health: int) -> bool:
    rows = len(grid)
    cols = len(grid[0])

    # If the starting cell is hazardous, we lose 1 health immediately
    start_cost = grid[0][0]
    if start_cost >= health:
        return False

    # dist[r][c] stores the minimum health cost to reach (r, c)
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = start_cost

    # 0-1 BFS using a deque
    queue = deque([(0, 0)])

    while queue:
        r, c = queue.popleft()

        if r == rows - 1 and c == cols - 1:
            return dist[r][c] < health

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                weight = grid[nr][nc]
                if dist[r][c] + weight < dist[nr][nc]:
                    dist[nr][nc] = dist[r][c] + weight
                    # If weight is 0, add to front; if 1, add to back
                    if weight == 0:
                        queue.appendleft((nr, nc))
                    else:
                        queue.append((nr, nc))

    return dist[rows - 1][cols - 1] < health
```
</details>
