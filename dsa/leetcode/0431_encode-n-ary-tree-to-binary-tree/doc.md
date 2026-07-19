# Encode N-ary Tree to Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 431 |
| Difficulty | Hard |
| Topics | Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/) |

## Problem Description
### Goal
Design a codec that maps an N-ary tree, whose nodes may have any number of ordered children, into a binary tree. The binary representation must retain every value and enough structural information to distinguish parent-child relationships from sibling order.

`encode(root)` returns the binary representation, and `decode(data)` must reconstruct an N-ary tree equivalent to the original. Empty trees must map back to empty trees, leaves must remain leaves, and children must reappear in their original order. The particular reversible convention is implementation-defined, but the round trip cannot omit nodes or rely on external state.

### Function Contract
**Inputs**

- `tree`: the app representation of an N-ary node as `[value, children]`, recursively, or `None` for an empty tree

**Return value**

- Encode the N-ary structure as a binary structure, decode it, and return the reconstructed nested representation. The native artifact exposes the required `Codec.encode(root)` and `Codec.decode(data)` methods.

### Examples
**Example 1**

- Input: `tree = [1, [[3, [[5, []], [6, []]]], [2, []], [4, []]]]`
- Output: `[1, [[3, [[5, []], [6, []]]], [2, []], [4, []]]]`

**Example 2**

- Input: `tree = [7, []]`
- Output: `[7, []]`

**Example 3**

- Input: `tree = None`
- Output: `None`
