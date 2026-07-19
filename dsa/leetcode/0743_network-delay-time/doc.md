# Network Delay Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 743 |
| Difficulty | Medium |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Shortest Path |
| Official Link | [LeetCode](https://leetcode.com/problems/network-delay-time/) |

## Problem Description
### Goal
A directed network contains `n` nodes labeled `1` through `n`. Every entry `[u, v, w]` in `times` means a signal needs `w` time units to travel from source `u` to target `v`.

Send a signal from node `k` and return the minimum time by which all `n` nodes have received it, assuming the signal can follow directed paths and reaches each node by its fastest route. If even one node is unreachable from `k`, return `-1`.

### Function Contract
**Inputs**

- `times`: directed edges `[source, destination, travel_time]` with positive travel times
- `n`: the number of nodes labeled from `1` through `n`
- `k`: the node where the signal starts at time zero

**Return value**

- The earliest time by which all nodes have received the signal, equal to the largest shortest-path distance from `k`, or `-1` if any node cannot be reached

### Examples
**Example 1**

- Input: `times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2`
- Output: `2`

**Example 2**

- Input: `times = [], n = 2, k = 2`
- Output: `-1`

**Example 3**

- Input: `times = [[1,2,49],[2,1,8]], n = 2, k = 2`
- Output: `8`
