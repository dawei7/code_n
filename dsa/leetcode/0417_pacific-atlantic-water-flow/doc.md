# Pacific Atlantic Water Flow

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 417 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/pacific-atlantic-water-flow/) |

## Problem Description
### Goal
Given a nonempty rectangular elevation matrix, water from a cell may move horizontally or vertically to an adjacent cell whose height is less than or equal to the current height. The Pacific borders the top and left edges, while the Atlantic borders the bottom and right edges.

Return every coordinate `[row, column]` from which some downhill-or-level route can reach both oceans, in any order. The two routes may differ and can leave through different boundary cells. Diagonal movement and uphill flow are forbidden. A cell touching both ocean boundaries qualifies directly, and repeated heights may form level-connected drainage regions.

### Function Contract
**Inputs**

- `heights`: a nonempty rectangular elevation matrix

**Return value**

- Return all `[row, column]` coordinates that can flow to both oceans, in any order.

### Examples
**Example 1**

- Input: `heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]`
- Output: `[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]`

**Example 2**

- Input: `heights = [[1]]`
- Output: `[[0,0]]`

**Example 3**

- Input: `heights = [[2,2],[2,2]]`
- Output: `[[0,0],[0,1],[1,0],[1,1]]`
