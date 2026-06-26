# N-Queens II

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_137` |
| Frontend ID | 52 |
| Difficulty | Hard |
| Topics | Backtracking |
| Official Link | [n-queens-ii](https://leetcode.com/problems/n-queens-ii/) |

## Problem Description & Examples
### Goal
Count how many ways `n` queens can be placed on an `n x n` chessboard so that no queen shares a row, column, or diagonal with another queen.

### Function Contract
**Inputs**

- `n`: int board size

**Return value**

int - number of valid queen placements

### Examples
**Example 1**

- Input: `n = 1`
- Output: `1`

**Example 2**

- Input: `n = 4`
- Output: `2`

**Example 3**

- Input: `n = 5`
- Output: `10`

---

## Underlying Base Algorithm(s)
Backtracking with occupied column and diagonal sets.

---

## Complexity Analysis
- **Time Complexity**: `O(n!)`
- **Space Complexity**: `O(n)`
