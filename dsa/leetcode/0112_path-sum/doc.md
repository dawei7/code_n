# Path Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 112 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/path-sum/) |

## Problem Description
### Goal
Given the root of a binary tree and an integer `targetSum`, decide whether one complete downward path has exactly that total. Every candidate path must begin at the root, follow parent-to-child links, and stop at a leaf with no children.

Return `True` when the sum of the node values on at least one such root-to-leaf path equals `targetSum`; otherwise return `False`. A matching prefix that stops at an internal node does not qualify, and a path may pass through negative, zero, or positive values. An empty tree contains no valid path, even when the requested sum is zero.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases
- `targetSum`: the required sum of one complete root-to-leaf path

**Return value**

`True` if at least one qualifying root-to-leaf path exists; otherwise `False`.

### Examples
**Example 1**

- Input: `root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1], targetSum = 22`
- Output: `True`

**Example 2**

- Input: `root = [1, 2, 3], targetSum = 5`
- Output: `False`

**Example 3**

- Input: `root = [], targetSum = 0`
- Output: `False`
