## General
Given an **undirected weighted** **connected** graph containing `n` nodes labeled from `0` to $n - 1$, and an integer array `edges` where $\text{edges}[i] = [a_{i}, b_{i}, w_{i}]$ indicates that there is an edge between nod..., the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O((n + m) log n)$ — Operation count bound.
- **Space Complexity**: $O(n + m)$ — Auxiliary memory allocation bound.
