# Check if Move is Legal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1958 |
| Difficulty | Medium |
| Topics | Array, Matrix, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-move-is-legal/) |

## Problem Description
### Goal
An 8-by-8 game board uses `"."` for a free cell, `"W"` for a white piece,
and `"B"` for a black piece. A move places the given color on the specified
free cell.

The move is legal only when the newly occupied cell becomes one endpoint of a
horizontal, vertical, or diagonal good line. Such a line contains at least
three cells: both endpoints have the played color, every cell strictly between
them has the opposite color, and no cell in the line is free. Return whether
the proposed move is legal.

### Function Contract
**Inputs**

- `board`: an 8-by-8 matrix containing only `"."`, `"W"`, and `"B"`.
- `rMove`, `cMove`: zero-based coordinates in $[0,7]$ identifying a free cell.
- `color`: either `"W"` or `"B"`, the color placed by the proposed move.

**Return value**

- `True` if the new piece is an endpoint of at least one good line; otherwise
  `False`.

### Examples
**Example 1**

- Input: `board = [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]], rMove = 4, cMove = 3, color = "B"`
- Output: `True`

**Example 2**

- Input: `board = [[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]], rMove = 4, cMove = 4, color = "W"`
- Output: `False`

**Example 3**

- Input: `board = [[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","W","B",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]], rMove = 3, cMove = 3, color = "B"`
- Output: `True`
