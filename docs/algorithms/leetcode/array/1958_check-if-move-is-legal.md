# Check if Move is Legal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1958 |
| Difficulty | Medium |
| Topics | Array, Matrix, Enumeration |
| Official Link | [check-if-move-is-legal](https://leetcode.com/problems/check-if-move-is-legal/) |

## Problem Description & Examples
### Goal
On an Othello-like board, decide whether placing a color at an empty square creates a legal line: adjacent opponent pieces followed by one of the placed color's pieces in a straight direction.

### Function Contract
**Inputs**

- `board`: an `8 x 8` grid containing `'B'`, `'W'`, and `'.'`.
- `rMove`, `cMove`: the empty target cell.
- `color`: the piece color to place.

**Return value**

Return `True` if the move is legal, otherwise `False`.

### Examples
**Example 1**

- Input: `board = [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]], rMove = 4, cMove = 3, color = "B"`
- Output: `True`

**Example 2**

- Input: `board = [[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]], rMove = 4, cMove = 4, color = "W"`
- Output: `False`

**Example 3**

- Input: `board = [["B",".",".",".",".",".",".","."],["W",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]], rMove = 2, cMove = 0, color = "B"`
- Output: `True`

---

## Underlying Base Algorithm(s)
Try all eight directions from the move square. A direction is legal only if it first sees at least one opponent piece and then reaches a same-color piece before leaving the board or hitting an empty cell.

---

## Complexity Analysis
- **Time Complexity**: `O(1)` because the board is fixed at `8 x 8`.
- **Space Complexity**: `O(1)`
