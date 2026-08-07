## General
Given an undirected tree rooted at node 0 with `n` nodes numbered from 0 to $n - 1$. Each node `i` has an integer value $\text{vals}[i]$, and its parent is given by $\text{par}[i]$, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n log^2 n + q log n)$ — Operation count bound.
- **Space Complexity**: $O(n log n + q)$ — Auxiliary memory allocation bound.
