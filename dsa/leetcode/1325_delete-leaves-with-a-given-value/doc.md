# Delete Leaves With a Given Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1325 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/delete-leaves-with-a-given-value/) |

## Problem Description
### Goal
Given the root of a binary tree and an integer `target`, delete every leaf whose value equals `target`.

Deletion can expose a new qualifying leaf: after its children are removed, a node with value `target` may itself have no children. Continue applying the same rule until no target-valued leaf remains, and return the resulting tree. The root may also be deleted if the cascade makes it a qualifying leaf.

### Function Contract
**Inputs**

- `root`: the root of a nonempty binary tree containing $n$ nodes, where $1\le n\le3000$ and every node value is between 1 and 1000.
- `target`: an integer between 1 and 1000.

**Return value**

The root of the tree after all target-valued leaves, including leaves created by earlier deletions, have been removed; return an empty tree if the root is deleted.

### Examples
**Example 1**

- Input: `root = [1,2,3,2,null,2,4], target = 2`
- Output: `[1,null,3,null,4]`
- Explanation: Removing the original target leaves makes the node 2 below the root a leaf, so it is removed as well.

**Example 2**

- Input: `root = [1,3,3,3,2], target = 3`
- Output: `[1,3,null,null,2]`

**Example 3**

- Input: `root = [1,2,null,2,null,2], target = 2`
- Output: `[1]`
- Explanation: The chain of 2-valued nodes disappears from the bottom upward.
