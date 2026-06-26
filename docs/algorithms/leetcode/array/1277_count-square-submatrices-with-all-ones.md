# Count Square Submatrices with All Ones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1277 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [count-square-submatrices-with-all-ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/) |

## Problem Description & Examples
### Goal
Count every square submatrix whose cells are all `1`.

### Function Contract
**Inputs**

- `matrix`: binary matrix.

**Return value**

The number of all-ones square submatrices.

### Examples
**Example 1**

- Input: `matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]`
- Output: `15`

**Example 2**

- Input: `matrix = [[1,0,1],[1,1,0],[1,1,0]]`
- Output: `7`

**Example 3**

- Input: `matrix = [[1]]`
- Output: `1`

---

## Underlying Base Algorithm(s)
Dynamic programming on square side lengths.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(1)` extra if the input matrix may be updated in place.
