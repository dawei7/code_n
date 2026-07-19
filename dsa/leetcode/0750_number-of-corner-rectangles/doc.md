# Number Of Corner Rectangles

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 750 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-corner-rectangles/) |

## Problem Description

### Goal

Given a rectangular binary matrix, count the axis-aligned rectangles whose four corner cells all contain `1`.

Each rectangle must choose two distinct rows and two distinct columns; the values in its interior and along its noncorner boundary positions do not matter. Count rectangles by their four selected corner coordinates, so different row or column choices are separate even when rectangles overlap. Return the total number of valid rectangles.

### Function Contract

**Inputs**

- `grid`: a non-empty rectangular matrix containing only `0` and `1`.

**Return value**

- The number of choices of two rows and two columns for which all four intersection cells are `1`.

### Examples

**Example 1**

- Input: `grid = [[1,0,0,1,0],[0,0,1,0,1],[0,0,0,1,0],[1,0,1,0,1]]`
- Output: `1`
- Explanation: The last two `1` columns shared by rows `1` and `3` form the only valid rectangle.

**Example 2**

- Input: `grid = [[1,1,1],[1,1,1],[1,1,1]]`
- Output: `9`
- Explanation: Choose any two of three rows and any two of three columns.
