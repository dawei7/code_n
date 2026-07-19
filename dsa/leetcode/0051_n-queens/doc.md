# N-Queens

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 51 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/n-queens/) |

## Problem Description
### Goal
Place exactly `n` chess queens on an $n \times n$ board. A valid placement must prevent every pair of queens from sharing a row, a column, or either diagonal, since queens attack along all of those lines.

Return every distinct valid board in any order. Represent each board as `n` strings of length `n`, using `Q` for a queen and `.` for an empty square. Each valid board must appear once. When no placement exists, return an empty collection.

### Function Contract
**Inputs**

- `n`: the board width and number of queens, with $1 \le n \le 9$

**Return value**

A `List[List[str]]` containing every distinct valid board.

### Examples
**Example 1**

- Input: `n = 4`
- Output: `[ [".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."] ]`

**Example 2**

- Input: `n = 1`
- Output: `[["Q"]]`

**Example 3**

- Input: `n = 2`
- Output: `[]`
