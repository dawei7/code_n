# Find Distance in a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1740 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-distance-in-a-binary-tree/) |

## Problem Description

### Goal

You are given the root of a binary tree whose node values are unique, together with two values `p` and `q` that both occur in the tree. The distance between two nodes is the number of edges on the shortest route connecting them.

Return the distance between the node whose value is `p` and the node whose value is `q`. The two values may identify the same node, and neither target is required to be a leaf.

### Function Contract

**Inputs**

- `root`: the root of a nonempty binary tree with unique integer node values.
- `p`: a value present in the tree.
- `q`: another value present in the tree; it may equal `p`.

Let $N$ be the number of nodes in the tree.

**Return value**

- Return the number of tree edges on the unique path between the two target nodes.

### Examples

**Example 1**

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 0`
- Output: `3`
- Explanation: The route is `5 -> 3 -> 1 -> 0`.

**Example 2**

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 7`
- Output: `2`
- Explanation: The route is `5 -> 2 -> 7`.

**Example 3**

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 5`
- Output: `0`
- Explanation: A node has distance zero from itself.
