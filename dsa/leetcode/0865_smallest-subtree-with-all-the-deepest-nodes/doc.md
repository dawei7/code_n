# Smallest Subtree with all the Deepest Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 865 |
| Difficulty | Medium |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/) |

## Problem Description
### Goal
Given the root of a binary tree, define a node's depth as its shortest distance in edges from the root. A deepest node is any node whose depth is as large as possible in the entire tree. Find the smallest subtree that contains every deepest node.

The subtree rooted at a node consists of that node and all its descendants. Return the root node of the qualifying subtree. If only one node is deepest, its one-node subtree is the answer; when deepest nodes lie in different branches, the answer is their lowest shared ancestor.

### Function Contract
**Inputs**

- `root`: the root of a non-empty binary tree containing $n$ nodes, where $1 \leq n \leq 500$.

Every node value is unique and lies in $[0,500]$. Let $h$ be the tree height measured as the maximum number of nodes on a root-to-leaf path.

**Return value**

Return the `TreeNode` that roots the smallest subtree containing all nodes at maximum depth.

### Examples
**Example 1**

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4]`
- Output: `[2,7,4]`

Nodes `7` and `4` are deepest, and node `2` roots their smallest common subtree.

**Example 2**

- Input: `root = [1]`
- Output: `[1]`

**Example 3**

- Input: `root = [0,1,3,null,2]`
- Output: `[2]`

Node `2` is the only deepest node, so its own subtree is smallest.
