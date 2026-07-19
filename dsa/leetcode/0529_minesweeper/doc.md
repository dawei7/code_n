# Minesweeper

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 529 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/minesweeper/) |

## Problem Description
### Goal
Given a Minesweeper board and a click on an unrevealed mine `M` or empty square `E`, update the board after that one click. If the clicked cell is a mine, change it to `X` and stop.

Otherwise count mines in all eight neighboring directions. An empty cell with at least one adjacent mine becomes the corresponding digit `1` through `8`. A cell with no adjacent mine becomes `B`, and its adjacent unrevealed empty cells are revealed recursively by the same rules. Return the updated board without changing already revealed digits or expanding through numbered boundary cells.

### Function Contract
**Inputs**

- `board`: a rectangular character matrix using `M` for unrevealed mines and `E` for unrevealed empty squares
- `click`: the `[row, column]` position selected by the player

**Return value**

- The board after processing the click and every forced reveal

### Examples
**Example 1**

- Input: `board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]`
- Output: `[["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]`

**Example 2**

- Input: `board = [["E","M"],["E","E"]], click = [0,1]`
- Output: `[["E","X"],["E","E"]]`

**Example 3**

- Input: `board = [["E","E","E"],["E","M","E"],["E","E","E"]], click = [0,0]`
- Output: `[["1","E","E"],["E","M","E"],["E","E","E"]]`
