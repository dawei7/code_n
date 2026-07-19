# Optimize Water Distribution in a Village

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1168 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Union-Find, Graph Theory, Heap (Priority Queue), Minimum Spanning Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/optimize-water-distribution-in-a-village/) |

## Problem Description

### Goal

A village contains $n$ houses labeled from `1` through `n`, and every house must receive water. For house $i$, you may build a well directly inside it for cost `wells[i - 1]`. A house without its own well may instead receive water through pipes connected, possibly through other houses, to a house that has a well.

Each entry `pipes[j] = [house1, house2, cost]` offers a bidirectional pipe between two different houses for the stated cost. The same pair of houses may have several offers with different costs. Choose any combination of wells and offered pipes that supplies all houses, and return the minimum possible total cost.

### Function Contract

**Inputs**

- `n`: The number of houses, where $2 \le n \le 10^4$.
- `wells`: A length-$n$ array; `wells[i - 1]` is the cost, from `0` through $10^5$, of a well at house $i$.
- `pipes`: Between $1$ and $10^4$ entries `[house1, house2, cost]`, with distinct endpoints in `1..n` and cost from `0` through $10^5$.
- Let $p$ be the number of pipe offers and define $e=n+p$.

**Return value**

- The minimum total cost of wells and pipes that gives every house access to water.

### Examples

**Example 1**

- Input: `n = 3`, `wells = [1,2,2]`, `pipes = [[1,2,1],[2,3,1]]`
- Output: `3`

Build the cost-`1` well at house `1` and use both cost-`1` pipes.

**Example 2**

- Input: `n = 2`, `wells = [1,1]`, `pipes = [[1,2,1],[1,2,2]]`
- Output: `2`
