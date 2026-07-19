# Binary Tree Paths

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 257 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Backtracking, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-paths/) |

## Problem Description
### Goal
Given the root of a binary tree, enumerate every complete path that begins at the root and ends at a leaf. A leaf is a node with no left or right child, so paths must not stop early at internal nodes.

Return each path as a string containing its node values in traversal order, separated by `"->"`. Include every root-to-leaf branch once and return the path strings in any order. Negative and repeated node values should be formatted normally and do not merge distinct structural paths. A one-node tree returns that value alone without an arrow because the root is also a leaf.

### Function Contract
**Inputs**

- `root`: the root of a binary tree

**Return value**

All root-to-leaf paths formatted with `->` between node values; path order is unrestricted.

### Examples
**Example 1**

- Input: `root = [1,2,3,null,5]`
- Output: `["1->2->5","1->3"]`

**Example 2**

- Input: `root = [1]`
- Output: `["1"]`

**Example 3**

- Input: `root = []`
- Output: `[]`
