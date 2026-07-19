# Deepest Leaves Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1302 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/deepest-leaves-sum/) |

## Problem Description
### Goal
Given the root of a nonempty binary tree, identify the leaves at the greatest depth from the root. A leaf is a node with no left or right child, and depth is measured by the number of edges from the root.

Return the sum of the values stored in all leaves at that maximum depth. Shallower leaves do not contribute, even when their values are larger.

### Function Contract
**Inputs**

- `root`: the root of a binary tree containing $n$ nodes, where $1 \le n \le 10^4$ and $1 \le \texttt{Node.val} \le 100$.
- In cOde(n) cases, the tree is serialized in level order with `null` entries for missing children.

**Return value**

The sum of the values of every leaf whose depth is greatest among all leaves in the tree.

### Examples
**Example 1**

- Input: `root = [1,2,3,4,5,null,6,7,null,null,null,null,8]`
- Output: `15`
- Explanation: The deepest leaves are 7 and 8.

**Example 2**

- Input: `root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]`
- Output: `19`
- Explanation: The deepest leaves have values 9, 1, 4, and 5.

**Example 3**

- Input: `root = [42]`
- Output: `42`
- Explanation: The root is also the only and deepest leaf.
