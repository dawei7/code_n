# Count Nodes That Are Great Enough

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2792 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Divide and Conquer, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-nodes-that-are-great-enough/) |

## Problem Description

### Goal

You are given the root of a binary tree and a positive integer `k`. A node's subtree contains that node together with every descendant below it.

Call a node *great enough* when its subtree contains at least `k` nodes and the node's value is strictly greater than the values of at least `k` nodes in that subtree. Equal values do not count as smaller. Return the total number of nodes that meet both conditions.

### Function Contract

**Inputs**

- `root`: The root of a non-empty binary tree containing between $1$ and $10^4$ nodes. Every node value is an integer from $1$ through $10^4$.
- `k`: The required count of strictly smaller subtree values, with $1 \le k \le 10$.

**Return value**

Return the number of tree nodes whose values are greater than at least `k` values in their own subtrees.

### Examples

**Example 1**

- Input: `root = [7, 6, 5, 4, 3, 2, 1], k = 2`
- Output: `3`
- Explanation: The root and its two children each exceed at least two values in their respective subtrees.

**Example 2**

- Input: `root = [1, 2, 3], k = 1`
- Output: `0`
- Explanation: No node has a strictly smaller value below it.

**Example 3**

- Input: `root = [3, 2, 2], k = 2`
- Output: `1`
- Explanation: The root is greater than both child values, while neither leaf has enough smaller subtree values.
