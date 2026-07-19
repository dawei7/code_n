# Design Tic-Tac-Toe

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 348 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Design, Matrix, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/design-tic-tac-toe/) |

## Problem Description
### Goal
Design a stateful $n \times n$ Tic-Tac-Toe game for players `1` and `2`. Each valid `move(row, col, player)` marks a previously empty cell, and moves arrive in gameplay order with no calls after a winner has been declared.

After each move, return that player's number if the mark completes an entire row, an entire column, the main diagonal, or the opposite diagonal using only that player's marks. Otherwise return `0`. Only lines passing through the newly marked cell can become winners. Preserve board state across calls and determine the result efficiently without rescanning the full board after every move.

### Function Contract
**Inputs**

- `n`: the board dimension
- `moves`: for the app adapter, triples `[row, column, player]` replayed in order. Native LeetCode calls `move(row, col, player)` one move at a time.

**Return value**

- The app adapter returns the status after every move. Each status is `0` when nobody has won, or the winning player number `1` or `2`.

### Examples
**Example 1**

- Input: `n = 3, moves = [[0,0,1],[0,2,2],[2,2,1],[1,1,2],[2,0,1],[1,0,2],[2,1,1]]`
- Output: `[0, 0, 0, 0, 0, 0, 1]`

**Example 2**

- Input: `n = 2, moves = [[0,0,1],[1,0,2],[0,1,1]]`
- Output: `[0, 0, 1]`

**Example 3**

- Input: `n = 1, moves = [[0,0,1]]`
- Output: `[1]`
