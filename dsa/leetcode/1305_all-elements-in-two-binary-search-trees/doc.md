# All Elements in Two Binary Search Trees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1305 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Search Tree, Sorting, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/all-elements-in-two-binary-search-trees/) |

## Problem Description
### Goal
Two binary search trees are given by their roots, `root1` and `root2`. Collect every node value from both trees and return those values together in ascending order.

Values that occur in both trees are not deduplicated: each node contributes one entry to the result. Either root may be null because each tree is allowed to contain no nodes, so the answer may come entirely from one tree or may be empty when both roots are null.

### Function Contract
**Inputs**

- `root1`: the root of the first binary search tree, or null.
- `root2`: the root of the second binary search tree, or null.
- Each tree contains between 0 and 5000 nodes.
- Every node value lies in the inclusive range $[-10^5,10^5]$.

Let $n$ and $m$ be the numbers of nodes in the first and second trees, respectively, and let $N=n+m$.

**Return value**

An array of length $N$ containing every node value from both trees in ascending order, with multiplicities preserved.

### Examples
**Example 1**

- Input: `root1 = [2,1,4]`, `root2 = [1,0,3]`
- Output: `[0,1,1,2,3,4]`
- Explanation: Both nodes with value 1 remain in the merged result.

**Example 2**

- Input: `root1 = [1,null,8]`, `root2 = [8,1]`
- Output: `[1,1,8,8]`

**Example 3**

- Input: `root1 = []`, `root2 = []`
- Output: `[]`
