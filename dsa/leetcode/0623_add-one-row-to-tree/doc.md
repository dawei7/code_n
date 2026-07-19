# Add One Row to Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 623 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/add-one-row-to-tree/) |

## Problem Description
### Goal
Given the root of a binary tree and integers `val` and `depth`, add a row of nodes whose value is `val` at the specified depth, where the original root is at depth `1`. For every non-null node at depth `depth - 1`, create one new left child and one new right child.

Attach the node's original left subtree below the new left child and its original right subtree below the new right child. If `depth` is `1`, create a new root with value `val` and place the entire original tree as its left subtree. Return the root of the resulting tree.

### Function Contract
**Inputs**

- `root`: the root of a nonempty binary tree
- `val`: the value assigned to every inserted node
- `depth`: the one-based depth where the new row must appear

**Return value**

- The resulting tree root
- At depth one, a new root has the old tree as its left subtree
- Otherwise each old child of a depth-`depth - 1` parent moves below a new node on the same side

### Examples
**Example 1**

- Input: `root = [4,2,6,3,1,5]`, `val = 1`, `depth = 2`
- Output: `[4,1,1,2,null,null,6,3,1,5]`

**Example 2**

- Input: `root = [4,2,null,3,1]`, `val = 1`, `depth = 3`
- Output: `[4,2,null,1,1,3,null,null,1]`
