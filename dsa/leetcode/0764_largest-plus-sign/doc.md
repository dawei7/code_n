# Largest Plus Sign

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 764 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-plus-sign/) |

## Problem Description

### Goal

Begin with an $n \times n$ grid filled with `1`s, then place `0` at every coordinate listed in `mines`. An axis-aligned plus sign of order `k` has one center cell and four arms extending up, down, left, and right by $k - 1$ cells each, with every covered cell equal to `1`.

Return the largest order of any plus sign in the grid. An order-`1` plus consists only of its center, and if no `1` cell remains the answer is `0`; diagonal cells do not form part of an axis-aligned arm.

### Function Contract

**Inputs**

- `n`: the side length of the square grid.
- `mines`: distinct coordinate pairs `[row, column]` whose cells contain zero.

**Return value**

- The maximum plus order, or `0` when the grid contains no one-cell.

### Examples

**Example 1**

- Input: `n = 5`, `mines = [[4,2]]`
- Output: `2`
- Explanation: Several centers support one one-cell in all four directions, but no order-three plus survives the mine and boundaries.

**Example 2**

- Input: `n = 1`, `mines = [[0,0]]`
- Output: `0`
- Explanation: The only cell is a mine.

**Example 3**

- Input: `n = 3`, `mines = []`
- Output: `2`
- Explanation: The center and its four adjacent cells form an order-two plus.
