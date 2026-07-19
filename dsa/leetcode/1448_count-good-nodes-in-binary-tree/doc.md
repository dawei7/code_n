# Count Good Nodes in Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1448 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) |

## Problem Description
### Goal

A node in a binary tree is good when no node on the path from the root to that
node has a value greater than the node's own value. The path includes both the
root and the node itself. Equality is allowed, so a node whose value ties the
largest earlier value on its path is good.

Given the root of a non-empty binary tree, return the total number of good
nodes. The root is always good because its root-to-root path contains no other
value that could exceed it.

### Function Contract
**Inputs**

- `root`: the root node of a non-empty binary tree containing $n$ nodes, where
  $1 \le n \le 10^5$.
- Each node has an integer `val` satisfying
  $-10^4 \le \text{val} \le 10^4$ and optional `left` and `right` children.
- Serialized examples represent the tree in level order and use `null` for a
  missing child; the function itself receives the constructed root node.

Let $h$ be the height of the tree.

**Return value**

Return the number of nodes whose value is at least every value on their path
from `root`.

### Examples
**Example 1**

- Input: `root = [3, 1, 4, 3, null, 1, 5]`
- Output: `4`
- Explanation: The root, the left leaf with value `3`, and the nodes with
  values `4` and `5` are good. The other nodes have a larger ancestor.

**Example 2**

- Input: `root = [3, 3, null, 4, 2]`
- Output: `3`
- Explanation: Equal value `3` is allowed, and its child `4` is also good;
  the node `2` is below an ancestor with value `3`.

**Example 3**

- Input: `root = [1]`
- Output: `1`
