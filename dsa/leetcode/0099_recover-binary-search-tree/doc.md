# Recover Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 99 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/recover-binary-search-tree/) |

## Problem Description
### Goal
You are given a binary search tree whose structure is intact but whose values were corrupted by swapping exactly two nodes. As a result, its inorder values are no longer strictly increasing in the proper positions.

Restore the binary search tree by swapping those two values back. Modify the existing tree in place, preserve every parent-child link, and return no value in the native contract. The misplaced nodes may be adjacent or far apart in inorder order, including the root or leaves.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

`None`; mutate the `TreeNode` values in place so the original root represents the recovered BST.

### Examples
**Example 1**

- Input: `root = [1, 3, null, null, 2]`
- Output tree: `[3, 1, null, null, 2]`

**Example 2**

- Input: `root = [3, 1, 4, null, null, 2]`
- Output tree: `[2, 1, 4, null, null, 3]`

**Example 3**

- Input: `root = [2, 3, 1]`
- Output tree: `[2, 1, 3]`
