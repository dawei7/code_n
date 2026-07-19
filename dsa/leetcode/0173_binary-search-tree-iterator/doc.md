# Binary Search Tree Iterator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 173 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Stack, Tree, Design, Binary Search Tree, Binary Tree, Iterator |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-search-tree-iterator/) |

## Problem Description
### Goal
Design an iterator over a binary search tree that exposes its nodes in inorder, which yields values from smallest to largest under the tree's ordering. Constructing the iterator establishes its initial position before any value has been returned.

`next()` must advance and return the next smallest remaining value, while `hasNext()` reports whether such a value exists without consuming it. Process repeated calls against the same iterator state; `next()` is invoked only when another node is available. Avoid materializing the complete traversal: use $O(h)$ memory for tree height `h`, with construction and operations meeting the required amortized efficiency.

### Function Contract
**Inputs**

- `root`: a `TreeNode` encoded as a level-order list
- `operations`: calls beginning with `BSTIterator`, followed by `next` and `hasNext`

**Return value**

A result list aligned with operations: `None` for construction, the next integer for next, and a boolean for hasNext.

### Examples
**Example 1**

- Input: `root = [7,3,15,null,null,9,20]`
- Output sequence from next calls: `3,7,9,15,20`

**Example 2**

- Input: `root = [1]`
- Output: first hasNext is true, next is `1`, final hasNext is false

**Example 3**

- Input: `root = []`
- Output: hasNext is false
