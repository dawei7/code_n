# Most Profitable Path in a Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2467 |
| Difficulty | Medium |
| Topics | Array, Tree, Depth-First Search, Breadth-First Search, Graph Theory |
| Official Link | [most-profitable-path-in-a-tree](https://leetcode.com/problems/most-profitable-path-in-a-tree/) |

## Problem Description & Examples
### Goal
Given an undirected tree representing a network of nodes, each containing a specific amount of income (or cost), Alice and Bob start at different nodes and move toward the root (node 0). Alice moves one step per turn starting from a given node, while Bob starts at node 0 and moves toward the root. When they land on a node, they collect the income; if they arrive at the same time, they split the income. If one arrives after the other, the first person collects the entire amount. The goal is to find the maximum net income Alice can accumulate by the time she reaches any leaf node.

### Function Contract
**Inputs**

- `edges`: A list of lists where each sublist `[u, v]` represents an undirected edge between nodes `u` and `v`.
- `bob`: An integer representing the starting node for Bob.
- `amount`: A list of integers where `amount[i]` is the income/cost at node `i`.

**Return value**

- An integer representing the maximum profit Alice can achieve upon reaching any leaf node.

### Examples
**Example 1**

- Input: `edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]`
- Output: `6`

**Example 2**

- Input: `edges = [[0,1]], bob = 1, amount = [-7280,2350]`
- Output: `-7280`

**Example 3**

- Input: `edges = [[0,2],[0,4],[1,3],[2,4]], bob = 0, amount = [1000, -1000, -500, 0, 0]`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem is solved using a combination of **Depth-First Search (DFS)** and **Breadth-First Search (BFS)**. First, we use DFS to determine the path Bob takes to reach the root and record the time at which he visits each node. Then, we perform a second DFS to simulate Alice's traversal, calculating her cumulative income based on her arrival time relative to Bob's arrival time at each node.

---

## Complexity Analysis
- **Time Complexity**: `O(N)`, where `N` is the number of nodes in the tree. We traverse the tree a constant number of times.
- **Space Complexity**: `O(N)` to store the adjacency list, the path/time map for Bob, and the recursion stack.
