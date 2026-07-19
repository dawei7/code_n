# Sum of Left Leaves

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 404 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-left-leaves/) |

## Problem Description
### Goal
Given the root of a binary tree, identify leaves that are reached through the left-child pointer of their parent. A leaf must have neither a left nor a right child; an internal left child does not contribute merely because of its position.

Return the sum of all such left-leaf values. Negative values subtract normally, and leaves in different branches are counted independently. The root itself has no parent and is therefore not a left leaf when it is the tree's only node. A tree with no qualifying left leaves returns `0`.

### Function Contract
**Inputs**

- `root`: the root of a binary tree, or `None`

**Return value**

- Return the sum of values from nodes that have no children and are reached through a parent's left edge.

### Examples
**Example 1**

- Input: `root = [3,9,20,null,null,15,7]`
- Output: `24`

**Example 2**

- Input: `root = [1]`
- Output: `0`

**Example 3**

- Input: `root = [1,2,3,4,5]`
- Output: `4`
