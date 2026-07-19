# Binary Tree Upside Down

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 156 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-upside-down/) |

## Problem Description
### Goal
Given a binary tree in which every right child is either absent or a leaf paired with a left sibling, turn the tree upside down along its left-child spine. The original leftmost node becomes the new root, and each former parent moves below its former left child.

For every flipped relationship, the former right sibling becomes the new node's left child and the former parent becomes its right child. Rewire the existing nodes without losing subtrees or leaving backward links into the old structure, then return the new root. An empty or single-node tree remains unchanged, and the original root becomes the rightmost descendant after a nontrivial flip.

### Function Contract
**Inputs**

- `root`: a `TreeNode` encoded as a level-order list; every original right child is either absent or paired with a left sibling and has no children

**Return value**

The root `TreeNode` of the rewired upside-down binary tree.

### Examples
**Example 1**

- Input: `root = [1,2,3,4,5]`
- Output: `[4,5,2,null,null,3,1]`

**Example 2**

- Input: `root = []`
- Output: `[]`

**Example 3**

- Input: `root = [1]`
- Output: `[1]`
