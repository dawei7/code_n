# Diagonal Traverse

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 498 |
| Difficulty | Medium |
| Topics | Array, Matrix, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/diagonal-traverse/) |

## Problem Description
### Goal
Given a nonempty $m \times n$ matrix `mat`, traverse diagonals whose cells share the same row-plus-column index, beginning at the top-left cell. Visit the first diagonal upward-right, reverse direction at a boundary, then alternate downward-left and upward-right for successive diagonals.

Return all $m \cdot n$ elements in that diagonal order, including each cell exactly once. Rectangular matrices, single rows, and single columns must follow the same boundary transitions. The function returns element values rather than coordinates and may not skip or repeat a boundary cell when changing direction.

### Function Contract
**Inputs**

- `mat`: a nonempty rectangular integer matrix

**Return value**

- All matrix values in the required alternating diagonal order

### Examples
**Example 1**

- Input: `mat = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `[1,2,4,7,5,3,6,8,9]`

**Example 2**

- Input: `mat = [[1,2],[3,4]]`
- Output: `[1,2,3,4]`

**Example 3**

- Input: `mat = [[1,2,3]]`
- Output: `[1,2,3]`
