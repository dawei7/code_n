# Cells with Odd Values in a Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1252 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/) |

## Problem Description

### Goal

Begin with an $m \times n$ matrix whose entries are all zero. Each operation in `indices` is a pair `[r, c]`: increment every cell in row `r` by one, then increment every cell in column `c` by one. The intersection cell receives both increments.

Apply all operations in their given order and return the number of matrix cells containing an odd value afterward. Repeated row or column indices represent repeated increments and must each affect the final parity.

### Function Contract

**Inputs**

- `m`: the row count, with $1 \le m \le 50$.
- `n`: the column count, with $1 \le n \le 50$.
- `indices`: a list of $k$ valid `[r, c]` operations, where $1 \le k \le 100$, $0 \le r < m$, and $0 \le c < n$.

**Return value**

- Return the number of cells whose final value is odd.

### Examples

**Example 1**

- Input: `m = 2`, `n = 3`, `indices = [[0, 1], [1, 1]]`
- Output: `6`

**Example 2**

- Input: `m = 2`, `n = 2`, `indices = [[1, 1], [0, 0]]`
- Output: `0`

**Example 3**

- Input: `m = 1`, `n = 1`, `indices = [[0, 0]]`
- Output: `0`
- Explanation: The sole cell is incremented once through its row and once through its column, ending at the even value `2`.
