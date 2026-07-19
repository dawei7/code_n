# Binary Tree Cameras

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 968 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [binary-tree-cameras](https://leetcode.com/problems/binary-tree-cameras/) |

## Problem Description

### Goal

You may install cameras on nodes of a binary tree. A camera monitors the node holding it, that node's parent, and its immediate left and right children. It does not monitor more distant ancestors or descendants.

Choose camera locations so that every node in the tree is monitored, then return the minimum possible number of cameras. Node values carry no information for placement; every node value is `0`, and only the tree structure determines the answer.

### Function Contract

**Inputs**

- `root`: the root of a binary tree with $N$ nodes and height $H$.
- The tree contains between $1$ and $1000$ nodes, inclusive.
- Every node has value `0`.
- Serialized cases use level order, with `null` for a missing child.

**Return value**

Return the minimum number of cameras needed to monitor all $N$ nodes.

### Examples

**Example 1**

- Input: `root = [0,0,null,0,0]`
- Output: `1`

**Example 2**

- Input: `root = [0,0,null,0,null,0,null,null,0]`
- Output: `2`
