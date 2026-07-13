# Toeplitz Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 766 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/toeplitz-matrix/) |

## Problem Description

### Goal

Given an $m \times n$ integer matrix, determine whether it is a Toeplitz matrix. A matrix is Toeplitz when every diagonal running from top left to bottom right contains the same element throughout that diagonal.

Return `True` if all such diagonals satisfy the condition and `False` otherwise. Different diagonals may contain different values; equality is required only among cells whose row and column indices advance together. One-cell diagonals satisfy the rule automatically.

### Function Contract

**Inputs**

- `matrix`: a nonempty rectangular list of nonempty integer rows.

**Return value**

- `True` when the matrix is Toeplitz; otherwise `False`.

### Examples

**Example 1**

- Input: `matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]`
- Output: `True`
- Explanation: Every descending diagonal repeats its first value.

**Example 2**

- Input: `matrix = [[1,2],[2,2]]`
- Output: `False`
- Explanation: The main diagonal contains `1` and `2`.

**Example 3**

- Input: `matrix = [[3,4,5,6]]`
- Output: `True`
- Explanation: A one-row matrix has only length-one diagonals.

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reduce each diagonal to adjacent comparisons**

Every cell outside the first row and first column has an upper-left predecessor on the same diagonal. Compare `matrix[row][column]` with `matrix[row - 1][column - 1]`. Return false at the first mismatch.

**Why local equality covers the whole diagonal**

If every adjacent pair on a diagonal is equal, transitivity makes every value on that diagonal equal to its first value. Conversely, any diagonal containing two different values must have some first position where its value changes, and that cell fails the upper-left comparison. Checking all eligible cells is therefore both necessary and sufficient.

#### Complexity detail

For `m` rows and `n` columns, the scan performs one comparison for each of $(m - 1)(n - 1)$ eligible cells, taking $O(mn)$ time. It uses only loop indices, for $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Traverse each diagonal once:** Starting from the first row and first column also visits every cell in $O(mn)$ time, but needs more boundary logic.
- **Hash by `row - column`:** All cells with the same difference share a diagonal; storing their first values takes $O(m + n)$ space.
- **Recheck every diagonal prefix:** Walking back to the diagonal start for every cell is correct but can take $O(mn \min(m,n))$ time.
- **Single row or column:** Every diagonal has length one, so the result is always true.
- **Negative and repeated values:** Equality comparisons require no value restrictions.
- **Late mismatch:** The scan must inspect the entire matrix unless it finds a failure.
- **Rectangular shape:** The same upper-left relation works without requiring a square matrix.

</details>
