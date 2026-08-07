## General
Given a **directed** graph of `n` nodes numbered from `0` to $n - 1$, where each node has **at most one** outgoing edge, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
