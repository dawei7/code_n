# Game of Life

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 289 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/game-of-life/) |

## Problem Description
### Goal
Given a binary matrix representing a Game of Life board, each cell has up to eight horizontal, vertical, and diagonal neighbors. Compute the next generation from the complete original board: a live cell survives with two or three live neighbors, while a dead cell becomes live with exactly three.

All other live cells die from underpopulation or overpopulation, and all other dead cells remain dead. Update the supplied board in place and return nothing. Every transition must occur simultaneously, so a newly changed cell cannot influence another cell's neighbor count during the same generation. Cells outside the finite board are treated as absent rather than wrapping around.

### Function Contract
**Inputs**

- `board`: a mutable matrix where one means live and zero means dead

**Return value**

Returns `None`; the board is updated in place according to the standard underpopulation, survival, overpopulation, and reproduction rules.

### Examples
**Example 1**

- Input: `board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]`
- Output: `[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]`

**Example 2**

- Input: `board = [[1,1],[1,0]]`
- Output: `[[1,1],[1,1]]`

**Example 3**

- Input: `board = [[1]]`
- Output: `[[0]]`
