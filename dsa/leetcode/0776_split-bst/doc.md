# Split BST

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 776 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Binary Search Tree, Recursion, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/split-bst/) |

## Problem Description

### Goal

Given the root of a binary search tree with distinct values and an integer `target`, split the tree into two binary search trees. The first must contain every original node whose value is less than or equal to `target`, and the second every node whose value is greater.

Preserve as much of the original parent-descendant structure as the split permits, changing only links needed to separate the value groups. Return the two component roots as `[small, large]`; either root may be null, and `target` does not need to occur in the input tree.

### Function Contract

**Inputs**

- `root`: the root node of a binary search tree with distinct values, represented in cases by level order.
- `target`: the split threshold, which need not occur in the tree.

**Return value**

- A two-element list `[small, large]` of component entry nodes, with all values `<= target` in `small` and all values `> target` in `large`; either entry may be `None`.

### Examples

**Example 1**

- Input: `root = [4,2,6,1,3,5,7]`, `target = 2`
- Output: `[[2,1],[4,3,6,null,null,5,7]]`
- Explanation: Node `3` becomes the left child of `4`, while `2` retains its left subtree.

**Example 2**

- Input: `root = [4,2,6,1,3,5,7]`, `target = 4`
- Output: `[[4,2,null,1,3],[6,5,7]]`
- Explanation: Splitting at the original root detaches its greater right component.

**Example 3**

- Input: `root = [2,1,3]`, `target = 0`
- Output: `[[],[2,1,3]]`
- Explanation: Every value is greater than the target.
