# Recover a Tree From Preorder Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1028 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [recover-a-tree-from-preorder-traversal](https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/).

### Goal
Reconstruct a binary tree from a preorder traversal string. Each node value is preceded by a number of dashes equal to its depth, with the root at depth `0`. If a node has only one child, that child is the left child.

### Function Contract
**Inputs**

- `traversal`: String encoding preorder node visits with dash depth markers.

**Return value**

Root of the reconstructed binary tree, represented in cOde(n) cases as a level-order list.

### Examples
**Example 1**

- Input: `traversal = "1-2--3--4-5--6--7"`
- Output: `[1, 2, 5, 3, 4, 6, 7]`

**Example 2**

- Input: `traversal = "1-2--3---4-5--6---7"`
- Output: `[1, 2, 5, 3, null, 6, null, 4, null, 7]`

**Example 3**

- Input: `traversal = "1-401--349---90--88"`
- Output: `[1, 401, null, 349, 88, 90]`

---

## Solution
### Approach
Parse the string into `(depth, value)` pairs. A stack tracks the path from the root to the most recently parsed node. Before attaching a new node, pop until the stack length equals the new node's depth; the stack top is then its parent.

Because the traversal is preorder, the first child encountered for a parent is its left child and the second child is its right child. Push the new node onto the stack and continue parsing.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of `traversal`.
- **Space Complexity**: `O(h)` for the stack of ancestors, where `h` is the tree height.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
