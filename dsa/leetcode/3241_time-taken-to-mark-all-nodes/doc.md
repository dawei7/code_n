# Time Taken to Mark All Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3241 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming, Tree, Depth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/time-taken-to-mark-all-nodes/) |

## Problem Description

### Goal

An undirected tree has $n$ nodes numbered from $0$ through $n-1$. The array `edges` contains its $n-1$ connections, where each pair `[u, v]` joins nodes `u` and `v`.

Initially no node is marked. Consider independently choosing each possible node $i$ and marking it at time $0$. An odd-numbered node becomes marked one time unit after any adjacent node is marked. An even-numbered node instead becomes marked two time units after any adjacent node is marked. Once marked, a node remains available to trigger its neighbors.

For every starting node $i$, determine the time at which the final unmarked node becomes marked. Return these $n$ independent completion times in node-number order.

### Function Contract

**Inputs**

- `edges`: The $n-1$ pairs of endpoints of a valid undirected tree on nodes $0$ through $n-1$.

The constraints guarantee $2 \le n \le 10^5$. Each endpoint is a valid node number.

**Return value**

- An array `times` of length $n$, where `times[i]` is the completion time when only node `i` is marked at time $0$.

### Examples

#### Example 1

- **Input:** `edges = [[0,1],[0,2]]`
- **Output:** `[2,4,3]`

#### Example 2

- **Input:** `edges = [[0,1]]`
- **Output:** `[1,2]`

#### Example 3

- **Input:** `edges = [[2,4],[0,1],[2,3],[0,2]]`
- **Output:** `[4,6,3,5,5]`
