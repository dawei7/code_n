# Largest Submatrix With Rearrangements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1727 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting, Matrix |
| Official Link | [largest-submatrix-with-rearrangements](https://leetcode.com/problems/largest-submatrix-with-rearrangements/) |

## Problem Description & Examples
### Goal
Columns of a binary matrix may be rearranged independently. Find the largest all-ones submatrix area obtainable after any column ordering.

### Function Contract
**Inputs**

- `matrix`: a binary matrix.

**Return value**

Return the maximum area of a submatrix containing only `1`s after rearranging columns.

### Examples
**Example 1**

- Input: `matrix = [[0,0,1],[1,1,1],[1,0,1]]`
- Output: `4`

**Example 2**

- Input: `matrix = [[1,0,1,0,1]]`
- Output: `3`

**Example 3**

- Input: `matrix = [[1,1,0],[1,0,1]]`
- Output: `2`

---

## Underlying Base Algorithm(s)
For each row, treat it as the bottom of a possible submatrix and compute the vertical height of consecutive ones in every column. Since columns can be rearranged, sort those heights descending; if the `j`th sorted height is `h`, then `h * (j + 1)` is a candidate area.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n log n)`
- **Space Complexity**: `O(n)` besides the matrix if heights are updated in place
