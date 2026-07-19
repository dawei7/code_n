# Delete Nodes And Return Forest

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1110 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/delete-nodes-and-return-forest/) |

## Problem Description

### Goal

You are given the `root` of a binary tree in which every node value is distinct, together with the distinct values in `to_delete`. Remove every node whose value appears in that deletion list. Removing a node also removes its links to its parent and children, but any undeleted child begins a separate remaining tree.

The nodes left after all deletions form a forest: a disjoint union of binary trees. Return the root node of every tree in that forest. The roots may be returned in any order, and the surviving parent-child relationships must be preserved.

### Function Contract

**Inputs**

- `root`: the root of a binary tree containing $N$ nodes with distinct values.
- `to_delete`: $D$ distinct node values to remove.

**Return value**

- A list containing exactly the roots of the connected binary trees that remain after all requested nodes are deleted. Root order is unrestricted.

### Examples

**Example 1**

- Input: `root = [1,2,3,4,5,6,7]`, `to_delete = [3,5]`
- Output: `[[1,2,null,4],[6],[7]]`

Deleting node `3` detaches its surviving children `6` and `7` as new roots. Deleting leaf `5` creates no additional tree.

**Example 2**

- Input: `root = [1,2,4,null,3]`, `to_delete = [3]`
- Output: `[[1,2,4]]`
