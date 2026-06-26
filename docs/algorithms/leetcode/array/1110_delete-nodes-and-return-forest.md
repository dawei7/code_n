# Delete Nodes And Return Forest

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1110 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Tree, Depth-First Search, Binary Tree |
| Official Link | [delete-nodes-and-return-forest](https://leetcode.com/problems/delete-nodes-and-return-forest/) |

## Problem Description & Examples
### Goal
Remove every tree node whose value appears in `to_delete`. Return the roots of all remaining connected components.

### Function Contract
**Inputs**

- `root`: root of a binary tree with unique node values.
- `to_delete`: values of nodes to remove.

**Return value**

A list of root nodes for the forest left after deletion. The order is not important.

### Examples
**Example 1**

- Input: `root = [1,2,3,4,5,6,7]`, `to_delete = [3,5]`
- Output: roots representing `[[1,2,null,4],[6],[7]]`

**Example 2**

- Input: `root = [1,2,4,null,3]`, `to_delete = [2]`
- Output: roots representing `[[1,null,4],[3]]`

**Example 3**

- Input: `root = [1]`, `to_delete = [1]`
- Output: `[]`

---

## Underlying Base Algorithm(s)
Postorder depth-first search with set membership.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` for recursion depth, delete set, and output in the worst case.
