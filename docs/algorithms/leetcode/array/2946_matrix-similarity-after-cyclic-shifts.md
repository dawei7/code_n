# Matrix Similarity After Cyclic Shifts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2946 |
| Difficulty | Easy |
| Topics | Array, Math, Matrix, Simulation |
| Official Link | [matrix-similarity-after-cyclic-shifts](https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/) |

## Problem Description & Examples
### Goal
Determine if a matrix remains identical to its original state after performing cyclic shifts on its rows. Specifically, even-indexed rows are shifted to the left by `k` positions, and odd-indexed rows are shifted to the right by `k` positions. The matrix is considered "similar" if the shifted matrix is equal to the original matrix.

### Function Contract
**Inputs**

- `mat`: A 2D list of integers representing the matrix.
- `k`: An integer representing the number of cyclic shifts to perform.

**Return value**

- A boolean: `True` if the matrix is identical to its original state after the specified shifts, `False` otherwise.

### Examples
**Example 1**

- Input: `mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1`
- Output: `False`

**Example 2**

- Input: `mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2`
- Output: `True`

**Example 3**

- Input: `mat = [[2,2],[2,2]], k = 3`
- Output: `True`

---

## Underlying Base Algorithm(s)
The problem relies on the property of cyclic shifts in modular arithmetic. A cyclic shift of a row of length `n` by `k` positions is equivalent to a shift by `k % n`. For a matrix to remain unchanged after a shift, every element at index `j` must be equal to the element at the index it moves to after the shift. Mathematically, this implies that for every row, the element at `mat[i][j]` must equal `mat[i][(j + shift) % n]`.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n)`, where `m` is the number of rows and `n` is the number of columns, as we must inspect every element in the matrix once.
- **Space Complexity**: `O(1)`, as we perform the comparison in-place without allocating additional data structures proportional to the input size.
