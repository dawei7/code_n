# Lowest Common Ancestor of a Binary Tree II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1644 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/) |

## Problem Description

### Goal

Given the root of a binary tree and two distinct target nodes `p` and `q`, return their lowest common ancestor. The lowest common ancestor is the deepest node whose subtree contains both targets; a node counts as its own descendant.

Unlike the standard version of this problem, either target may be absent from the tree. Return `null` unless both `p` and `q` exist. Every node value in the tree is unique.

### Function Contract

**Inputs**

- `root`: the root of a binary tree containing $n$ nodes, where $1 \le n \le 10^4$.
- Every node value is unique and lies between $-10^9$ and $10^9$.
- `p`: the first target `TreeNode`; it may not belong to `root`.
- `q`: the distinct second target `TreeNode`; it may not belong to `root`.

JSON fixtures use each target's unique value to recover the corresponding object from `root` before the call. An absent value becomes a missing target represented to the solution as `null`.

**Return value**

Return the lowest-common-ancestor `TreeNode` when both targets occur in the tree; otherwise return `null`. The result display uses the returned node's value.

### Examples

#### Example 1

- **Input:** `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1`
- **Output:** `3`

The targets lie in different subtrees of the root.

#### Example 2

- **Input:** `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4`
- **Output:** `5`

Node 5 is an ancestor of node 4 and also counts as its own descendant.

#### Example 3

- **Input:** `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10`
- **Output:** `null`

The value 10 is absent, so no result may be returned even though node 5 exists.
