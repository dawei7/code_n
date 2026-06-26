# Difference Between Maximum and Minimum Price Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2538 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Tree, Depth-First Search |
| Official Link | [difference-between-maximum-and-minimum-price-sum](https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/) |

## Problem Description & Examples
### Goal
Given an undirected tree where each node has an associated price, find the maximum possible difference between the sum of prices along any path and the price of one of the endpoints of that path. Specifically, for any path between two nodes $u$ and $v$, we want to maximize $|(\sum_{i \in path(u,v)} price_i) - price_u|$ or $|(\sum_{i \in path(u,v)} price_i) - price_v|$. This simplifies to finding the maximum path sum excluding either the start or end node.

### Function Contract
**Inputs**

- `n`: An integer representing the number of nodes in the tree (labeled 0 to n-1).
- `edges`: A list of lists where each sublist `[u, v]` represents an undirected edge between nodes `u` and `v`.
- `price`: A list of integers where `price[i]` is the cost associated with node `i`.

**Return value**

- An integer representing the maximum difference between the path sum and the price of one of its endpoints.

### Examples
**Example 1**

- Input: `n = 6, edges = [[0,1],[1,2],[1,3],[3,4],[3,5]], price = [9,8,7,6,10,5]`
- Output: `24`

**Example 2**

- Input: `n = 3, edges = [[0,1],[1,2]], price = [1,1,2]`
- Output: `3`

---

## Underlying Base Algorithm(s)
The problem is solved using Tree Dynamic Programming. Since the path can be rooted at any node, we perform a two-pass DFS (Re-rooting technique or post-order traversal). We maintain two DP states for each node: the maximum path sum starting from the node downwards, and the maximum path sum starting from the node downwards excluding the node's own price. By aggregating these values from children, we can compute the optimal path sum for any node acting as the "highest" point of a path.

---

## Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the number of nodes. We traverse the tree twice (or once with post-order aggregation) to compute DP values.
- **Space Complexity**: $O(n)$ to store the adjacency list and the DP tables.
