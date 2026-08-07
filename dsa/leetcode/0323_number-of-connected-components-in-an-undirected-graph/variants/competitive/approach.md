## General
Given You have a graph of `n` nodes. You are given an integer `n` and an array `edges` where $\text{edges}[i] = [a_{i}, b_{i}]$ indicates that there is an edge between $a_{i}$ and $b_{i}$ in the graph, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n + e \alpha(n))$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
