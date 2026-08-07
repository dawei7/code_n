## General
Given an integer `n` and a **directed** graph with `n` nodes labeled from 0 to $n - 1$. This is represented by a 2D array `edges`, where $\text{edges}[i] = [u_{i}, v_{i}, \text{start}_{i}, \text{end}_{i}]$ indicates an edge..., the algorithm executes a single-pass linear scan through input elements. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O((n + m) log n)$ — Operation count bound.
- **Space Complexity**: $O(n + m)$ — Auxiliary memory allocation bound.
