# 01 Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 542 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Breadth-First Search, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/01-matrix/) |

## Problem Description
### Goal
Given a nonempty binary matrix containing at least one `0`, compute a distance for every cell. Movement is allowed one step at a time between horizontally or vertically adjacent cells, and each step has distance one.

Return a matrix of the same dimensions where entry `(r, c)` is the minimum number of steps from the input cell `(r, c)` to any cell containing zero. Every zero has distance zero, diagonal movement is not allowed, and different cells may use different nearest zeroes. Preserve the input shape and return distances rather than paths or nearest-zero coordinates.

### Function Contract
**Inputs**

- `mat`: a nonempty rectangular matrix of zeros and ones containing at least one zero

**Return value**

- A matrix of the same dimensions where each entry is the minimum number of horizontal or vertical steps to any zero

### Examples
**Example 1**

- Input: `mat = [[0,0,0],[0,1,0],[0,0,0]]`
- Output: `[[0,0,0],[0,1,0],[0,0,0]]`

**Example 2**

- Input: `mat = [[0,0,0],[0,1,0],[1,1,1]]`
- Output: `[[0,0,0],[0,1,0],[1,2,1]]`

**Example 3**

- Input: `mat = [[1,1,0,1]]`
- Output: `[[2,1,0,1]]`
