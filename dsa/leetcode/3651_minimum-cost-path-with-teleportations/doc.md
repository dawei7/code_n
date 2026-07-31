# Minimum Cost Path with Teleportations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3651 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-path-with-teleportations/) |

## Problem Description
### Goal

Start at the top-left cell of an $m\times n$ integer matrix `grid` and reach its bottom-right cell. A normal move goes one cell right or one cell down and adds the destination cell's value to the total cost. The starting cell itself costs nothing.

You may also teleport at most `k` times. From a current cell `(i, j)`, a teleport may reach any matrix cell `(x, y)` whose value is at most `grid[i][j]`; this move costs zero and is not restricted to moving right or down.

Return the minimum possible total cost of reaching the bottom-right cell using any legal mixture of normal moves and teleportations.

### Function Contract
**Inputs**

- `grid`: An $m\times n$ matrix with $2\le m,n\le80$ and values in $[0,10^4]$.
- `k`: The maximum number of teleportations, with $0\le k\le10$.

**Return value**

Return the minimum accumulated destination-cell cost needed to reach `(m - 1, n - 1)`.

### Examples
**Example 1**

- Input: `grid = [[1,3,3],[2,5,4],[4,3,5]]`, `k = 2`
- Output: `7`
- Explanation: Move down for 2, move right for 5, then teleport from value 5 to the bottom-right value 5 at no additional cost.

**Example 2**

- Input: `grid = [[1,2],[2,3],[3,4]]`, `k = 1`
- Output: `9`
- Explanation: Every later cell on a monotone route has a larger value, so the available teleport cannot improve the normal path cost.
