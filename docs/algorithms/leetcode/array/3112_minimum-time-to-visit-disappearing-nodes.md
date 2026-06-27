# Minimum Time to Visit Disappearing Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3112 |
| Difficulty | Medium |
| Topics | Array, Graph Theory, Heap (Priority Queue), Shortest Path |
| Official Link | [minimum-time-to-visit-disappearing-nodes](https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/) |

## Problem Description & Examples
### Goal
Given a graph represented by edges with travel times, determine the shortest time required to reach every node from the source node (node 0). Each node has a specific "disappearance time"; if the arrival time at a node is greater than or equal to its disappearance time, that node becomes unreachable. If a node cannot be reached before it disappears, the result for that node should be -1.

### Function Contract
**Inputs**

- `n`: An integer representing the number of nodes (labeled 0 to n-1).
- `edges`: A list of lists where each inner list `[u, v, length]` represents an undirected edge between `u` and `v` with travel time `length`.
- `disappear`: A list of integers where `disappear[i]` is the time at which node `i` becomes inaccessible.

**Return value**

- A list of integers of length `n`, where the `i`-th element is the minimum time to reach node `i`, or -1 if it is unreachable.

### Examples
**Example 1**

- Input: `n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,1,5]`
- Output: `[0,-1,3]`

**Example 2**

- Input: `n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,3,5]`
- Output: `[0,2,3]`

**Example 3**

- Input: `n = 2, edges = [[0,1,1]], disappear = [1,1]`
- Output: `[0,-1]`

---

## Underlying Base Algorithm(s)
Dijkstra's Algorithm. We use a min-priority queue to greedily explore the shortest paths. We only push a neighbor into the queue if the arrival time is strictly less than the node's disappearance time.

---

## Complexity Analysis
- **Time Complexity**: `O(E log E + E log V)`, where `E` is the number of edges and `V` is the number of nodes, due to the priority queue operations.
- **Space Complexity**: `O(V + E)` to store the adjacency list and the distance array.
