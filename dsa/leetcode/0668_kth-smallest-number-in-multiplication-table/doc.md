# Kth Smallest Number in Multiplication Table

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 668 |
| Difficulty | Hard |
| Topics | Math, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/) |

## Problem Description
### Goal
A multiplication table of size $m \times n$ is a one-indexed integer matrix in which cell `(i, j)` contains the product $i \cdot j$. The table is implicit; it does not need to be constructed as a full matrix.

Given `m`, `n`, and `k`, return the `k`th smallest element among all $m \cdot n$ table entries. Equal products in different cells occupy separate positions in the ordering, so rank counts occurrences rather than distinct values.

### Function Contract
**Inputs**

- `m`: the positive number of table rows
- `n`: the positive number of table columns
- `k`: a 1-based rank between `1` and $m \cdot n$

**Return value**

- The integer value of the `k`-th smallest table entry, counting duplicate entries separately

### Examples
**Example 1**

- Input: `m = 3, n = 3, k = 5`
- Output: `3`

**Example 2**

- Input: `m = 2, n = 3, k = 6`
- Output: `6`

**Example 3**

- Input: `m = 2, n = 2, k = 3`
- Output: `2`
