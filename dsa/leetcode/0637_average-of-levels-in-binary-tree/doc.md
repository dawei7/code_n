# Average of Levels in Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 637 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/average-of-levels-in-binary-tree/) |

## Problem Description
### Goal
Given the root of a nonempty binary tree, compute the average value of the nodes on each level. The root forms the first level, its existing children form the next level, and so on from top to bottom.

Return an array of floating-point averages in level order. For each depth, sum only the values of nodes actually present at that level and divide by that level's node count; missing children are not zero-valued nodes. Answers within $10^{-5}$ of the exact average are accepted.

### Function Contract
**Inputs**

- `root`: the root of a binary tree, represented by a level-order list with null markers in app cases

**Return value**

- A list of floating-point averages, one for each tree level in top-to-bottom order

### Examples
**Example 1**

- Input: `root = [3,9,20,null,null,15,7]`
- Output: `[3.0,14.5,11.0]`

**Example 2**

- Input: `root = [1]`
- Output: `[1.0]`

**Example 3**

- Input: `root = [1,2,3,4,5,6,7]`
- Output: `[1.0,2.5,5.5]`
