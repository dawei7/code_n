# Maximum Width of Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 662 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-width-of-binary-tree/) |

## Problem Description
### Goal
Given the root of a binary tree, return its maximum width over all levels. The width of one level is the number of complete-tree positions from its leftmost non-null node through its rightmost non-null node, including null positions between those two end-nodes.

Do not count absent positions outside the two end-nodes. Evaluate every depth and return the greatest width found; sparse descendants can therefore create a width larger than the number of actual nodes on that level. The answer is guaranteed to fit in a signed 32-bit integer.

### Function Contract
**Inputs**

- `root`: the non-null root node of a binary tree

**Return value**

- The maximum positional width of any tree level

### Examples
**Example 1**

- Input: `root = [1, 3, 2, 5, 3, null, 9]`
- Output: `4`

**Example 2**

- Input: `root = [1, 3, 2, 5, null, null, 9, 6, null, 7]`
- Output: `7`

**Example 3**

- Input: `root = [1, 3, 2, 5]`
- Output: `2`
