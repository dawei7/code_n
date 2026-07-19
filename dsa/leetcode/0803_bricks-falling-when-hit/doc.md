# Bricks Falling When Hit

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 803 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/bricks-falling-when-hit/) |

## Problem Description

### Goal

Given an $m \times n$ binary grid, `1` represents a brick and `0` empty space. A brick is stable when it is in the top row or is connected horizontally or vertically through other stable bricks to the top.

Apply each hit in order by erasing the brick at its coordinate if one exists. Any other bricks that become unstable then fall and are immediately removed rather than landing elsewhere. Return, for every hit, the number of bricks that fall because of it, excluding the brick directly erased by that hit.

### Function Contract

**Inputs**

- `grid`: a rectangular binary matrix, where `1` is a brick and `0` is empty.
- `hits`: a list of `[row, column]` positions struck in order.

**Return value**

- One integer per hit: the number of bricks that fall because of that hit, excluding the brick directly removed by the hit.

### Examples

**Example 1**

- Input: `grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]`
- Output: `[2]`
- Explanation: Removing the lower-left support disconnects the other two bricks in its row from the top.

**Example 2**

- Input: `grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]`
- Output: `[0,0]`
- Explanation: The first removed brick supports nothing, and the second hit does not count the brick it directly removes.

**Example 3**

- Input: `grid = [[1],[1],[1]], hits = [[1,0],[2,0],[0,0]]`
- Output: `[1,0,0]`
- Explanation: The first hit makes the bottom brick fall; later hits strike an empty cell and then the remaining top brick.
