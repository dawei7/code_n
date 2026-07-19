# Univalued Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 965 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [univalued-binary-tree](https://leetcode.com/problems/univalued-binary-tree/) |

## Problem Description

### Goal

A binary tree is called uni-valued when every node in the entire tree stores the same value. Given the tree's `root`, determine whether it has this property.

Return `true` only if every existing node agrees with the root's value; otherwise return `false`. Missing children are structural gaps rather than nodes and therefore contribute no value to compare. The input always contains at least one node, so `root` itself supplies the required reference value.

### Function Contract

**Inputs**

- `root`: the root of a binary tree containing $N$ nodes and having height $H$.
- The node count satisfies $1 \le N \le 100$.
- Every node value satisfies $0 \le \texttt{Node.val} < 100$.
- In serialized cases, the tree is represented in level order and `null` denotes a missing child.

**Return value**

Return `true` if all $N$ nodes have one common value; otherwise return `false`.

### Examples

**Example 1**

- Input: `root = [1,1,1,1,1,null,1]`
- Output: `true`

**Example 2**

- Input: `root = [2,2,2,5,2]`
- Output: `false`
