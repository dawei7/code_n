# Find Winner on a Tic Tac Toe Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1275 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/) |

## Problem Description

### Goal

Two players, `A` and `B`, play tic-tac-toe on an initially empty $3 \times 3$ grid. Player `A` moves first and marks `X`; player `B` marks `O`. They alternate turns, always selecting an empty cell. The game ends as soon as one player fills an entire row, column, or diagonal with their mark, or when all nine cells are occupied.

Array `moves` lists the played cells in chronological order. The sequence is guaranteed to describe a valid game, including the rule that no move occurs after the game has ended. Return the winning player's name if a win occurred. If the board filled without a winner, return `"Draw"`; if the valid sequence has not yet ended, return `"Pending"`.

### Function Contract

**Inputs**

- `moves`: a list of $m$ distinct coordinate pairs `[row, col]`, where $1 \le m \le 9$ and each coordinate is between $0$ and $2$ inclusive. Even-indexed moves belong to `A`; odd-indexed moves belong to `B`.

**Return value**

- Return exactly `"A"`, `"B"`, `"Draw"`, or `"Pending"` according to the final state represented by the valid move sequence.

### Examples

**Example 1**

- Input: `moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]`
- Output: `"A"`

**Example 2**

- Input: `moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]`
- Output: `"B"`

**Example 3**

- Input: `moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]`
- Output: `"Draw"`
