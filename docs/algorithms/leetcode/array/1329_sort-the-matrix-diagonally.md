# Sort the Matrix Diagonally

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1329 |
| Difficulty | Medium |
| Topics | Array, Sorting, Matrix |
| Official Link | [sort-the-matrix-diagonally](https://leetcode.com/problems/sort-the-matrix-diagonally/) |

## Problem Description & Examples
### Goal
Sort every top-left to bottom-right diagonal of a matrix in ascending order while keeping values on their original diagonals.

### Function Contract
**Inputs**

- `mat`: integer matrix.

**Return value**

The matrix after independently sorting each diagonal.

### Examples
**Example 1**

- Input: `mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]`
- Output: `[[1,1,1,1],[1,2,2,2],[1,2,3,3]]`

**Example 2**

- Input: `mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]`
- Output: `[[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]`

**Example 3**

- Input: `mat = [[2,1],[1,2]]`
- Output: `[[2,1],[1,2]]`

---

## Underlying Base Algorithm(s)
Diagonal grouping and sorting.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n * log(min(m, n)))`
- **Space Complexity**: `O(m * n)` for diagonal groups.
