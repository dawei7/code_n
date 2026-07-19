# Binary Tree Vertical Order Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 314 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search, Sorting, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-vertical-order-traversal/) |

## Problem Description
### Goal
Assign the root of a binary tree to column zero. A left child is one column smaller than its parent, and a right child is one column larger. Group every node value by the column reached through these offsets.

Return columns from the smallest coordinate to the largest. Inside each column, list nodes from top to bottom; when nodes share both row and column, preserve their natural left-to-right level-order appearance. Include each existing node once and no missing placeholders. An empty tree returns an empty list, while repeated values remain separate entries according to their positions.

### Function Contract
**Inputs**

- `root`: the root of a binary tree, encoded as a level-order list in app cases

**Return value**

A list of vertical columns, each containing its node values in the required traversal order.

### Examples
**Example 1**

- Input: `root = [3,9,20,null,null,15,7]`
- Output: `[[9],[3,15],[20],[7]]`

**Example 2**

- Input: `root = [3,9,8,4,0,1,7]`
- Output: `[[4],[9],[3,0,1],[8],[7]]`

**Example 3**

- Input: `root = []`
- Output: `[]`
