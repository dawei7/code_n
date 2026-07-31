# Make Costs of Paths Equal in a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2673 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Greedy, Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/) |

## Problem Description

### Goal

You are given a perfect binary tree containing nodes numbered from $1$ through $n$. Node $1$ is the root, and every non-leaf node $i$ has children $2i$ and $2i + 1$. The 0-indexed array `cost` stores the positive node costs, so `cost[i]` belongs to node $i + 1$.

One operation increments any single node's cost by one. Apply as few operations as possible so that the sum of node costs on every root-to-leaf path is identical, and return that minimum number of increments. Costs may only increase; they cannot be reduced.

### Function Contract

**Inputs**

- `n`: The number of nodes, where $3 \le n \le 10^5$ and $n + 1$ is a power of two.
- `cost`: An integer array of length $n$, where $1 \le \texttt{cost[i]} \le 10^4$.

**Return value**

- Return the minimum total number of unit increments needed to equalize all root-to-leaf path sums.

### Examples

**Example 1**

- Input: `n = 7`, `cost = [1,5,2,2,3,3,1]`
- Output: `6`
- Explanation: The four path sums can all be raised to `9` using six increments in total.

**Example 2**

- Input: `n = 3`, `cost = [5,3,3]`
- Output: `0`
- Explanation: Both root-to-leaf paths already have equal cost.
