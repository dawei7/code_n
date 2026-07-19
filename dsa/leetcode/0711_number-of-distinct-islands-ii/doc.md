# Number of Distinct Islands II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 711 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Depth-First Search, Breadth-First Search, Union-Find, Sorting, Matrix, Hash Function |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-distinct-islands-ii/) |

## Problem Description
### Goal
Given a binary grid, an island is a maximal group of `1` cells connected horizontally or vertically. Count how many distinct island shapes occur.

Two islands have the same shape when one can be translated, rotated by a multiple of 90 degrees, or reflected so that all occupied cells coincide. Absolute location and any of those transformations do not create a new shape, while diagonal contact does not join islands. Return the number of equivalence classes under all allowed transformations.

### Function Contract
**Inputs**

- `grid`: a rectangular matrix whose `1` cells are land and whose `0` cells are water

**Return value**

- The number of island equivalence classes under translation, quarter-turn rotations, and reflection

### Examples
**Example 1**

- Input: `grid = [[1,1,0,1],[0,0,0,1]]`
- Output: `1`
- Explanation: the horizontal and vertical dominoes differ only by rotation.

**Example 2**

- Input: `grid = [[1,0,0,1,1],[1,1,0,0,1]]`
- Output: `1`
- Explanation: the two three-cell corners are congruent after reflection and rotation.

**Example 3**

- Input: `grid = [[1,1,1,0,1,0],[0,0,0,0,1,1]]`
- Output: `2`
- Explanation: a three-cell line cannot become a three-cell corner.
