# Number of Paths with Max Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1301 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-paths-with-max-score/) |

## Problem Description
### Goal
A square character board has `E` in its top-left cell and `S` in its bottom-right cell. Every other cell contains either a digit from `1` through `9` or an obstacle `X`. Starting at `S`, move only up, left, or diagonally up-left, and never enter an obstacle.

A path's score is the sum of the numeric cells it visits; `S` and `E` contribute nothing. Return both the greatest score attainable on a path reaching `E` and the number of paths attaining exactly that score, with the count reduced modulo $10^9+7$. If `E` cannot be reached, return `[0,0]`.

### Function Contract
**Inputs**

- `board`: a list of $n$ strings, each of length $n$, where $2 \le n \le 100$.
- `board[0][0] = "E"` and `board[n - 1][n - 1] = "S"`; every other character is `"X"` or a digit from `"1"` through `"9"`.

**Return value**

A two-element array `[maximum_score, number_of_maximum_score_paths]`, with the second value modulo $10^9+7$; return `[0,0]` when no valid path exists.

### Examples
**Example 1**

- Input: `board = ["E23","2X2","12S"]`
- Output: `[7,1]`

**Example 2**

- Input: `board = ["E12","1X1","21S"]`
- Output: `[4,2]`

**Example 3**

- Input: `board = ["E11","XXX","11S"]`
- Output: `[0,0]`
- Explanation: The obstacle row prevents every route from reaching `E`.
