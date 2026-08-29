# Path with Maximum Probability

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1514 |
| Difficulty | Medium |
| Topics | Array, Graph Theory, Heap (Priority Queue), Shortest Path |
| Official Link | [LeetCode](https://leetcode.com/problems/path-with-maximum-probability/) |

## Problem Description

### Goal

An undirected graph has $n$ nodes labeled from 0 through $n-1$. Each listed edge connects two different nodes and has a success probability between 0 and 1. The probability of successfully traversing an entire path is the product of the probabilities on its edges.

Given distinct start and destination nodes, find the greatest success probability among all paths connecting them. Return zero when the destination is unreachable. Results within $10^{-5}$ of the exact maximum are accepted.

### Function Contract

**Inputs**

Let $e$ be the number of edges.

- `n`: The node count, satisfying $2 \leq n \leq 10^4$.
- `edges`: A length-$e$ list of undirected endpoint pairs `[a, b]`. There are no self-loops and at most one edge between a pair of nodes.
- `succProb`: A length-$e$ list where `succProb[i]` is the traversal probability of `edges[i]` and lies in `[0,1]`.
- `start_node`, `end_node`: Distinct valid node labels.

**Return value**

Return the maximum product of edge probabilities along a path from `start_node` to `end_node`, or `0.0` if no such path exists.

### Examples

#### Example 1

- **Input:** `n = 3, edges = [[0, 1], [1, 2], [0, 2]], succProb = [0.5, 0.5, 0.2], start_node = 0, end_node = 2`
- **Output:** `0.25`
- **Explanation:** The two-edge path succeeds with probability $0.5\cdot0.5=0.25$, exceeding the direct edge's 0.2.

#### Example 2

- **Input:** `n = 3, edges = [[0, 1], [1, 2], [0, 2]], succProb = [0.5, 0.5, 0.3], start_node = 0, end_node = 2`
- **Output:** `0.3`

#### Example 3

- **Input:** `n = 3, edges = [[0, 1]], succProb = [0.5], start_node = 0, end_node = 2`
- **Output:** `0.0`
