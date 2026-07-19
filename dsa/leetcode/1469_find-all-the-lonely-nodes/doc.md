# Find All The Lonely Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1469 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/find-all-the-lonely-nodes/) |

## Problem Description
### Goal

In a binary tree, a node is lonely when it is the only child of its parent: its parent has that node on one side and no child on the other side. The root is never lonely because it has no parent, even when it is the only node in the tree.

Given the tree's `root`, collect the values of every lonely node. The values may be returned in any order.

### Function Contract
**Inputs**

- `root`: the root of a nonempty binary tree containing $N$ nodes, where $1 \le N \le 1000$.
- Every node value lies in the inclusive range $[1,10^6]$.

**Return value**

Return an array containing the value of each non-root node whose parent has exactly one child. Result order is unrestricted.

### Examples
**Example 1**

- Input: `root = [1,2,3,null,4]`
- Output: `[4]`
- Explanation: Nodes `2` and `3` are siblings, while node `4` is the only child of node `2`.

**Example 2**

- Input: `root = [7,1,4,6,null,5,3,null,null,null,null,null,2]`
- Output: `[6,2]`
- Explanation: The order `[2,6]` is equally valid.

**Example 3**

- Input: `root = [197]`
- Output: `[]`
- Explanation: A root has no parent and therefore cannot be lonely.
