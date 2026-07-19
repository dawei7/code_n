# Where Will the Ball Fall

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1706 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/where-will-the-ball-fall/) |

## Problem Description
### Goal

A box is represented by an $m \times n$ matrix `grid`, with its top and bottom open. Each cell contains one diagonal board. A value of `1` is a board descending from the cell's top-left corner to its bottom-right corner and redirects a ball right; `-1` descends from top-right to bottom-left and redirects a ball left.

Drop one ball into the top of every column. A ball moves through the rows in order, but it becomes stuck if a board directs it into a side wall or if two neighboring boards form a `V` around it. Return the bottom exit column of every ball in starting-column order, using `-1` for each ball that cannot leave the box.

### Function Contract
**Inputs**

- `grid`: an $m \times n$ matrix containing only `1` and `-1`
- $1 \le m,n \le 100$, and every row has exactly $n$ entries

**Return value**

A length-$n$ list where entry `start` is the exit column for the ball dropped above `grid[0][start]`, or `-1` when that ball gets stuck.

### Examples
**Example 1**

- Input: `grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]`
- Output: `[1, -1, -1, -1, -1]`

Only the ball from column zero follows compatible adjacent boards through every row and exits at column one.

**Example 2**

- Input: `grid = [[-1]]`
- Output: `[-1]`

The only board points through the left wall, so the ball is immediately stuck.

**Example 3**

- Input: `grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]`
- Output: `[0, 1, 2, 3, 4, -1]`

The first five balls alternate right and left moves and return to their starting columns; the last ball hits the right wall in the first row.
