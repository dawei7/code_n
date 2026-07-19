# Nearest Exit from Entrance in Maze

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/) |
| Frontend ID | 1926 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given a rectangular maze whose cells are either open (`"."`) or walls (`"+"`), together with the coordinates of an open entrance cell. From one open cell, one step may move up, down, left, or right to another open cell. Movement through a wall or outside the grid is forbidden.

An exit is an open cell on the outer border of the maze, except that the entrance itself never counts even when it lies on that border. Return the fewest steps needed to reach any exit from the entrance, or `-1` when no exit is reachable.

### Function Contract

**Inputs**

- `maze`: an $R \times C$ matrix containing only `"."` and `"+"`.
- `entrance`: `[row, column]` for an open cell in `maze`.
- $1 \le R,C \le 100$.

**Return value**

- Return the shortest four-directional path length from `entrance` to a different open boundary cell.
- Return `-1` if no such boundary cell is reachable.

### Examples

**Example 1**

- Input: `maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]`
- Output: `1`

The open cell directly above the entrance is an exit.

**Example 2**

- Input: `maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]`
- Output: `2`

The entrance is on the border but is excluded; the exit is at the other end of the row.

**Example 3**

- Input: `maze = [[".","+"]], entrance = [0,0]`
- Output: `-1`
