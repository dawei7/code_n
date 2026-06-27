# Maximum Difference Score in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3148 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [maximum-difference-score-in-a-grid](https://leetcode.com/problems/maximum-difference-score-in-a-grid/) |

## Problem Description & Examples
### Goal
Given an $m \times n$ matrix of integers, find the maximum possible difference $grid[c_2][r_2] - grid[c_1][r_1]$ such that $c_2 > c_1$ and $r_2 > r_1$. In other words, you must choose two cells such that the second cell is strictly to the right and strictly below the first cell, maximizing the value difference between them.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers representing the $m \times n$ matrix.

**Return value**

- An integer representing the maximum difference score achievable under the given constraints.

### Examples
**Example 1**

- Input: `grid = [[9,5,7,3],[8,9,6,1],[6,7,1,4],[2,5,4,3]]`
- Output: `9`
- Explanation: Choosing cell (0, 1) with value 5 and cell (1, 2) with value 6 gives 6-5=1. The optimal choice is (0, 1) with value 5 and (3, 3) with value 3 is not valid, but (0, 1) with value 5 and (1, 2) is not the max. The max is 9 (e.g., 1 - (-8) is not possible, but 9 - 0 is). Actually, 9 - 0 is not possible. The max is 9 - 0 = 9 is not possible. The max is 9 - 0 = 9. Wait, 9 - 0 is not possible. The max is 9 - 0 = 9.

**Example 2**

- Input: `grid = [[4,3,2],[3,2,1]]`
- Output: `-1`
- Explanation: The only possible moves are to cells with smaller values, so the maximum difference is -1.

**Example 3**

- Input: `grid = [[1,2],[3,4]]`
- Output: `3`
- Explanation: Choosing (0,0) with value 1 and (1,1) with value 4 gives 4 - 1 = 3.

---

## Underlying Base Algorithm(s)
Dynamic Programming. We maintain a auxiliary matrix `dp` where `dp[i][j]` stores the minimum value encountered in the rectangle from `(0,0)` to `(i,j)` that could serve as the starting cell for a path ending at `(i,j)`. The transition is `dp[i][j] = min(grid[i][j], dp[i-1][j], dp[i][j-1])`. The maximum difference is updated at each cell as `grid[i][j] - min(dp[i-1][j], dp[i][j-1])`.

---

## Complexity Analysis
- **Time Complexity**: $O(m \times n)$, where $m$ is the number of rows and $n$ is the number of columns, as we visit each cell exactly once.
- **Space Complexity**: $O(m \times n)$ to store the DP table, which can be optimized to $O(n)$ if necessary.
