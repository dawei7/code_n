# Binary Search Tree to Greater Sum Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1038 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [binary-search-tree-to-greater-sum-tree](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/).

### Goal
Convert a binary search tree into a greater sum tree. Each node's new value should be its original value plus the sum of all original node values greater than it.

### Function Contract
**Inputs**

- `root`: Root of a binary search tree, represented in cOde(n) cases as a level-order list.

**Return value**

Root of the same tree after values are updated in place.

### Examples
**Example 1**

- Input: `root = [4, 1, 6, 0, 2, 5, 7, null, null, null, 3, null, null, null, 8]`
- Output: `[30, 36, 21, 36, 35, 26, 15, null, null, null, 33, null, null, null, 8]`

**Example 2**

- Input: `root = [0, null, 1]`
- Output: `[1, null, 1]`

**Example 3**

- Input: `root = [3, 2, 4, 1]`
- Output: `[7, 9, 4, 10]`

---

## Solution
### Approach
A BST visited in reverse inorder order yields values from largest to smallest. Keep a running sum of all values already visited. When visiting a node, add its original value to the running sum and replace the node's value with that sum.

The traversal order is right subtree, current node, left subtree.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of nodes.
- **Space Complexity**: `O(h)` for recursion depth, where `h` is the tree height.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
