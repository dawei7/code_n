## General
Given an integer `n` representing the number of nodes in a graph, labeled from 0 to $n - 1$, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O((n + Q) * log n)$ — Operation count bound.
- **Space Complexity**: $O(n * log n)$ — Auxiliary memory allocation bound.
