# The Maze

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 490 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/the-maze/) |

## Problem Description
### Goal
Given a maze of open cells and walls, a ball starts at one open position. From a stopped position it may be sent up, down, left, or right, but after choosing a direction it keeps rolling through open cells until a wall blocks the next step; only then may a new direction be chosen.

Return whether some sequence of rolls makes the ball stop exactly at the destination. Merely passing over the destination while the ball can continue does not succeed. The ball cannot cross walls or leave the maze, and a route is evaluated by its stopping positions rather than by ordinary one-cell movement at every open coordinate.

### Function Contract
**Inputs**

- `maze`: a rectangular matrix where `0` is open and `1` is a wall
- `start`: the initial open cell as `[row, column]`
- `destination`: the open cell where the ball must stop

**Return value**

- `True` if some sequence of rolls stops at the destination; otherwise `False`

### Examples
**Example 1**

- Input: `maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]`
- Output: `True`

**Example 2**

- Input: `maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]`
- Output: `False`

**Example 3**

- Input: `maze = [[0,0,0],[0,0,0],[0,0,0]], start = [0,0], destination = [1,1]`
- Output: `False`
