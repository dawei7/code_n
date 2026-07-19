# Check Completeness of a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 958 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [check-completeness-of-a-binary-tree](https://leetcode.com/problems/check-completeness-of-a-binary-tree/) |

## Problem Description

### Goal

Given the `root` of a binary tree, determine whether the tree is complete. In a complete binary tree, every level before the last is completely filled.

The last level may contain fewer nodes, but its nodes must occupy the leftmost available positions without any gap before a later node. Equivalently, a level-order listing that includes missing child positions may contain no non-null node after the first missing position. Return whether the supplied tree satisfies this structure.

### Function Contract

Let $N$ be the number of nodes in the tree.

**Inputs**

- `root`: the non-null root of a binary tree containing $1 \le N \le 100$ nodes.
- Every node value is between 1 and 1000; values do not affect completeness.

**Return value**

Return `true` if the tree is complete; otherwise return `false`.

### Examples

**Example 1**

- Input: `root = [1,2,3,4,5,6]`
- Output: `true`
- Explanation: Earlier levels are full, and nodes 4, 5, and 6 occupy the leftmost last-level positions.

**Example 2**

- Input: `root = [1,2,3,4,5,null,7]`
- Output: `false`
- Explanation: Node 7 occurs after an empty position on the last level.
