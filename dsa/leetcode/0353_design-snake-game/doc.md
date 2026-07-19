# Design Snake Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 353 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Design, Queue, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/design-snake-game/) |

## Problem Description
### Goal
Simulate a snake beginning at the board's top-left cell on a `height x width` grid. Each `U`, `D`, `L`, or `R` move advances the head one cell. Food appears in the supplied order, and only the next food item can be consumed when the head reaches its coordinate.

Eating food increases the score and leaves the tail in place, growing the snake. Otherwise the tail advances, so moving into the cell it vacates is allowed. Moving outside the board or into any remaining body cell ends the game and returns `-1`; successful moves return the current score. Preserve all state across calls.

### Function Contract
**Inputs**

- `width`, `height`: board dimensions in columns and rows
- `food`: food coordinates `[row, column]` in consumption order
- `directions`: for the app adapter, the sequence of `"U"`, `"D"`, `"L"`, and `"R"` moves. Native LeetCode calls `move(direction)` individually.

**Return value**

- The app adapter returns the score after every move, or `-1` at the losing move. Native `move` returns that move's status directly.

### Examples
**Example 1**

- Input: `width = 3, height = 2, food = [[1,2],[0,1]], directions = ["R","D","R","U","L","U"]`
- Output: `[0, 0, 1, 1, 2, -1]`

**Example 2**

- Input: `width = 1, height = 1, food = [], directions = ["R"]`
- Output: `[-1]`

**Example 3**

- Input: `width = 2, height = 2, food = [[0,1]], directions = ["R","D","L","U"]`
- Output: `[1, 1, 1, 1]`
