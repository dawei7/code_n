# Available Captures for Rook

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 999 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/available-captures-for-rook/) |

## Problem Description

### Goal

You are given an $8\times8$ matrix representing a chessboard. Exactly one white rook is marked `'R'`; white bishops are marked `'B'`, black pawns are marked `'p'`, and empty squares are marked `'.'`.

The rook can move horizontally or vertically through any number of empty squares until it reaches the board edge or another piece. It attacks a pawn when it can reach that pawn's square in one move, but it cannot pass through a bishop or another pawn. Return the number of black pawns currently attacked by the rook.

### Function Contract

**Inputs**

- `board`: exactly eight rows of eight characters each. Every cell is `'R'`, `'B'`, `'p'`, or `'.'`, and exactly one cell contains the rook.

**Return value**

- The number of directions in which the first piece visible from the rook is a black pawn.

### Examples

**Example 1**

- Input: a board with the rook at row $2$, column $3$ and unobstructed pawns above, right, and below it.
- Output: `3`
- Explanation: All three pawns are reachable in one rook move.

**Example 2**

- Input: a board with a bishop immediately adjacent to the rook in every direction.
- Output: `0`
- Explanation: Each bishop blocks the pawns beyond it.

**Example 3**

- Input: a board where the first visible pieces are pawns above, left, and right, while a bishop blocks the downward pawn.
- Output: `3`
