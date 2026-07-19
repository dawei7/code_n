# Out of Boundary Paths

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 576 |
| Difficulty | Medium |
| Topics | Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/out-of-boundary-paths/) |

## Problem Description
### Goal
Place a ball at `(startRow, startColumn)` inside an $m \times n$ grid. On each move, the ball may travel one cell up, down, left, or right. Count the paths that move the ball across any grid boundary using at most `maxMove` moves.

Different sequences of directions count as different paths, and a path is counted when it first leaves the grid; no additional moves are made after that exit. Return the total modulo `1,000,000,007`. Paths may leave before all allowed moves are used, while a sequence that remains inside after `maxMove` moves contributes nothing.

### Function Contract
**Inputs**

- `m: int`: number of grid rows
- `n: int`: number of grid columns
- `maxMove: int`: maximum number of moves the ball may make
- `startRow: int`: starting row inside the grid
- `startColumn: int`: starting column inside the grid

**Return value**

- The number of direction sequences that cross the grid boundary within at most `maxMove` moves, modulo `1,000,000,007`

### Examples
**Example 1**

- Input: `m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0`
- Output: `6`

**Example 2**

- Input: `m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1`
- Output: `12`

**Example 3**

- Input: `m = 3, n = 4, maxMove = 0, startRow = 1, startColumn = 2`
- Output: `0`
