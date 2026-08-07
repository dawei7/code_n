## General
Given There is an undirected graph of `n` nodes. You are given a 2D array `edges`, where $\text{edges}[i] = [u_{i}, v_{i}, \text{length}_{i}]$ describes an edge between node $u_{i}$ and node $v_{i}$ with a traversal time of..., the algorithm executes a single-pass linear scan through input elements. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O((n + m) log n)$ — Operation count bound.
- **Space Complexity**: $O(n + m)$ — Auxiliary memory allocation bound.
