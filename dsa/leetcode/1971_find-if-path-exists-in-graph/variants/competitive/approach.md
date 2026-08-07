## General
Given There is a **bi-directional** graph with `n` vertices, where each vertex is labeled from `0` to $n - 1$ (**inclusive**). The edges in the graph are represented as a 2D integer array `edges`, where each $\text{edges}[i..., the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(V+E)$ — Operation count bound.
- **Space Complexity**: $O(V+E)$ — Auxiliary memory allocation bound.
