# Binary Search Tree Iterator II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1586 |
| Difficulty | Medium |
| Topics | Stack, Tree, Design, Binary Search Tree, Binary Tree, Iterator |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-search-tree-iterator-ii/) |

## Problem Description
### Goal

Design a bidirectional iterator over the inorder traversal of a binary search tree. The inorder values form the iterator's ordered sequence. At construction, place the cursor before the smallest value, rather than on a tree node.

`next()` moves the cursor one position to the right and returns that value, while `hasNext()` reports whether such a move is possible. Symmetrically, `prev()` moves one position to the left and returns the new current value, while `hasPrev()` reports whether a value exists on that side. Calls to `next()` and `prev()` are guaranteed to be valid.

The same iterator must preserve its position across an arbitrary valid mixture of forward and backward calls. In particular, moving backward and then forward must revisit already discovered values without advancing the underlying inorder traversal twice.

### Function Contract
**Inputs**

- `root`: The root of a binary search tree with $N$ nodes, encoded for the app as a level-order list.
- `operations`: A sequence of $Q$ calls beginning with `BSTIterator`, followed by valid uses of `next`, `hasNext`, `prev`, and `hasPrev`.

**Return value**

Return one result per operation: `None` for construction, an integer for `next` or `prev`, and a boolean for `hasNext` or `hasPrev`.

### Examples
**Example 1**

- Input: `root = [7,3,15,null,null,9,20], operations = ["BSTIterator","next","next","prev","next"]`
- Output: `[null,3,7,3,7]`

**Example 2**

- Input: `root = [1], operations = ["BSTIterator","hasNext","next","hasPrev","hasNext"]`
- Output: `[null,true,1,false,false]`

**Example 3**

- Input: `root = [2,1,3], operations = ["BSTIterator","next","next","next","prev","next"]`
- Output: `[null,1,2,3,2,3]`
