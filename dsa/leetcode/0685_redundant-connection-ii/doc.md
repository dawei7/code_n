# Redundant Connection II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 685 |
| Difficulty | Hard |
| Topics | Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/redundant-connection-ii/) |

## Problem Description
### Goal
A rooted tree is a directed graph with one root having no parent, every other node having exactly one parent, and every node reachable as a descendant of the root. The input began as such a tree on nodes `1` through `n`, then one extra directed edge was added.

Return one input edge whose removal restores a rooted tree. Edge `[u, v]` points from parent candidate `u` to child candidate `v`. If several removals would produce a valid rooted tree, return the qualifying edge that occurs last in the input order.

### Function Contract
**Inputs**

- `edges`: `n` directed edges `[parent, child]` on nodes labeled `1` through `n`

**Return value**

- The endpoints of the last input edge whose removal restores a rooted directed tree

### Examples
**Example 1**

- Input: `edges = [[1,2],[1,3],[2,3]]`
- Output: `[2,3]`

**Example 2**

- Input: `edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]`
- Output: `[4,1]`

**Example 3**

- Input: `edges = [[2,1],[3,1],[4,2],[1,4]]`
- Output: `[2,1]`
