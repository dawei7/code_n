# Find the Safest Path in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2812 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Breadth-First Search, Union-Find, Heap (Priority Queue), Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-safest-path-in-a-grid](https://leetcode.com/problems/find-the-safest-path-in-a-grid/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-safest-path-in-a-grid/).

### Goal
Given an $n \times n$ grid containing some cells occupied by thieves (represented by 1) and others empty (represented by 0), find a path from the top-left corner $(0, 0)$ to the bottom-right corner $(n-1, n-1)$. The "safeness factor" of a path is defined as the minimum Manhattan distance from any cell in the path to the nearest thief. The objective is to maximize this safeness factor across all possible paths.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers (size $n \times n$) where 0 represents an empty cell and 1 represents a thief.

**Return value**

- An integer representing the maximum possible safeness factor for a path from $(0, 0)$ to $(n-1, n-1)$.

### Examples
**Example 1**

- Input: `grid = [[1,0,0],[0,0,0],[0,0,1]]`
- Output: `0`

**Example 2**

- Input: `grid = [[0,0,1],[0,0,0],[0,0,0]]`
- Output: `2`

**Example 3**

- Input: `grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]`
- Output: `2`

---

## Solution
### Approach
1. **Multi-Source Breadth-First Search (BFS)**: Used to calculate the minimum Manhattan distance from every cell to the nearest thief.
2. **Dijkstra's Algorithm (or Max-Heap BFS)**: Used to find the path that maximizes the minimum safeness factor along the route.

### Complexity Analysis
- **Time Complexity**: $O(n^2 \log n)$, where $n$ is the side length of the grid. The multi-source BFS takes $O(n^2)$, and the priority queue-based pathfinding takes $O(n^2 \log n)$.
- **Space Complexity**: $O(n^2)$ to store the distance grid and the priority queue.

### Reference Implementations
<details>
<summary>python</summary>

```python
import heapq
from collections import deque

def solve(grid: list[list[int]]) -> int:
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return 0

    # Multi-source BFS to calculate distance to nearest thief
    dist = [[-1] * n for _ in range(n)]
    queue = deque()

    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                dist[r][c] = 0
                queue.append((r, c))

    while queue:
        r, c = queue.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

    # Dijkstra-like approach to find the path with max-min safeness
    # Max-heap stores (-safeness, r, c)
    pq = [(-dist[0][0], 0, 0)]
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True

    while pq:
        d, r, c = heapq.heappop(pq)
        d = -d

        if r == n - 1 and c == n - 1:
            return d

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                # The safeness of the path is the min of current path and next cell
                new_dist = min(d, dist[nr][nc])
                heapq.heappush(pq, (-new_dist, nr, nc))

    return 0
```
</details>
