# Smallest Missing Genetic Value in Each Subtree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2003 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Tree, Depth-First Search, Union-Find |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/) |

## Problem Description

### Goal

A family tree contains $N$ nodes numbered from $0$ through $N-1$ and is rooted at node $0$. Array `parents` gives the parent of every node, with `parents[0] = -1`. Each node $i$ carries the distinct positive genetic value `nums[i]`, drawn from $1$ through $10^5$.

For every node $i$, consider all genetic values stored at $i$ and its descendants. Find the smallest positive integer absent from that subtree and return all $N$ answers in node order.

### Function Contract

**Inputs**

- `parents`: a valid rooted-tree parent array of length $N$, where $2 \le N \le 10^5$.
- `nums`: $N$ pairwise-distinct integers from $1$ through $10^5$.

**Return value**

Return an array `answer` of length $N$ in which `answer[i]` is the smallest positive genetic value missing from the subtree rooted at node $i$.

### Examples

**Example 1**

- Input: `parents = [-1, 0, 0, 2], nums = [1, 2, 3, 4]`
- Output: `[5, 1, 1, 1]`
- Explanation: The root contains values $1$ through $4$, while every other subtree omits $1$.

**Example 2**

- Input: `parents = [-1, 0, 1, 0, 3, 3], nums = [5, 4, 6, 2, 1, 3]`
- Output: `[7, 1, 1, 4, 2, 1]`
- Explanation: The subtree at node $3$ contains $\{1,2,3\}$, and the leaf holding $1$ is missing $2$.

**Example 3**

- Input: `parents = [-1, 2, 3, 0, 2, 4, 1], nums = [2, 3, 4, 5, 6, 7, 8]`
- Output: `[1, 1, 1, 1, 1, 1, 1]`
- Explanation: Genetic value $1$ is absent from the whole tree, so it is absent from every subtree.
