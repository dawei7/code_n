# Check Knight Tour Configuration

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2596 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-knight-tour-configuration/) |

## Problem Description

### Goal

A knight is meant to tour an $n \times n$ chessboard, beginning at the top-left cell and visiting every cell exactly once. The matrix `grid` records the visit order: `grid[row][col]` is the zero-based move number at which the knight visits `(row, col)`.

Every value from $0$ through $n^2-1$ occurs exactly once. Consecutive move numbers must describe legal knight moves: two cells in one axis and one cell in the other axis.

Return whether the recorded order is a valid complete tour that starts at `(0, 0)`.

### Function Contract

**Inputs**

- `grid`: A square matrix of distinct integers containing every value from $0$ through $n^2-1$ exactly once.

The board dimension satisfies $3 \leq n \leq 7$.

**Return value**

- `true` if move zero is at the top-left cell and every pair of consecutive moves forms a legal knight move; otherwise, `false`.

### Examples

#### Example 1

- **Input:** `grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]`
- **Output:** `true`

The visit order starts at the top-left and every transition from move zero through move 24 has coordinate differences one and two.

#### Example 2

- **Input:** `grid = [[0,3,6],[5,8,1],[2,7,4]]`
- **Output:** `false`

The transition from move `7` to move `8` is not a legal knight move.
