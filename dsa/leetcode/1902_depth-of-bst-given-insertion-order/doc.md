# Depth of BST Given Insertion Order

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1902 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Tree, Binary Search Tree, Binary Tree, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Depth of BST Given Insertion Order](https://leetcode.com/problems/depth-of-bst-given-insertion-order/) |

## Problem Description

### Goal

`order` is a permutation of the integers from $1$ through $n$ and describes how those keys are inserted into an initially empty binary search tree. The first key becomes the root. Each later key follows left links while it is smaller than the current node and right links while it is larger, becoming a leaf at the first empty child position.

Return the resulting tree's depth: the number of nodes on its longest root-to-leaf path. The root alone has depth one. The task asks only for this depth; the tree does not need to be returned.

### Function Contract

**Inputs**

- `order`: a permutation of every integer from $1$ through $n$, where $1 \le n \le 10^5$.

**Return value**

Return the maximum number of nodes on a root-to-leaf path in the BST produced by inserting the keys in the given order.

### Examples

**Example 1**

- Input: `order = [2, 1, 4, 3]`
- Output: `3`
- Explanation: One longest path is `2 -> 4 -> 3`.

**Example 2**

- Input: `order = [2, 1, 3, 4]`
- Output: `3`
- Explanation: The path `2 -> 3 -> 4` has three nodes.

**Example 3**

- Input: `order = [1, 2, 3, 4]`
- Output: `4`
- Explanation: Increasing insertion order creates a right-only chain.
