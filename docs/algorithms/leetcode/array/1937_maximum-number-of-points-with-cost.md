# Maximum Number of Points with Cost

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1937 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [maximum-number-of-points-with-cost](https://leetcode.com/problems/maximum-number-of-points-with-cost/) |

## Problem Description & Examples
### Goal
Choose one cell from each row of a points matrix. Moving from column `a` in one row to column `b` in the next subtracts `abs(a - b)` from the score; maximize the total.

### Function Contract
**Inputs**

- `points`: an `m x n` matrix of non-negative scores.

**Return value**

Return the largest obtainable score.

### Examples
**Example 1**

- Input: `points = [[1,2,3],[1,5,1],[3,1,1]]`
- Output: `9`

**Example 2**

- Input: `points = [[1,5],[2,3],[4,2]]`
- Output: `11`

**Example 3**

- Input: `points = [[7]]`
- Output: `7`

---

## Underlying Base Algorithm(s)
Maintain the best score ending at each column for the previous row. For each new row, do a left-to-right pass tracking `prev[j] + j`, and a right-to-left pass tracking `prev[j] - j`; these give the best transition into each column without trying all pairs.

---

## Complexity Analysis
- **Time Complexity**: `O(mn)`
- **Space Complexity**: `O(n)`
