# Paths in Matrix Whose Sum Is Divisible by K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2435 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [paths-in-matrix-whose-sum-is-divisible-by-k](https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/).

### Goal
Given a 2D grid of non-negative integers, determine the total number of distinct paths from the top-left cell (0, 0) to the bottom-right cell (m-1, n-1). A path is valid if and only if the sum of all integers encountered along the path is evenly divisible by a given integer k. Movement is restricted to only moving right or down.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers representing the matrix.
- `k`: An integer divisor.

**Return value**

- An integer representing the count of paths whose sum modulo k equals 0. Since the result can be very large, return it modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3`
- Output: `2`

**Example 2**

- Input: `grid = [[0,0]], k = 5`
- Output: `1`

**Example 3**

- Input: `grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1`
- Output: `10`

---

## Solution
### Approach
The problem is solved using Dynamic Programming. We maintain a 3D DP table `dp[i][j][rem]`, representing the number of paths reaching cell `(i, j)` such that the path sum modulo `k` is `rem`. The state transition is `dp[i][j][(rem + grid[i][j]) % k] = dp[i-1][j][rem] + dp[i][j-1][rem]`.

### Complexity Analysis
- **Time Complexity**: O(m * n * k), where m is the number of rows, n is the number of columns, and k is the divisor. We iterate through every cell and update k states.
- **Space Complexity**: O(m * n * k) to store the DP table. This can be optimized to O(n * k) by observing that we only need the previous row's values.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid: list[list[int]], k: int) -> int:
    MOD = 10**9 + 7
    rows = len(grid)
    cols = len(grid[0])

    # dp[i][j][rem] stores the number of paths to (i, j) with sum % k == rem
    dp = [[[0] * k for _ in range(cols)] for _ in range(rows)]

    # Initialize starting cell
    dp[0][0][grid[0][0] % k] = 1

    for i in range(rows):
        for j in range(cols):
            for rem in range(k):
                if dp[i][j][rem] == 0:
                    continue

                # Move Down
                if i + 1 < rows:
                    new_rem = (rem + grid[i + 1][j]) % k
                    dp[i + 1][j][new_rem] = (dp[i + 1][j][new_rem] + dp[i][j][rem]) % MOD

                # Move Right
                if j + 1 < cols:
                    new_rem = (rem + grid[i][j + 1]) % k
                    dp[i][j + 1][new_rem] = (dp[i][j + 1][new_rem] + dp[i][j][rem]) % MOD

    return dp[rows - 1][cols - 1][0]
```
</details>
