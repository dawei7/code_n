# Redundant Connection

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 684 |
| Difficulty | Medium |
| Topics | Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/redundant-connection/) |

## Problem Description
### Goal
A connected, cycle-free undirected tree originally contained `n` nodes labeled `1` through `n`. One additional edge between two different vertices was added, producing the input list `edges` of length `n` and creating a cycle.

Return one input edge whose removal makes the graph a tree again. If more than one edge on the cycle could be removed successfully, return the valid answer that occurs last in the input order. Preserve the edge's endpoint order as it appears in `edges`.

### Function Contract
**Inputs**

- `edges`: the `n` undirected edges of the tree-plus-one-edge graph, in their given order

**Return value**

- The two endpoints of the last input edge that can be removed to restore a tree

### Examples
**Example 1**

- Input: `edges = [[1,2],[1,3],[2,3]]`
- Output: `[2,3]`

**Example 2**

- Input: `edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]`
- Output: `[1,4]`

**Example 3**

- Input: `edges = [[2,3],[1,2],[1,3]]`
- Output: `[1,3]`
