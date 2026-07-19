# Maximal Rectangle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 85 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Stack, Matrix, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximal-rectangle/) |

## Problem Description
### Goal
You are given a rectangular character matrix containing only `"0"` and `"1"`. Choose an axis-aligned rectangle whose cells are all `"1"`; its sides must follow row and column boundaries, and it must cover a contiguous range of rows and columns.

Return the largest possible rectangle area measured in cells. A single one-cell is a valid area-one rectangle, while a matrix with no ones returns zero. The rectangle may span the entire matrix or any smaller all-one region.

### Function Contract
**Inputs**

- `matrix`: a nonempty rectangular matrix containing `"0"` and `"1"`

**Return value**

The maximum all-one rectangle area.

### Examples
**Example 1**

- Input: `matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]`
- Output: `6`

**Example 2**

- Input: `matrix = [["0"]]`
- Output: `0`

**Example 3**

- Input: `matrix = [["1","1"],["1","1"]]`
- Output: `4`
