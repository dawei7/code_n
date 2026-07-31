# Find the Level of Tree with Minimum Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3157 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-level-of-tree-with-minimum-sum/) |

## Problem Description
### Goal
Given the root of a non-empty binary tree whose nodes hold positive values, consider the sum of all node values at each depth. The root belongs to level $1$; every other node's level is one more than its distance in edges from the root.

Return the level number having the minimum value sum. If several levels share that minimum, return the smallest level number, which is the tied level closest to the root.

### Function Contract
**Inputs**

- `root`: The root of a binary tree containing between $1$ and $10^5$ nodes, inclusive. Every node value satisfies $1 \le \texttt{Node.val} \le 10^9$.

**Return value**

Return the 1-indexed level with the smallest sum of node values. On a tie, return the lowest numerical level.

### Examples
**Example 1**

- Input: `root = [50, 6, 2, 30, 80, 7]`
- Output: `2`
- Explanation: The level sums are $50$, $8$, and $117$, so level $2$ is minimum.

**Example 2**

- Input: `root = [36, 17, 10, null, null, 24]`
- Output: `3`
- Explanation: The sums are $36$ at level $1$, $27$ at level $2$, and $24$ at level $3$.

**Example 3**

- Input: `root = [5, null, 5, null, 5]`
- Output: `1`
- Explanation: Every level sums to $5$, so the smallest level number wins the tie.
