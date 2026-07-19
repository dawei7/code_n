# Number of Spaces Cleaning Robot Cleaned

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2061 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/) |

## Problem Description

### Goal

A binary matrix represents a room: `0` is an empty space and `1` is an object. The upper-left space is always empty. A cleaning robot starts there facing right, and its starting space and every empty space it visits become clean.

The robot repeatedly attempts to move one cell straight ahead. If the next cell is outside the room or contains an object, it stays in place and turns $90^\circ$ clockwise; otherwise it advances without changing direction. The robot runs indefinitely. Return the number of distinct spaces it eventually cleans.

### Function Contract

**Inputs**

- `room`: an $m\times n$ binary matrix, where $1 \le m,n \le 300$ and `room[0][0] == 0`.

**Return value**

- Return the number of distinct empty cells visited by the indefinitely running robot.

### Examples

**Example 1**

- Input: `room = [[0,0,0],[1,1,0],[0,0,0]]`
- Output: `7`
- Explanation: The robot follows the open outer path and visits every empty cell.

**Example 2**

- Input: `room = [[0,1,0],[1,0,0],[0,0,0]]`
- Output: `1`
- Explanation: Objects or boundaries block all four directions from the start.

**Example 3**

- Input: `room = [[0,0,0],[0,0,0],[0,0,0]]`
- Output: `8`
- Explanation: The motion cycles around the boundary and never visits the center.
