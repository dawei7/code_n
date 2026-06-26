# Minimum Falling Path Sum II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1289 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [minimum-falling-path-sum-ii](https://leetcode.com/problems/minimum-falling-path-sum-ii/) |

## Problem Description & Examples
### Goal
Choose one cell from each row of a square grid so that no two adjacent rows choose the same column, minimizing the total sum.

### Function Contract
**Inputs**

- `grid`: an `n x n` integer matrix.

**Return value**

The minimum valid falling path sum.

### Examples
**Example 1**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `13`

**Example 2**

- Input: `grid = [[7]]`
- Output: `7`

**Example 3**

- Input: `grid = [[2,2,1],[1,2,2],[2,1,2]]`
- Output: `3`

---

## Underlying Base Algorithm(s)
Dynamic programming with minimum and second minimum tracking.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)`
