# Lowest Common Ancestor of Deepest Leaves

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1123 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/) |

## Problem Description

### Goal

Given the `root` of a binary tree, return the lowest common ancestor of all its deepest leaves. A node is a leaf exactly when it has no children. The root has depth $0$, and each child has depth one greater than its parent, so the deepest leaves are those whose depth is maximum among every leaf in the tree.

For a set $S$ of nodes, its lowest common ancestor is the node of greatest depth whose rooted subtree contains every node in $S$. Apply that definition to the complete set of deepest leaves. If only one leaf reaches the maximum depth, that leaf is its own lowest common ancestor. Node values are unique, but the result must be the tree node itself rather than only its value.

### Function Contract

**Inputs**

- `root`: the root of a nonempty binary tree containing $n$ nodes, where $1 \le n \le 1000$; every node value is unique and lies in $[0, 1000]$. cOde(n) serializes the tree as a level-order array with `null` for missing children.

Let $h$ be the tree height measured in nodes on the longest root-to-leaf path.

**Return value**

The `TreeNode` that is the lowest common ancestor of every deepest leaf. cOde(n) serializes the returned node's entire subtree in level order.

### Examples

**Example 1**

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4]`
- Output: `[2,7,4]`
- Explanation: Leaves `7` and `4` are at depth $3$, deeper than leaves `6`, `0`, and `8`; their lowest common ancestor is node `2`.

**Example 2**

- Input: `root = [1]`
- Output: `[1]`
- Explanation: The root is the only and therefore deepest leaf, so it is its own lowest common ancestor.

**Example 3**

- Input: `root = [0,1,3,null,2]`
- Output: `[2]`
- Explanation: Node `2` is the unique deepest leaf.
