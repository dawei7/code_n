## General
Given an undirected tree rooted at node 0 with `n` nodes numbered from 0 to $n - 1$. Each node `i` has an integer value $\text{vals}[i]$, and its parent is given by $\text{par}[i]$, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n * 3^D)$ — Operation count bound.
- **Space Complexity**: $O(n * 2^D)$ — Auxiliary memory allocation bound.
