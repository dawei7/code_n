# Collect Coins in a Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2603 |
| Difficulty | Hard |
| Topics | Array, Tree, Graph Theory, Topological Sort |
| Official Link | [collect-coins-in-a-tree](https://leetcode.com/problems/collect-coins-in-a-tree/) |

## Problem Description & Examples
### Goal
Given an undirected tree where some nodes contain coins, you must collect all coins by traversing the tree. You are allowed to remove any leaf nodes that do not contain coins. After pruning, you must calculate the total number of edges traversed to visit all remaining nodes containing coins, starting from any node and returning to the starting point (effectively counting each edge twice).

### Function Contract
**Inputs**

- `coins`: A list of integers where `coins[i]` is 1 if node `i` has a coin, and 0 otherwise.
- `edges`: A list of pairs representing the undirected connections between nodes.

**Return value**

- An integer representing the minimum number of edges traversed to collect all coins.

### Examples
**Example 1**

- Input: `coins = [1,0,0,0,0,1], edges = [[0,1],[1,2],[2,3],[3,4],[4,5]]`
- Output: `2`

**Example 2**

- Input: `coins = [0,0,0,1,1,0,0,1], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]]`
- Output: `2`

**Example 3**

- Input: `coins = [0,0], edges = [[0,1]]`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem is solved using a multi-pass Topological Sort (Kahn's Algorithm approach). First, we prune all leaf nodes that do not contain coins, as they are irrelevant to the collection process. Second, we prune the tree twice more to remove nodes that are at a distance of 2 from any coin, as these nodes do not need to be visited to collect the coins. The remaining edges in the pruned graph are counted, and the result is twice the number of remaining edges.

---

## Complexity Analysis
- **Time Complexity**: `O(N)`, where `N` is the number of nodes in the tree. We perform a constant number of passes over the nodes and edges.
- **Space Complexity**: `O(N)` to store the adjacency list and the degree of each node.
