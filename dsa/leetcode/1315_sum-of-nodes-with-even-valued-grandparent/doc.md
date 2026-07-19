# Sum of Nodes with Even-Valued Grandparent

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1315 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/) |

## Problem Description
### Goal
Given the root of a nonempty binary tree, identify every node whose grandparent has an even value. A node's grandparent is the parent of its parent, so the root and its direct children never qualify.

Add the values of all qualifying nodes and return the total. The parity of the qualifying node and its parent does not matter; only the grandparent's value determines whether the node contributes. Return 0 when no node has an even-valued grandparent.

### Function Contract
**Inputs**

- `root`: the root of a binary tree containing $n$ nodes, where $1\le n\le10^4$.
- Every node value is between 1 and 100 inclusive.

**Return value**

The sum of `node.val` over all nodes whose existing grandparent has an even value.

### Examples
**Example 1**

- Input: `root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]`
- Output: `18`

**Example 2**

- Input: `root = [1]`
- Output: `0`

**Example 3**

- Input: `root = [2,3,5,7,11,13,17]`
- Output: `48`
- Explanation: The four grandchildren have even-valued grandparent 2, so they contribute $7+11+13+17$.
