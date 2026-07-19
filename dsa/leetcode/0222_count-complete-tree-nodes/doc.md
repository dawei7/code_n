# Count Complete Tree Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 222 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Binary Search, Bit Manipulation, Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-complete-tree-nodes/) |

## Problem Description
### Goal
Given the root of a complete binary tree, return its total number of nodes. In a complete tree, every level except possibly the last is full, and nodes on the last level occupy the leftmost available positions without gaps.

Count every existing node exactly once and return `0` for an empty tree. Use the completeness guarantee to run faster than a traversal that visits all `n` nodes; the required bound is logarithmic height work across logarithmically many levels. The result concerns actual nodes only, so absent positions on the partially filled final level are not counted.

### Function Contract
**Inputs**

- `root`: the root of a complete binary tree

**Return value**

The total node count.

### Examples
**Example 1**

- Input: `[1,2,3,4,5,6]`
- Output: `6`

**Example 2**

- Input: `[]`
- Output: `0`

**Example 3**

- Input: `[1]`
- Output: `1`
