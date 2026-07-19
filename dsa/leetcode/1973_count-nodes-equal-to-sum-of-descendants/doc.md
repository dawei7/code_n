# Count Nodes Equal to Sum of Descendants

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1973 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/count-nodes-equal-to-sum-of-descendants/) |

## Problem Description
### Goal
Given the root of a nonempty binary tree, count the nodes whose stored value
equals the sum of the values stored in all of their descendants. A descendant
is any node strictly below the current node on a path toward a leaf; the
current node itself is not included.

A leaf has no descendants, so its descendant sum is defined as zero. It
therefore contributes to the answer exactly when its own value is `0`.

### Function Contract
**Inputs**

- `root`: the root of a binary tree containing $N$ nodes, where
  $1 \le N \le 10^5$.
- Every node value is an integer in the inclusive range from `0` through
  $10^5$.

**Return value**

- The number of nodes whose value equals the sum of all strict descendants in
  that node's subtree.

### Examples
**Example 1**

- Input: `root = [10, 3, 4, 2, 1]`
- Output: `2`

**Example 2**

- Input: `root = [2, 3, null, 2, null]`
- Output: `0`

**Example 3**

- Input: `root = [0]`
- Output: `1`
