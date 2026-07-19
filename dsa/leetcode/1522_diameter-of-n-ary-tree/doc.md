# Diameter of N-Ary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1522 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/diameter-of-n-ary-tree/) |

## Problem Description
### Goal

Given the root of an N-ary tree, find the tree's diameter: the greatest number of edges on a simple path between any two nodes. The longest path may pass through the supplied root, through another internal node, or end at the root.

The source tree contains between 1 and $10^4$ nodes and may have depth up to 1000. Return only the diameter length in edges, not the endpoints or the path itself.

### Function Contract
**Inputs**

Let $n$ be the node count.

- `tree`: The app-local tree as $n$ records `[value, child_values]`. Every non-root value appears in exactly one child list, values are unique, and $1 \leq n \leq 10^4$.
- The equivalent native interface receives the actual N-ary root node, whose `children` list contains child nodes.
- The maximum root-to-leaf depth is 1000.

**Return value**

Return the maximum number of edges on a path between any two nodes. A one-node tree has diameter 0.

### Examples
**Example 1**

- Input: `tree = [[1, [3, 2, 4]], [3, [5, 6]], [2, []], [4, []], [5, []], [6, []]]`
- Output: `3`
- Explanation: A longest path joins node 5 or 6 to node 2 or 4 using three edges.

**Example 2**

- Input: `tree = [[1, [2]], [2, [3, 4]], [3, [5]], [4, []], [5, [6]], [6, []]]`
- Output: `4`
- Explanation: The path from node 6 to node 4 contains four edges.

**Example 3**

- Input: `tree = [[7, []]]`
- Output: `0`
