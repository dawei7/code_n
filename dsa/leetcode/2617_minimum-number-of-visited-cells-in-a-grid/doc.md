# Minimum Number of Visited Cells in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2617 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Stack, Breadth-First Search, Union-Find, Heap (Priority Queue), Matrix, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-number-of-visited-cells-in-a-grid](https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/).

### Goal
Given an $m \times n$ grid where each cell contains a non-negative integer representing the maximum jump distance allowed from that cell, determine the minimum number of steps required to travel from the top-left corner $(0, 0)$ to the bottom-right corner $(m-1, n-1)$. From any cell $(r, c)$ with value $v$, you can move to any cell $(r, c+k)$ or $(r+k, c)$ where $1 \le k \le v$, provided the destination is within grid boundaries. If the destination is unreachable, return -1.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers (`List[List[int]]`) representing the jump capacity of each cell.

**Return value**

- `int`: The minimum number of moves to reach the target, or -1 if it is impossible.

### Examples
**Example 1**

- Input: `grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]`
- Output: `3`

**Example 2**

- Input: `grid = [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]`
- Output: `3`

**Example 3**

- Input: `grid = [[2,1,0],[1,0,0]]`
- Output: `-1`

---

## Solution
### Approach
The problem is solved using Dynamic Programming optimized with Monotonic Priority Queues (or Segment Trees). Since a naive DP approach would be $O(m \cdot n \cdot \max(m, n))$, we optimize the transition by maintaining the minimum steps seen so far for each row and column using min-heaps. This allows us to query the minimum value in a range efficiently, reducing the complexity to $O(m \cdot n \cdot \log(m \cdot n))$.

### Complexity Analysis
- **Time Complexity**: $O(m \cdot n \cdot \log(m \cdot n))$, where $m$ is the number of rows and $n$ is the number of columns. Each cell is pushed and popped from the row and column heaps at most once.
- **Space Complexity**: $O(m \cdot n)$ to store the DP table and the heaps for each row and column.

### Reference Implementations
<details>
<summary>python</summary>

```python
import heapq

def solve(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    # dp[r][c] stores the min steps to reach (r, c)
    dp = [[float('inf')] * n for _ in range(m)]
    dp[0][0] = 1

    # row_heaps[r] stores (steps, col_index) for row r
    # col_heaps[c] stores (steps, row_index) for col c
    row_heaps = [[] for _ in range(m)]
    col_heaps = [[] for _ in range(n)]

    def push(r, c, val):
        heapq.heappush(row_heaps[r], (val, c))
        heapq.heappush(col_heaps[c], (val, r))

    push(0, 0, 1)

    for r in range(m):
        for c in range(n):
            if r == 0 and c == 0:
                continue

            while row_heaps[r] and row_heaps[r][0][1] + grid[r][row_heaps[r][0][1]] < c:
                heapq.heappop(row_heaps[r])

            while col_heaps[c] and col_heaps[c][0][1] + grid[col_heaps[c][0][1]][c] < r:
                heapq.heappop(col_heaps[c])

            res = float('inf')
            if row_heaps[r]:
                res = min(res, row_heaps[r][0][0] + 1)
            if col_heaps[c]:
                res = min(res, col_heaps[c][0][0] + 1)

            dp[r][c] = res
            if res != float('inf'):
                push(r, c, res)

    return dp[m-1][n-1] if dp[m-1][n-1] != float('inf') else -1
```
</details>
