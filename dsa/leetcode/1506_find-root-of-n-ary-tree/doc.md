# Find Root of N-Ary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1506 |
| Difficulty | Medium |
| Topics | Hash Table, Bit Manipulation, Tree, Depth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/find-root-of-n-ary-tree/) |

## Problem Description
### Goal

An N-ary tree consists of nodes that each store a unique integer value and a list of zero or more children. Instead of receiving a pointer to the root, you are given an array containing every node object in the tree. The nodes may appear in any order, but their child references still describe the original directed parent-to-child edges.

Find and return the one node that is the root. The input is guaranteed to describe one valid N-ary tree, so exactly one node has no parent. LeetCode's displayed level-order serialization is only a way to construct tests; the array supplied to the function is randomly ordered.

### Function Contract
**Inputs**

Let $N$ be the number of nodes in the tree.

- Native `findRoot(tree)` receives an array of all $N$ node objects in arbitrary order. Every node exposes a unique integer `val` and a `children` list containing references to its children.
- The directed references form one valid N-ary tree: the root has no parent and every other node appears exactly once among all child lists.
- The app-local `solve(tree)` receives the same information as `[value, child_values]` records. Values identify nodes unambiguously because they are unique.

**Return value**

Return the root node. The app-local adapter returns that node's integer value.

### Examples
**Example 1**

- Input: `tree = [[3, [5, 6]], [2, []], [4, []], [1, [3, 2, 4]], [5, []], [6, []]]`
- Output: `1`
- Explanation: Every value except `1` occurs in a child list, so the node with value `1` is the root.

**Example 2**

- Input: `tree = [[8, []], [9, []], [7, [8, 9]]]`
- Output: `7`

**Example 3**

- Input: `tree = [[42, []]]`
- Output: `42`
