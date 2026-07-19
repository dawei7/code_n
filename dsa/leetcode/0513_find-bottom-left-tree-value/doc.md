# Find Bottom Left Tree Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 513 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/find-bottom-left-tree-value/) |

## Problem Description
### Goal
Given the root of a nonempty binary tree, assign the root to depth zero and increase depth by one along every child edge. The last row is the greatest depth containing at least one node.

Return the value of the leftmost node in that last row. Leftmost is determined by the tree's structural left-to-right order, not by the smallest numeric value. If only one node occupies the deepest level, return that node's value; if the tree contains only its root, the root is both deepest and leftmost.

### Function Contract
**Inputs**

- `root`: the root of a nonempty binary tree

**Return value**

- The value stored in the first node from the left on the tree's maximum-depth level

### Examples
**Example 1**

- Input: `root = [2, 1, 3]`
- Output: `1`

**Example 2**

- Input: `root = [1, 2, 3, 4, null, 5, 6, null, null, 7]`
- Output: `7`

**Example 3**

- Input: `root = [1]`
- Output: `1`
