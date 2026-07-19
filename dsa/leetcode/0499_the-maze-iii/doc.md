# The Maze III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 499 |
| Difficulty | Hard |
| Topics | Array, String, Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path |
| Official Link | [LeetCode](https://leetcode.com/problems/the-maze-iii/) |

## Problem Description
### Goal
Given a maze, a ball position, and a hole, choose rolling directions `u`, `d`, `l`, and `r`. After a direction is chosen, the ball continues through open cells until a wall stops it, except that reaching the hole ends the route immediately even when the ball could otherwise roll farther.

Return a direction string for a route that makes the ball fall into the hole using the minimum traveled distance, where distance counts open cells crossed. If several routes have the same shortest distance, return the lexicographically smallest direction string; if the hole is unreachable, return `"impossible"`. Direction changes are allowed only after the ball stops.

### Function Contract
**Inputs**

- `maze`: a rectangular binary matrix where `0` is open and `1` is a wall
- `ball`: the starting open cell as `[row, column]`
- `hole`: the target open cell where rolling stops immediately

**Return value**

- The lexicographically smallest shortest path using `d`, `l`, `r`, and `u`, or `"impossible"`

### Examples
**Example 1**

- Input: `maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], ball = [4,3], hole = [0,1]`
- Output: `"lul"`

**Example 2**

- Input: `maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], ball = [4,3], hole = [3,0]`
- Output: `"impossible"`

**Example 3**

- Input: `maze = [[0,0,0],[0,0,0],[0,0,0]], ball = [0,0], hole = [2,2]`
- Output: `"dr"`
