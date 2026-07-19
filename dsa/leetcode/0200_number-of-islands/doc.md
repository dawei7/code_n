# Number of Islands

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 200 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-islands/) |

## Problem Description
### Goal
Given a nonempty rectangular grid whose cells are `"1"` for land and `"0"` for water, group land cells that can reach one another through a sequence of horizontal or vertical land neighbors. Each maximal connected group represents one island surrounded by water or the grid boundary.

Return the number of distinct islands. Diagonal contact alone does not connect land, separate components must be counted independently even when close together, and every land cell belongs to exactly one component. An all-water grid returns `0`, while any connected shape of land—regardless of holes or irregular boundaries—contributes one island.

### Function Contract
**Inputs**

- `grid`: a nonempty matrix whose cells are `"1"` for land or `"0"` for water

**Return value**

The number of distinct land components connected horizontally or vertically.

### Examples
**Example 1**

- Input: `[["1","1","0"],["1","0","0"],["0","0","1"]]`
- Output: `2`

**Example 2**

- Input: all water
- Output: `0`

**Example 3**

- Diagonal land cells only
- Output: one island per land cell
