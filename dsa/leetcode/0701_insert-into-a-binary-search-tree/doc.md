# Insert into a Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 701 |
| Difficulty | Medium |
| Topics | Tree, Binary Search Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/insert-into-a-binary-search-tree/) |

## Problem Description
### Goal
Given the root of a binary search tree and a value `val` that does not already occur in it, insert one new node containing `val` while preserving the binary-search-tree ordering.

Return the root after insertion. More than one resulting shape may be valid as long as every original node remains, exactly one new node is added, and the final tree is still a binary search tree; you may return any valid insertion result.

### Function Contract
**Inputs**

- `root`: the root of the current binary search tree, represented in cases by level-order values
- `val`: a value absent from the tree

**Return value**

- The root of the updated binary search tree containing every original node plus one new node with value `val`

### Examples
**Example 1**

- Input: `root = [4,2,7,1,3], val = 5`
- Output: `[4,2,7,1,3,5]`

**Example 2**

- Input: `root = [2,1,3], val = 0`
- Output: `[2,1,3,0]`

**Example 3**

- Input: `root = [], val = 5`
- Output: `[5]`
