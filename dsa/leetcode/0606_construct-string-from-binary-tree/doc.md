# Construct String from Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 606 |
| Difficulty | Medium |
| Topics | String, Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/construct-string-from-binary-tree/) |

## Problem Description
### Goal
Given the root of a binary tree, construct its string representation from a preorder traversal. Write each node as its integer value, then represent each nonempty child subtree inside parentheses immediately after its parent.

Omit empty parenthesis pairs whenever doing so does not change the one-to-one mapping between the string and the original tree. In particular, omit an empty right child, but write `()` for an empty left child when the node has a right child so that the right subtree cannot be mistaken for a left subtree. Return the complete representation without spaces or null markers.

### Function Contract
**Inputs**

- `root: TreeNode | None`: the binary-tree root

**Return value**

- A preorder string containing each node value
- A nonempty child is enclosed in parentheses
- An empty left child is written as `()` when a right child exists
- An empty right child is always omitted

### Examples
**Example 1**

- Input: `root = [1,2,3,4]`
- Output: `"1(2(4))(3)"`

**Example 2**

- Input: `root = [1,2,3,null,4]`
- Output: `"1(2()(4))(3)"`

**Example 3**

- Input: `root = [1,null,2]`
- Output: `"1()(2)"`
