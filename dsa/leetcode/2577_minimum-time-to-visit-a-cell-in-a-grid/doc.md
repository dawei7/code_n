# Minimum Time to Visit a Cell In a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2577 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-time-to-visit-a-cell-in-a-grid](https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/).

### Goal
Given a 2D grid of size `m x n` where each cell contains a non-negative integer representing the earliest time you can enter that cell, determine the minimum time required to travel from the top-left corner `(0, 0)` to the bottom-right corner `(m-1, n-1)`. You can move to adjacent cells (up, down, left, right) at each time step, but you can only enter a cell if your current time is greater than or equal to the value stored in that cell. If you arrive at an adjacent cell earlier than its required time, you must "wait" by moving back and forth between the current cell and an adjacent one until the time is sufficient to enter the target cell.

### Function Contract
**Inputs**

- `grid`: A 2D list of integers where `grid[i][j]` is the minimum time required to enter cell `(i, j)`.

**Return value**

- An integer representing the minimum time to reach `(m-1, n-1)`. If it is impossible to reach the destination, return `-1`.

### Examples
**Example 1**

- Input: `grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]`
- Output: `7`

**Example 2**

- Input: `grid = [[0,2,4],[3,2,1],[1,0,4]]`
- Output: `-1`

**Example 3**

- Input: `grid = [[0,1],[1,2]]`
- Output: `2`

---

## Solution
### Approach
The problem is modeled as a shortest-path problem on a weighted graph. Since we need to find the minimum time, **Dijkstra's Algorithm** is the optimal choice. The state is defined by `(time, row, col)`. When moving from a cell, if the current time plus one is less than the target cell's requirement, we calculate the wait time. If the difference between the target requirement and the current time is odd, we can reach the target exactly at the requirement time; if even, we must wait one extra unit to maintain parity.

### Complexity Analysis
- **Time Complexity**: `O(E log V)` where `E` is the number of edges (4 per cell) and `V` is the number of vertices (`m * n`). This simplifies to `O(m * n * log(m * n))`.
- **Space Complexity**: `O(m * n)` to store the `visited` matrix and the priority queue.

### Reference Implementations
<details>
<summary>python</summary>

```python
import heapq

def solve(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])

    # If the first step is impossible, return -1
    if grid[0][1] > 1 and grid[1][0] > 1:
        return -1

    # Priority Queue stores (time, row, col)
    pq = [(0, 0, 0)]
    visited = set([(0, 0)])

    while pq:
        time, r, c = heapq.heappop(pq)

        if r == m - 1 and c == n - 1:
            return time

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                wait = 0
                # If the next cell's requirement is greater than current time + 1
                if grid[nr][nc] > time + 1:
                    diff = grid[nr][nc] - (time + 1)
                    # If diff is odd, we can arrive exactly at grid[nr][nc]
                    # If diff is even, we arrive at grid[nr][nc] + 1
                    wait = diff if diff % 2 == 0 else diff + 1

                new_time = time + 1 + wait
                visited.add((nr, nc))
                heapq.heappush(pq, (new_time, nr, nc))

    return -1
```
</details>
