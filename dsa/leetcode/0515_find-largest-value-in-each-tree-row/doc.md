# Find Largest Value in Each Tree Row

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 515 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/find-largest-value-in-each-tree-row/) |

## Problem Description
### Goal
Given the root of a binary tree, group node values by their zero-based row or depth. The root occupies row zero, its children occupy row one, and each later row contains the existing children of nodes in the preceding row.

Return an array containing the largest value in each occupied row, ordered from the root row downward. Negative values compare normally, missing children add no placeholders, and each row contributes exactly one maximum. If the tree is empty, return an empty array; the function returns values rather than the nodes or their positions.

### Function Contract
**Inputs**

- `root`: the root of a binary tree, or `null`

**Return value**

- One maximum value per nonempty tree level, from shallowest to deepest

### Examples
**Example 1**

- Input: `root = [1, 3, 2, 5, 3, null, 9]`
- Output: `[1, 3, 9]`

**Example 2**

- Input: `root = [1, 2, 3]`
- Output: `[1, 3]`

**Example 3**

- Input: `root = [1]`
- Output: `[1]`
