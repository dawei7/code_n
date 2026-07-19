# Correct a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1660 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/correct-a-binary-tree/) |

## Problem Description
### Goal
A binary tree contains exactly one invalid node. Instead of a normal right child, that node's `right` pointer incorrectly references another node at the same depth that lies to its right. Remove the invalid node and its entire genuine descendant subtree while preserving the node reached by the erroneous pointer and every other valid part of the tree.

For serialized custom tests, `root` describes the tree before corruption. The node whose value is `fromNode` initially has no right child; after parsing, its `right` pointer is redirected to the same-depth node whose value is `toNode`. These two values are supplied only to construct the test and are not arguments of LeetCode's native `correctBinaryTree(root)` method.

### Function Contract
**Inputs**

- `root`: the root node of a binary tree containing between 3 and $10^4$ uniquely valued nodes, represented by level order in local cases, with each value in $[-10^9,10^9]$.
- `fromNode`: the unique value of the invalid node used by the local custom-test adapter.
- `toNode`: the unique value of a node at the same depth and to the right of `fromNode`.

The original parsed node identified by `fromNode` has `right = null`; the judge replaces that pointer with the node identified by `toNode` before invoking the native method. Let $N$ be the number of tree nodes.

**Return value**

Return the corrected tree root after removing the invalid node and all of its genuine descendants. The incorrectly referenced `toNode` subtree remains in its original location.

### Examples
**Example 1**

- Input: `root = [1, 2, 3], fromNode = 2, toNode = 3`
- Output: `[1, null, 3]`

Node 2 is invalid, so its parent link is cleared.

**Example 2**

- Input: `root = [8, 3, 1, 7, null, 9, 4, 2, null, null, null, 5, 6], fromNode = 7, toNode = 4`
- Output: `[8, 3, 1, null, null, 9, 4, null, null, 5, 6]`

Removing invalid node 7 also removes its genuine descendant 2, while node 4 remains attached beneath node 1.
