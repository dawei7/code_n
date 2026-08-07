## General
Given There is a **directed weighted** graph that consists of `n` nodes numbered from `0` to $n - 1$. The edges of the graph are initially represented by the given array `edges` where $\text{edges}[i] = [\text{from}_{i}, \t..., the algorithm executes a single-pass linear scan through input elements. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O((n + e) log n)$ — Operation count bound.
- **Space Complexity**: $O(n + e)$ — Auxiliary memory allocation bound.
