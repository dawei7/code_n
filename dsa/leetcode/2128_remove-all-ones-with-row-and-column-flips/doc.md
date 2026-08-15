# Remove All Ones With Row and Column Flips

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2128 |
| Difficulty | Medium |
| Topics | Array, Math, Bit Manipulation, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/) |

## Problem Description

### Goal

You are given an $m\times n$ binary matrix. In one operation, choose any
complete row or any complete column and flip all of its entries: every `0`
becomes `1`, and every `1` becomes `0`.

You may perform any number of these operations, including none, and may choose
rows and columns in any order. Determine whether it is possible to transform
the entire matrix to zeros.

### Function Contract

**Inputs**

- `grid`: An $m\times n$ matrix whose entries are either `0` or `1`, with
  $1\le m,n\le 300$.

**Return value**

`true` if row and column flips can remove every `1`; otherwise `false`.

### Examples

#### Example 1

- **Input:** `grid = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]`
- **Output:** `true`
- **Explanation:** Flipping the middle row and then the middle column produces an
  all-zero matrix.

#### Example 2

- **Input:** `grid = [[1, 1, 0], [0, 0, 0], [0, 0, 0]]`
- **Output:** `false`
- **Explanation:** No combination of whole-row and whole-column flips can remove
  all ones.

#### Example 3

- **Input:** `grid = [[0]]`
- **Output:** `true`
- **Explanation:** The matrix already contains no ones.
