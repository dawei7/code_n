# Check if Every Row and Column Contains All Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2133 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/) |

## Problem Description

### Goal

An $n\times n$ integer matrix is valid when every row and every column
contains all integers from $1$ through $n$, inclusive. Given such a square
matrix, determine whether it satisfies that condition everywhere.

Because each row and column has exactly $n$ positions and every input value is
already guaranteed to lie in the required range, containing all required
numbers is equivalent to containing no duplicate.

### Function Contract

**Inputs**

- `matrix`: An $n\times n$ matrix with $1\le n\le 100$ and
  $1\le \texttt{matrix[i][j]}\le n$.

**Return value**

`true` if every row and column contains each integer from $1$ through $n`;
otherwise `false`.

### Examples

#### Example 1

- **Input:** `matrix = [[1,2,3],[3,1,2],[2,3,1]]`
- **Output:** `true`
- **Explanation:** Every row and column contains `1`, `2`, and `3`.

#### Example 2

- **Input:** `matrix = [[1,1,1],[1,2,3],[1,2,3]]`
- **Output:** `false`
- **Explanation:** The first row and first column omit required values.
