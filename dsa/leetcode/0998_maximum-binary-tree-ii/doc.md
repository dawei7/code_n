# Maximum Binary Tree II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 998 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/maximum-binary-tree-ii/) |

## Problem Description

### Goal

A maximum tree is a binary tree in which each node's value is greater than every other value in its subtree. The given `root` was constructed from an unknown list `a`: choose the largest list element as the root, recursively construct the left child from the elements before that maximum, and recursively construct the right child from the elements after it.

Create `b` by appending `val` to the end of `a`. All values in `b` are guaranteed to be unique. Although `a` itself is unavailable, return the maximum tree that the same recursive construction would produce from `b`.

### Function Contract

**Inputs**

- `root`: the root of a maximum binary tree with $N$ unique nodes, where $1\le N\le100$ and every node value lies from $1$ through $100$.
- `val`: a value from $1$ through $100$ that does not occur in the tree.

Let $H$ be the height of the tree's right spine.

**Return value**

- The root of the maximum tree obtained after appending `val` to the source list.

### Examples

**Example 1**

- Input: `root = [4, 1, 3, null, null, 2], val = 5`
- Output: `[5, 4, null, 1, 3, null, null, 2]`
- Explanation: Appending $5$ makes it the maximum of the entire sequence, so the old tree becomes its left subtree.

**Example 2**

- Input: `root = [5, 2, 4, null, 1], val = 3`
- Output: `[5, 2, 4, null, 1, null, 3]`

**Example 3**

- Input: `root = [5, 2, 3, null, 1], val = 4`
- Output: `[5, 2, 4, null, 1, 3]`
