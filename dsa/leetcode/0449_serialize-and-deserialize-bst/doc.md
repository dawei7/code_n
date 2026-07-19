# Serialize and Deserialize BST

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 449 |
| Difficulty | Medium |
| Topics | String, Tree, Depth-First Search, Breadth-First Search, Design, Binary Search Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/serialize-and-deserialize-bst/) |

## Problem Description
### Goal
Design a codec for binary search trees. `serialize(root)` must encode every node value and enough ordering information to reconstruct the original BST while taking advantage of its strict search-tree structure rather than storing unnecessary generic-tree markers.

`deserialize(data)` returns a tree equivalent in values and structure to the serialized input. Negative values, unbalanced branches, and an empty tree must round-trip correctly. The exact compact string format is implementation-defined but must be unambiguous and self-contained, with no global state shared between calls. The app adapter verifies the complete encode-decode result; the native interface exposes both methods.

### Function Contract
**Inputs**

- `root`: the app's level-order array representation of a binary search tree, using `None` for missing children

**Return value**

- Serialize and deserialize the tree, then return its reconstructed level-order representation. The native artifact exposes `Codec.serialize(root)` and `Codec.deserialize(data)` with `TreeNode` objects.

### Examples
**Example 1**

- Input: `root = [2, 1, 3]`
- Output: `[2, 1, 3]`

**Example 2**

- Input: `root = [5, 3, 6, 2, 4, None, 7]`
- Output: `[5, 3, 6, 2, 4, None, 7]`

**Example 3**

- Input: `root = []`
- Output: `[]`
