## General
Given an integer `n` representing the number of nodes in a **directed weighted** graph, numbered from 0 to $n - 1$. This is represented by a 2D integer array `edges`, where $\text{edges}[i] = [u_{i}, v_{i}, w_{i}]$ represen..., the algorithm executes a single-pass linear scan through input elements. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(k(n+m) log(nk))$ — Operation count bound.
- **Space Complexity**: $O(k(n+m))$ — Auxiliary memory allocation bound.
