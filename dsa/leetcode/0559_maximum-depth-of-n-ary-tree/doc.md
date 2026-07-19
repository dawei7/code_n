# Maximum Depth of N-ary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 559 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Breadth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/) |

## Problem Description
### Goal
Given the root of an N-ary tree, the depth of a node is the number of nodes on the path from the root to that node, including both endpoints. The root therefore has depth one, and every child level increases depth by one.

Return the maximum depth over all nodes, equivalently the number of nodes on the longest root-to-leaf path. An empty tree has depth zero, and a one-node tree has depth one. Children may be absent or numerous at different nodes; the function returns only the depth, not the deepest leaf or path.

### Function Contract
**Inputs**

- `root`: the app representation of an N-ary node as `[value, children]`, recursively, or `None` for an empty tree

**Return value**

- The tree's maximum depth as an integer

### Examples
**Example 1**

- Input tree: `[1, [[3, [[5, []], [6, []]]], [2, []], [4, []]]]`
- Output: `3`

**Example 2**

- Input tree: `[7, []]`
- Output: `1`

**Example 3**

- Input tree: `null`
- Output: `0`
