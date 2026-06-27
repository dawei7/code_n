# Shortest Path in a Weighted Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3515 |
| Difficulty | Hard |
| Topics | Array, Tree, Depth-First Search, Binary Indexed Tree, Segment Tree |
| Official Link | [shortest-path-in-a-weighted-tree](https://leetcode.com/problems/shortest-path-in-a-weighted-tree/) |

## Problem Description & Examples
### Goal
Given a weighted tree structure and a set of queries, determine the shortest path distance between two specified nodes for each query. The tree edges have associated weights, and the path distance is defined as the sum of weights of all edges connecting the two nodes.

### Function Contract
**Inputs**

- `n`: An integer representing the number of nodes in the tree (labeled 0 to n-1).
- `edges`: A list of lists where each inner list `[u, v, w]` represents an undirected edge between nodes `u` and `v` with weight `w`.
- `queries`: A list of lists where each inner list `[start, end]` represents a request to find the distance between `start` and `end`.

**Return value**

- A list of integers where the $i$-th element is the shortest path distance for the $i$-th query.

### Examples
**Example 1**

- Input: `n = 3, edges = [[0, 1, 5], [1, 2, 3]], queries = [[0, 2]]`
- Output: `[8]`

**Example 2**

- Input: `n = 4, edges = [[0, 1, 1], [1, 2, 2], [1, 3, 3]], queries = [[0, 2], [2, 3]]`
- Output: `[3, 5]`

**Example 3**

- Input: `n = 5, edges = [[0, 1, 2], [0, 2, 4], [1, 3, 1], [1, 4, 7]], queries = [[3, 4], [2, 3]]`
- Output: `[8, 7]`

---

## Underlying Base Algorithm(s)
The problem is solved using the Lowest Common Ancestor (LCA) approach. Since the distance between two nodes $u$ and $v$ in a tree is given by $dist(root, u) + dist(root, v) - 2 \times dist(root, LCA(u, v))$, we precompute the depths and distances from the root using DFS, and use Binary Lifting to find the LCA in logarithmic time.

---

## Complexity Analysis
- **Time Complexity**: $O((n + q) \log n)$, where $n$ is the number of nodes and $q$ is the number of queries. Preprocessing the tree takes $O(n \log n)$ and each query takes $O(\log n)$.
- **Space Complexity**: $O(n \log n)$ to store the binary lifting table (ancestor table).
