# Brick Wall

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 554 |
| Difficulty | Medium |
| Topics | Array, Hash Table |
| Official Link | [LeetCode](https://leetcode.com/problems/brick-wall/) |

## Problem Description
### Goal
Each row of a rectangular wall is made from positive-width bricks, and every row has the same total width. Draw one vertical line from the top of the wall to the bottom without placing it along the wall's left or right outer edge.

Return the minimum number of bricks the line crosses. Passing through an internal edge between two bricks in a row crosses no brick in that row, while passing through a brick's interior crosses one. The line has one shared horizontal coordinate for all rows; the function returns only the minimum count, not the coordinate.

### Function Contract
**Inputs**

- `wall`: a list of rows, where each row lists positive brick widths and every row has the same total width

**Return value**

- The minimum number of bricks crossed by a legal vertical line

### Examples
**Example 1**

- Input: `wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]`
- Output: `2`

**Example 2**

- Input: `wall = [[1], [1], [1]]`
- Output: `3`

**Example 3**

- Input: `wall = [[1, 1]]`
- Output: `0`
