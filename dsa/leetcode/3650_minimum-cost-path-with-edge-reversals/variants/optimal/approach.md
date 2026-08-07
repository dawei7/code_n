## General
Given a directed, weighted graph with `n` nodes labeled from 0 to $n - 1$, and an array `edges` where $\text{edges}[i] = [u_{i}, v_{i}, w_{i}]$ represents a directed edge from node $u_{i}$ to node $v_{i}$ with cost $w_{i}$, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O((V + E) log V)$ — Operation count bound.
- **Space Complexity**: $O(V + E)$ — Auxiliary memory allocation bound.
