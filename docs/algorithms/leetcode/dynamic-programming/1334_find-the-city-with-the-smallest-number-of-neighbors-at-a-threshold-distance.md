# Find the City With the Smallest Number of Neighbors at a Threshold Distance

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `graph_06` |
| Frontend ID | 1334 |
| Difficulty | Medium |
| Topics | Dynamic Programming, Graph Theory, Shortest Path |
| Official Link | [find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) |

## Problem Description & Examples
### Goal
Compute all-pairs shortest paths using the Floyd-Warshall
algorithm. The graph has directed, weighted edges (positive
weights). Return the N x N distance matrix where entry [i][j]
is the shortest distance from i to j, or -1 if j is
unreachable from i. The diagonal [i][i] is 0.
Requirement: O(V^3).
Source: https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/

### Function Contract
**Inputs**

- `num_nodes`: number of nodes in the graph.
- `edges`: list-like of (u, v, weight) tuples for directed edges.

**Return value**

an N x N matrix of shortest distances; -1 for unreachable pairs.

### Examples
_This local spec has fewer than three authored examples. Add original examples before marking this reference complete._

---

## Underlying Base Algorithm(s)
graphs

---

## Complexity Analysis
- **Time Complexity**: `O(n³)`
- **Space Complexity**: `TODO`
