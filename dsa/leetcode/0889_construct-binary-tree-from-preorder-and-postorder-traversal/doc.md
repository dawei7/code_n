# Construct Binary Tree from Preorder and Postorder Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 889 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Divide and Conquer, Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/) |

## Problem Description
### Goal
Two integer arrays describe the same binary tree with distinct node values. `preorder` lists each root before its left and right subtrees, while `postorder` lists both subtrees before their root.

Reconstruct and return a binary tree whose preorder traversal is exactly `preorder` and whose postorder traversal is exactly `postorder`. The traversals are guaranteed to be mutually valid. They may not determine a unique tree—for example, the side of a single child is ambiguous—and any tree matching both arrays is acceptable.

### Function Contract
Let $n=\lvert\texttt{preorder}\rvert=\lvert\texttt{postorder}\rvert$.

**Inputs**

- `preorder`: the preorder traversal of $n$ distinct node values, where $1 \leq n \leq 30$ and every value lies between $1$ and $n$.
- `postorder`: the postorder traversal of the same binary tree, containing the same $n$ distinct values.

**Return value**

Return the root of any binary tree whose preorder and postorder traversals equal the given arrays.

### Examples
**Example 1**

- Input: `preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]`
- Output: `[1,2,3,4,5,6,7]`

**Example 2**

- Input: `preorder = [1], postorder = [1]`
- Output: `[1]`

**Example 3**

- Input: `preorder = [1,2], postorder = [2,1]`
- Output: `[1,2]`

`[1,null,2]` is also valid because both possible child orientations have the same two traversals.
