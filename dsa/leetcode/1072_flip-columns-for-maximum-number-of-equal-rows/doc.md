# Flip Columns For Maximum Number of Equal Rows

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1072 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/) |

## Problem Description

### Goal

Given an $M \times N$ binary matrix, choose any number of columns. Flipping a chosen column changes every `0` in that column to `1` and every `1` to `0`, across all rows.

After applying one shared set of column flips, count the rows whose values are all equal within that row: a qualifying row may consist entirely of zeros or entirely of ones. Return the maximum possible number of such rows over every choice of columns.

### Function Contract

**Inputs**

- `matrix`: an $M \times N$ binary matrix, where $1 \le M,N \le 300$.
- Every `matrix[i][j]` is either `0` or `1`.

**Return value**

- The greatest number of rows that can simultaneously have all values equal after flipping some set of columns.

### Examples

**Example 1**

- Input: `matrix = [[0, 1], [1, 1]]`
- Output: `1`
- Explanation: With no flips, the second row already has equal values; no flip pattern makes both rows uniform.

**Example 2**

- Input: `matrix = [[0, 1], [1, 0]]`
- Output: `2`
- Explanation: Flip the first column to turn the rows into `[1, 1]` and `[0, 0]`.

**Example 3**

- Input: `matrix = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]`
- Output: `2`
- Explanation: Flipping the first two columns makes the last two rows uniform.
