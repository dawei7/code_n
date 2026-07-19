# N-Queens II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 52 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/n-queens-ii/) |

## Problem Description
### Goal
Place exactly `n` queens on an $n \times n$ chessboard so that no queen can attack another. Thus each row and column contains one queen, and no two selected cells share either diagonal direction.

Return the number of distinct valid placements rather than constructing their board representations. Placements using different queen cells count separately, including mirror images or rotations when they occupy different coordinates. For board sizes with no solution, return zero; the $1 x 1$ board has one placement.

### Function Contract
**Inputs**

- `n`: the board width and number of queens, with $1 \le n \le 9$

**Return value**

The integer number of valid placements.

### Examples
**Example 1**

- Input: `n = 1`
- Output: `1`

**Example 2**

- Input: `n = 4`
- Output: `2`

**Example 3**

- Input: `n = 5`
- Output: `10`
