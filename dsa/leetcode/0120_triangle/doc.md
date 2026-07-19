# Triangle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 120 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/triangle/) |

## Problem Description
### Goal
Given a triangular array of integers, choose a connected path from its single top value to some value in the bottom row. If the current value is at index `j` of one row, the next value must be either index `j` or index $j + 1$ in the row directly below.

Return the minimum path sum, including both endpoints and exactly one value from every row. Choices cannot skip levels or move to nonadjacent positions. Entries may be negative, so the path with the smallest individual early value is not necessarily optimal; a one-row triangle simply returns its sole value.

### Function Contract
**Inputs**

- `triangle`: rows of lengths `1, 2, ..., r` containing integer values

**Return value**

The minimum total of any valid top-to-bottom path.

### Examples
**Example 1**

- Input: `triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]`
- Output: `11`

**Example 2**

- Input: `triangle = [[-10]]`
- Output: `-10`

**Example 3**

- Input: `triangle = [[1], [2, 3], [4, 5, 6]]`
- Output: `7`
