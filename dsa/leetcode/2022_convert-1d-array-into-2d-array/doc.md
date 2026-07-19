# Convert 1D Array Into 2D Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2022 |
| Difficulty | Easy |
| Topics | Array, Matrix, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/convert-1d-array-into-2d-array/) |

## Problem Description

### Goal

Given a zero-indexed one-dimensional integer array `original` and positive
integers `m` and `n`, construct a matrix with exactly `m` rows and `n` columns
using every source element.

Preserve row-major order: indices `0` through `n - 1` form the first row,
indices `n` through `2 * n - 1` form the second row, and so forth. If the
requested dimensions cannot hold exactly all elements, return an empty matrix.

### Function Contract

Let $L$ be the length of `original`.

**Inputs**

- `original`: a list of $L$ integers, where $1 \le L \le 5 \cdot 10^4$ and
  every value is between $1$ and $10^5$, inclusive.
- `m`: the requested number of rows, where $1 \le m \le 4 \cdot 10^4$.
- `n`: the requested number of columns, where $1 \le n \le 4 \cdot 10^4$.

**Return value**

- An `m`-by-`n` list of lists in row-major order when $L = mn$; otherwise, an
  empty list.

### Examples

**Example 1**

- Input: `original = [1, 2, 3, 4], m = 2, n = 2`
- Output: `[[1, 2], [3, 4]]`

**Example 2**

- Input: `original = [1, 2, 3], m = 1, n = 3`
- Output: `[[1, 2, 3]]`

**Example 3**

- Input: `original = [1, 2], m = 1, n = 1`
- Output: `[]`
- Explanation: One cell cannot contain both source elements.
