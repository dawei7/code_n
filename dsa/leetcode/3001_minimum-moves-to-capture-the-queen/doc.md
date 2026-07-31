# Minimum Moves to Capture The Queen

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3001 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-moves-to-capture-the-queen/) |

## Problem Description
### Goal
A 1-indexed $8\times8$ chessboard contains a white rook, a white bishop, and a
stationary black queen. The rook is at `(a, b)`, the bishop is at `(c, d)`, and
the queen is at `(e, f)`; the three squares are distinct.

Only the white pieces may move. A rook moves any positive number of squares
horizontally or vertically, while a bishop moves any positive number of
squares diagonally. Neither piece may jump over another piece. A move captures
the queen when the moving white piece reaches its square.

Return the minimum number of white moves required to capture the queen.

### Function Contract
**Inputs**

- `a`: the rook's row
- `b`: the rook's column
- `c`: the bishop's row
- `d`: the bishop's column
- `e`: the queen's row
- `f`: the queen's column

Every coordinate is between 1 and 8 inclusive, and no two pieces occupy the
same square.

**Return value**

Return the minimum number of legal white-piece moves needed for a capture.

### Examples
**Example 1**

- Input: `a = 1, b = 1, c = 8, d = 8, e = 2, f = 3`
- Output: `2`

Neither white piece initially attacks the queen, but the rook can capture it
after repositioning once.

**Example 2**

- Input: `a = 5, b = 3, c = 3, d = 4, e = 5, f = 2`
- Output: `1`

The rook and bishop each have an unobstructed capture in one move.
