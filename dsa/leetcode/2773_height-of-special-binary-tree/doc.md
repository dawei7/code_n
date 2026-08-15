# Height of Special Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2773 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [2773. Height of Special Binary Tree](https://leetcode.com/problems/height-of-special-binary-tree/) |

## Problem Description

### Goal

You are given the root of a special binary tree containing $n$ uniquely numbered nodes. Let its original leaves, in their numbered order, be $b_1,b_2,\ldots,b_k$. The tree stores an additional cyclic link among these leaves: the right pointer of $b_i$ refers to $b_{i+1}$, wrapping from $b_k$ to $b_1$, while its left pointer refers to $b_{i-1}$, wrapping from $b_1$ to $b_k$.

Those neighbor pointers do not create deeper tree levels; they replace the otherwise empty child pointers of the leaves. Return the height of the underlying binary tree, defined as the number of edges on the longest path from the root to any node. The leaf cycle must therefore be recognized and excluded from the descendant traversal.

### Function Contract

**Inputs**

- `root`: The root node of the special binary tree. JSON fixtures represent the underlying tree in level order and omit the implied cyclic links between its leaves.

The tree satisfies $2 \le n \le 10^4$. Every node value lies from $1$ through $n$, and all node values are distinct. Let $h$ denote the requested height.

**Return value**

Return $h$, the greatest number of original tree edges from `root` to any node.

### Examples

#### Example 1

- **Input:** `root = [1, 2, 3, null, null, 4, 5]`
- **Output:** `2`
- **Explanation:** Nodes `2`, `4`, and `5` form the leaf cycle, but each is two original edges or fewer from the root.

#### Example 2

- **Input:** `root = [1, 2]`
- **Output:** `1`
- **Explanation:** The tree has one original leaf and one edge from the root to that leaf.

#### Example 3

- **Input:** `root = [1, 2, 3, null, null, 4, null, 5, 6]`
- **Output:** `3`
- **Explanation:** The deepest original nodes are three edges below the root.
