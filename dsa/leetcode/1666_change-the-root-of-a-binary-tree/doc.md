# Change the Root of a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1666 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/change-the-root-of-a-binary-tree/) |

## Problem Description
### Goal
Every node in a binary tree has `left`, `right`, and `parent` pointers. Given the original `root` and an existing leaf node, restructure the tree so that `leaf` becomes the new root while preserving every node and every subtree not on the leaf-to-root path.

For each path node `cur` other than the old root, move an existing left child to `cur.right`, make `cur`'s former parent its new left child, and clear the former parent's link back to `cur`. The contract guarantees each such `cur` has at most one child when processed. All child and `parent` pointers must agree in the returned tree.

### Function Contract
**Inputs**

- `root`: the root node of a parent-linked binary tree containing between 2 and 100 uniquely valued nodes.
- `leaf`: a leaf node in that same tree, represented by a shared-tree target fixture in local cases.

Node values lie in $[-10^9,10^9]$. Let $h$ be the number of nodes on the path from `leaf` to `root`.

**Return value**

Return the supplied leaf node as the root of the correctly rerooted tree, with its `parent` set to `null`.

### Examples
**Example 1**

- Input: `root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], leaf = 7`
- Output: `[7, 2, null, 5, 4, 3, 6, null, null, null, 1, null, null, 0, 8]`

**Example 2**

- Input: `root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], leaf = 0`
- Output: `[0, 1, null, 3, 8, 5, null, null, null, 6, 2, null, null, 7, 4]`
