# Equal Sum Grid Partition II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3548 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Matrix, Enumeration, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/equal-sum-grid-partition-ii/) |

## Problem Description

### Goal

You are given an $m \times n$ matrix `grid` of positive integers. Choose either one horizontal cut between consecutive rows or one vertical cut between consecutive columns. The cut must span the complete grid and create two nonempty sections.

The two section sums may already be equal. Otherwise, you may discount the value of at most one cell from exactly one section's sum. When a cell is discounted, all other cells in that section must remain connected through up, down, left, and right moves. The discounted cell is not available as part of those connecting paths.

Return `true` if some legal cut, with zero or one discount, makes the section sums equal. Return `false` when no such choice exists.

### Function Contract

**Inputs**

- `grid`: A rectangular matrix whose entries are positive integers.

Let $m$ and $n$ be the row and column counts. The constraints are $1 \le m,n \le 10^5$, $2 \le mn \le 10^5$, and $1 \le \texttt{grid[i][j]} \le 10^5$.

**Return value**

Return a boolean indicating whether one full horizontal or vertical cut can balance the two nonempty sections, optionally after discounting one connectivity-safe cell.

### Examples

**Example 1**

- Input: `grid = [[1,4],[2,3]]`
- Output: `true`
- Explanation: A horizontal cut gives sums $5$ and $5$, so no discount is needed.

**Example 2**

- Input: `grid = [[1,2],[3,4]]`
- Output: `true`
- Explanation: A vertical cut gives sums $4$ and $6$. Discounting the cell valued `2` from the right section balances the sums, and the remaining cell stays connected.

**Example 3**

- Input: `grid = [[1,2,4],[2,3,5]]`
- Output: `false`
- Explanation: The horizontal sums are $7$ and $10$, but discounting the middle value `3` would split the bottom row into disconnected pieces. No other cut works.

**Example 4**

- Input: `grid = [[4,1,8],[3,2,6]]`
- Output: `false`
- Explanation: No horizontal or vertical cut can be balanced by a legal discount.

---
