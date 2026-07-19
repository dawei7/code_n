# Leftmost Column with at Least a One

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1428 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Matrix, Interactive |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/leftmost-column-with-at-least-a-one/) |

## Problem Description

### Goal

A hidden binary matrix is available only through a `BinaryMatrix` interface. Calling `dimensions()` returns its row and column counts, while `get(row, col)` reveals one cell. Every row is sorted in non-decreasing order, so all zeroes in a row precede all ones.

Return the smallest column index that contains at least one `1` anywhere in the matrix. Return `-1` when the matrix contains no ones. The number of calls to `get` is restricted, so the matrix must not be copied or exhaustively inspected.

### Function Contract

**Inputs**

- `binary_matrix`: a read-only `BinaryMatrix` containing $m$ rows and $n$ columns, where $1 \le m,n \le 100$.
- `binary_matrix.dimensions()` returns `[m, n]`.
- `binary_matrix.get(row, col)` returns the binary value at a valid zero-based position.
- Each row is sorted in non-decreasing order, and at most 1000 calls to `get` may be made.

**Return value**

- The leftmost column index containing a `1`, or `-1` if every cell is `0`.

### Examples

**Example 1**

- Input: `binary_matrix = [[0,0],[1,1]]`
- Output: `0`

**Example 2**

- Input: `binary_matrix = [[0,0],[0,1]]`
- Output: `1`

**Example 3**

- Input: `binary_matrix = [[0,0],[0,0]]`
- Output: `-1`
