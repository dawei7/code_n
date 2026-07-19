# Maximum Product of Splitted Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1339 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/) |

## Problem Description
### Goal
Given the root of a binary tree with positive node values, remove exactly one edge. This separates the original tree into two non-empty subtrees. Compute the sum of the node values in each resulting component and multiply those two sums.

Choose the edge that makes this product as large as possible. Maximize the full integer product first, then return that maximum modulo $10^9+7$; comparing products after reducing them modulo the constant would not preserve their true order.

### Function Contract
**Inputs**

- `root`: the root of a binary tree containing $n$ nodes, where $2\le n\le5\cdot10^4$ and $1\le\texttt{node.val}\le10^4$.

**Return value**

The maximum product of the two component sums obtainable by removing one edge, reduced modulo $10^9+7$ only after the maximum is chosen.

### Examples
**Example 1**

- Input: `root = [1,2,3,4,5,6]`
- Output: `110`
- Explanation: One optimal cut creates components with sums 11 and 10.

**Example 2**

- Input: `root = [1,null,2,3,4,null,null,5,6]`
- Output: `90`

**Example 3**

- Input: `root = [1,2]`
- Output: `2`
- Explanation: The only edge separates sums 1 and 2.
