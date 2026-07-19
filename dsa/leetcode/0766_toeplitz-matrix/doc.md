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
