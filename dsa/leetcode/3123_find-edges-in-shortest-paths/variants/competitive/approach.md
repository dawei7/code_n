## General
Given an undirected weighted graph of `n` nodes numbered from 0 to $n - 1$. The graph consists of `m` edges represented by a 2D array `edges`, where $\text{edges}[i] = [a_{i}, b_{i}, w_{i}]$ indicates that there is an edge ..., the algorithm executes a single-pass linear scan through input elements. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O((n + m) log n)$ — Operation count bound.
- **Space Complexity**: $O(n + m)$ — Auxiliary memory allocation bound.
