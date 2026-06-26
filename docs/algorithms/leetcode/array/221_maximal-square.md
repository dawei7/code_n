# Maximal Square

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 221 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [maximal-square](https://leetcode.com/problems/maximal-square/) |

## Problem Description & Examples
### Goal
Find the area of the largest axis-aligned square containing only `1` cells in a binary matrix.

### Function Contract
**Inputs**

- `matrix`: a rectangular matrix of string or character values `"0"` and `"1"`.

**Return value**

The area of the largest all-ones square.

### Examples
**Example 1**

- Input: `matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]`
- Output: `4`

**Example 2**

- Input: `matrix = [["0", "1"], ["1", "0"]]`
- Output: `1`

**Example 3**

- Input: `matrix = [["0"]]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Let `dp[r][c]` be the side length of the largest all-ones square ending at cell `(r, c)`. A `1` cell extends one beyond the minimum of the values above, left, and diagonally above-left; a `0` cell contributes zero. Track the largest side and square it for the area.

---

## Complexity Analysis
- **Time Complexity**: `O(mn)`
- **Space Complexity**: `O(n)` with a rolling row
