# Maximal Square

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 221 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximal-square/) |

## Problem Description
### Goal
Given a nonempty rectangular matrix whose entries are the characters `"0"` and `"1"`, find an axis-aligned square submatrix in which every cell is `"1"`. The square must occupy consecutive rows and columns and have equal height and width.

Return the area of the largest such square, not its side length or coordinates. A single `"1"` forms an area-one square, while an all-zero matrix returns `0`. When several largest squares exist, their shared area is sufficient. Rectangular all-one regions whose shorter dimension limits the square contribute only the area of their largest square portion.

### Function Contract
**Inputs**

- `matrix`: a nonempty rectangular matrix of `"0"` and `"1"`

**Return value**

The largest all-one square's area.

### Examples
**Example 1**

- A matrix containing a two-by-two all-one region
- Output: `4`

**Example 2**

- Input: `[["0","1"],["1","0"]]`
- Output: `1`

**Example 3**

- Input: `[["0"]]`
- Output: `0`
