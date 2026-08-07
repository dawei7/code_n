## General
Given an undirected tree with `n` nodes labeled 0 to $n - 1$. This is represented by a 2D array `edges` of length $n - 1$, where $\text{edges}[i] = [u_{i}, v_{i}]$ indicates an undirected edge between nodes $u_{i}$ and $v_{i}$, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O((N + Q) log N)$ — Operation count bound.
- **Space Complexity**: $O(N log N)$ — Auxiliary memory allocation bound.
