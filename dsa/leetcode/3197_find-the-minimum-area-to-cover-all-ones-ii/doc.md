# Find the Minimum Area to Cover All Ones II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3197 |
| Difficulty | Hard |
| Topics | Array, Matrix, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/) |

## Problem Description

### Goal

You are given a two-dimensional binary array `grid`. Choose exactly three
axis-aligned rectangles, each with non-zero area, so that every cell containing
`1` lies inside at least one of the rectangles.

The rectangles must not overlap, although their boundaries may touch. Cells
containing `0` may lie inside a chosen rectangle. Return the minimum possible
sum of the three rectangle areas.

### Function Contract

**Inputs**

- `grid`: An $R \times C$ binary matrix, where $1 \le R,C \le 30$ and every
  entry is either `0` or `1`.

The matrix contains at least three cells whose value is `1`.

**Return value**

The minimum sum of the areas of three non-overlapping, non-zero-area,
axis-aligned rectangles that cover every `1` in `grid`.

### Examples

#### Example 1

- **Input:** `grid = [[1, 0, 1], [1, 1, 1]]`
- **Output:** `5`

Use area-$2$ rectangles for the left and right columns and a unit rectangle
for the remaining center cell.

#### Example 2

- **Input:** `grid = [[1, 0, 1, 0], [0, 1, 0, 1]]`
- **Output:** `5`

The two `1`s in the first row can share an area-$3$ rectangle, while the two
remaining `1`s use separate unit rectangles.
