# Count Paths With the Given XOR Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3393 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-paths-with-the-given-xor-value](https://leetcode.com/problems/count-paths-with-the-given-xor-value/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-paths-with-the-given-xor-value/).

### Goal
Given a 2D grid of integers, determine the number of distinct paths from the top-left cell (0, 0) to the bottom-right cell (m-1, n-1). A valid path consists only of moves either right or down, and the XOR sum of all integers encountered along the path must equal a specified target value `k`.

### Function Contract
**Inputs**

- `grid`: A 2D list of integers (List[List[int]]) representing the matrix.
- `k`: An integer representing the target XOR sum.

**Return value**

- An integer representing the total count of paths whose XOR sum equals `k`, modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `grid = [[1,2],[3,4]], k = 1`
- Output: `2`

**Example 2**

- Input: `grid = [[5,2],[1,6]], k = 1`
- Output: `0`

**Example 3**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1`
- Output: `2`

---

## Solution
### Approach
The problem is solved using **Dynamic Programming**. We maintain a 3D state `dp[r][c][current_xor]`, representing the number of ways to reach cell `(r, c)` with a cumulative XOR sum of `current_xor`. Since each cell depends only on the cells above it and to its left, we can iteratively build the solution. Given the constraints on XOR values (typically up to 16 for this problem type), the state space is manageable.

### Complexity Analysis
- **Time Complexity**: O(m * n * K), where m and n are the dimensions of the grid and K is the maximum possible XOR value (typically 16 for this problem).
- **Space Complexity**: O(m * n * K), which can be optimized to O(n * K) using space-optimized DP since we only need the previous row's results.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid: list[list[int]], k: int) -> int:
    MOD = 10**9 + 7
    m = len(grid)
    n = len(grid[0])
    # The maximum XOR value is 16 (2^4) based on problem constraints
    MAX_XOR = 16

    # dp[r][c][xor_val] stores the number of paths to (r, c) with XOR sum xor_val
    dp = [[[0] * MAX_XOR for _ in range(n)] for _ in range(m)]

    # Initialize starting point
    dp[0][0][grid[0][0]] = 1

    for r in range(m):
        for c in range(n):
            for val in range(MAX_XOR):
                if dp[r][c][val] == 0:
                    continue

                # Move Right
                if c + 1 < n:
                    new_xor = val ^ grid[r][c + 1]
                    dp[r][c + 1][new_xor] = (dp[r][c + 1][new_xor] + dp[r][c][val]) % MOD

                # Move Down
                if r + 1 < m:
                    new_xor = val ^ grid[r + 1][c]
                    dp[r + 1][c][new_xor] = (dp[r + 1][c][new_xor] + dp[r][c][val]) % MOD

    return dp[m - 1][n - 1][k]
```
</details>
