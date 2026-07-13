# Number of Increasing Paths in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2328 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort, Memoization, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-increasing-paths-in-a-grid](https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/).

### Goal
Given an `m x n` integer grid, the task is to find the total number of strictly increasing paths. A path can start from any cell and end at any cell. Each step in a path must move from the current cell to an adjacent cell (up, down, left, or right) such that the value of the destination cell is strictly greater than the value of the current cell. The final count should be returned modulo `10^9 + 7`.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers representing the `m x n` grid. `1 <= m, n <= 1000`, `1 <= m * n <= 10^5`, `1 <= grid[i][j] <= 10^5`.

**Return value**

- An integer representing the total number of strictly increasing paths, modulo `10^9 + 7`.

### Examples
**Example 1**

- Input: `grid = [[1,1],[3,4]]`
- Output: `8`
- Explanation:
    Paths of length 1: `[1]`, `[1]`, `[3]`, `[4]` (4 paths)
    Paths of length 2: `[1->3]`, `[1->4]`, `[3->4]` (3 paths)
    Paths of length 3: `[1->3->4]` (1 path)
    Total paths = 4 + 3 + 1 = 8.

**Example 2**

- Input: `grid = [[1],[2]]`
- Output: `3`
- Explanation:
    Paths of length 1: `[1]`, `[2]` (2 paths)
    Paths of length 2: `[1->2]` (1 path)
    Total paths = 3.

**Additional Example**

- Input: `grid = [[1]]`
- Output: `1`
- Explanation:
    Paths of length 1: `[1]` (from (0,0)) (1 path)
    Total paths = 1.

---

## Solution
### Approach
The problem can be modeled as finding all paths in a Directed Acyclic Graph (DAG). Each cell `(r, c)` in the grid represents a node. A directed edge exists from `(r, c)` to an adjacent cell `(nr, nc)` if `grid[nr][nc] > grid[r][c]`. Since values must strictly increase, no cycles are possible, confirming it's a DAG.

The core idea is to use **Dynamic Programming** or **Memoized Depth-First Search (DFS)**. For each cell `(r, c)`, we want to calculate `dp[r][c]`, which represents the number of strictly increasing paths that *start* at `(r, c)`.

The recurrence relation for `dp[r][c]` is:
`dp[r][c] = 1 + sum(dp[nr][nc])`
where `(nr, nc)` are valid adjacent cells such that `grid[nr][nc] > grid[r][c]`. The `1` accounts for the path consisting only of the cell `(r, c)` itself.

Since paths can start from any cell, the final answer is the sum of `dp[r][c]` for all `(r, c)` in the grid, modulo `10^9 + 7`.

A DFS function with memoization can efficiently compute `dp[r][c]` for each cell. When `dfs(r, c)` is called:
1. If `dp[r][c]` has already been computed, return the stored value.
2. Initialize `count = 1` (for the path `[grid[r][c]]`).
3. For each of the four adjacent cells `(nr, nc)`:
    a. Check if `(nr, nc)` is within grid boundaries.
    b. Check if `grid[nr][nc] > grid[r][c]`.
    c. If both conditions are met, recursively call `dfs(nr, nc)` and add its result to `count`.
4. Store `count` in `dp[r][c]` and return it.

The overall algorithm iterates through every cell in the grid, initiating a DFS from each. The memoization ensures that each `(r, c)` state is computed only once.

### Complexity Analysis
- **Time Complexity**: `O(M * N)`.
    The grid has `M * N` cells. Each cell `(r, c)` serves as a state in our dynamic programming/memoization table. The `dfs` function for each state is called at most once due to memoization. Inside `dfs`, we perform a constant amount of work (checking 4 neighbors and performing additions). Therefore, the total time complexity is proportional to the number of cells in the grid.
- **Space Complexity**: `O(M * N)`.
    This is primarily for the memoization table (or `lru_cache` storage) which stores `dp[r][c]` for all `M * N` cells. In the worst case, the recursion stack depth for DFS could also go up to `M * N` (e.g., a snake-like path through the entire grid), contributing to the space complexity.

### Reference Implementations
<details>
<summary>python</summary>

```python
import sys
from functools import lru_cache

def solve(grid: list[list[int]]) -> int:
    MOD = 10**9 + 7
    m = len(grid)
    n = len(grid[0])

    # Directions for moving up, down, left, right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    @lru_cache(None)
    def dfs(r: int, c: int) -> int:
        # A path consisting only of the current cell is 1 path
        count = 1

        # Explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Check boundary conditions
            if 0 <= nr < m and 0 <= nc < n:
                # Check strictly increasing condition
                if grid[nr][nc] > grid[r][c]:
                    count = (count + dfs(nr, nc)) % MOD

        return count

    total_paths = 0
    # Iterate through each cell and sum up the paths starting from it
    for r in range(m):
        for c in range(n):
            total_paths = (total_paths + dfs(r, c)) % MOD

    return total_paths
```
</details>
