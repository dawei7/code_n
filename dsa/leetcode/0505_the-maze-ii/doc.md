# The Maze II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 505 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path |
| Official Link | [LeetCode](https://leetcode.com/problems/the-maze-ii/) |

## Problem Description
### Goal
Given a maze of open cells and walls, a ball starts at one open position. From any stop it may roll in one of four orthogonal directions, but it cannot change direction until a wall blocks the next cell; it then stops at the last open cell before that wall.

Return the shortest distance required for the ball to stop exactly at the destination, or `-1` if no sequence of rolls can do so. Distance counts the number of open cells crossed and does not count the starting cell. Passing over the destination without stopping is insufficient, and different roll sequences may reach the same stopping cell with different traveled distances.

### Function Contract
**Inputs**

- `maze`: a rectangular binary matrix where `0` is open and `1` is a wall
- `start`: the ball's initial open cell as `[row, column]`
- `destination`: the open cell where the ball must come to rest

**Return value**

- The minimum traveled distance among routes that stop at `destination`, or `-1` if no such route exists

### Examples
**Example 1**

- Input: `maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]`
- Output: `12`

**Example 2**

- Input: `maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]`
- Output: `-1`

**Example 3**

- Input: `maze = [[0,0,0],[0,0,0],[0,0,0]], start = [0,0], destination = [2,2]`
- Output: `4`
