# Critical Connections in a Network

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `graph_15` |
| Frontend ID | 1192 |
| Difficulty | Hard |
| Topics | Depth-First Search, Graph Theory, Biconnected Component |
| Official Link | [critical-connections-in-a-network](https://leetcode.com/problems/critical-connections-in-a-network/) |

## Problem Description & Examples
### Goal
Find all strongly connected components of a directed graph
using Tarjan's algorithm. Each SCC is a maximal set of
nodes where every node can reach every other.
Return a list of SCCs; each SCC is sorted internally; the
outer list is sorted by smallest element.
Requirement: O(V + E).
Source: https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/

### Function Contract
**Inputs**

- `num_nodes`: number of nodes in the graph.
- `edges`: list-like of (u, v) tuples for directed edges.

**Return value**

a list of SCCs (each a sorted list of node indices; outer list sorted).

### Examples
_This local spec has fewer than three authored examples. Add original examples before marking this reference complete._

---

## Underlying Base Algorithm(s)
graphs

---

## Complexity Analysis
- **Time Complexity**: `O(n²)`
- **Space Complexity**: `TODO`
