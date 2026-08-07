## General
Given an **undirected weighted** tree with `n` nodes, numbered from `0` to $n - 1$. It is represented by a 2D integer array `edges` of length $n - 1$, where $\text{edges}[i] = [u_{i}, v_{i}, w_{i}]$ indicates that there is ..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O((n + q) log n)$ — Operation count bound.
- **Space Complexity**: $O(n log n)$ — Auxiliary memory allocation bound.
