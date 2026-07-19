# Complete Binary Tree Inserter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 919 |
| Difficulty | Medium |
| Topics | Tree, Breadth-First Search, Design, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/complete-binary-tree-inserter/) |

## Problem Description
### Goal

A complete binary tree has every level fully occupied except possibly its last, and the nodes on that last level occupy the leftmost positions without gaps. Starting from the root of a non-empty complete binary tree, maintain that shape while new nodes are added.

The data structure supports three operations. Its constructor receives the current root. `insert(val)` creates a node whose value is `val`, places it in the next position of level order so the tree remains complete, and returns the value of the new node's parent. `get_root()` returns the root of the updated tree.

### Function Contract
**Inputs**

- `root`: the root node of an initially complete binary tree containing between $1$ and $1000$ nodes. Cases serialize the tree in level order.
- `operations`: a sequence containing `["insert", val]` and `["get_root"]` operations. Each `val` is between $0$ and $5000$, inclusive, and the sequence contains at most $10^4$ operations.

Let $n$ be the initial number of nodes, $q$ the number of operations, and $m$ the maximum number of nodes present after those operations.

**Return value**

A result list in operation order. An `insert` entry contributes its inserted node's parent value; a `get_root` entry contributes the current tree in level order.

### Examples
**Example 1**

- Input: `root = [1,2], operations = [["insert",3],["insert",4],["get_root"]]`
- Output: `[1,2,[1,2,3,4]]`

**Example 2**

- Input: `root = [1], operations = [["insert",2],["get_root"]]`
- Output: `[1,[1,2]]`

**Example 3**

- Input: `root = [1,2,3,4,5,6], operations = [["insert",7],["insert",8],["get_root"]]`
- Output: `[3,4,[1,2,3,4,5,6,7,8]]`
