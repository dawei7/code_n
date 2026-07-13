# Maximum Number of Points From Grid Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2503 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Two Pointers, Breadth-First Search, Union-Find, Sorting, Heap (Priority Queue), Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-number-of-points-from-grid-queries](https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/).

### Goal
Given an $m \times n$ grid of integers and a list of queries, determine for each query $k$ the maximum number of cells you can visit starting from the top-left cell $(0, 0)$. You can only move to adjacent cells (up, down, left, right) if the value in the target cell is strictly less than $k$.

### Function Contract
**Inputs**

- `grid`: A 2D list of integers representing the grid values.
- `queries`: A list of integers representing the threshold values for each query.

**Return value**

- A list of integers where the $i$-th element is the count of reachable cells for the $i$-th query.

### Examples
**Example 1**

- Input: `grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]`
- Output: `[5,8,1]`

**Example 2**

- Input: `grid = [[5,2,1],[1,1,2]], queries = [3]`
- Output: `[0]`

**Example 3**

- Input: `grid = [[1,2],[2,1]], queries = [1,2,3]`
- Output: `[0,1,4]`

---

## Solution
### Approach
The problem is solved using a **Min-Priority Queue (Dijkstra-like approach)** combined with **Offline Query Processing**. By sorting the queries, we can process them in increasing order. We maintain a priority queue of reachable boundary cells, always expanding into the smallest available neighbor. This allows us to incrementally count reachable cells as the threshold $k$ increases.

### Complexity Analysis
- **Time Complexity**: $O(MN \log(MN) + Q \log Q)$, where $M \times N$ is the grid size and $Q$ is the number of queries. We visit each cell once and perform heap operations, and we sort the queries.
- **Space Complexity**: $O(MN + Q)$ to store the grid, the priority queue, and the results.

### Reference Implementations
<details>
<summary>python</summary>

```python
import heapq

def solve(grid, queries):
    m, n = len(grid), len(grid[0])

    # Store queries with original indices to return results in correct order
    sorted_queries = sorted((q, i) for i, q in enumerate(queries))
    results = [0] * len(queries)

    # Min-heap stores (value, row, col)
    # We start from (0, 0)
    pq = [(grid[0][0], 0, 0)]
    visited = [[False for _ in range(n)] for _ in range(m)]
    visited[0][0] = True

    count = 0

    for q_val, original_idx in sorted_queries:
        # Expand the frontier while the smallest value in heap is less than q_val
        while pq and pq[0][0] < q_val:
            val, r, c = heapq.heappop(pq)
            count += 1

            # Check 4-directional neighbors
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(pq, (grid[nr][nc], nr, nc))

        results[original_idx] = count

    return results
```
</details>
