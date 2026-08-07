## General
Given There is an **undirected** connected tree with `n` nodes labeled from `1` to `n` and $n - 1$ edges. You are given the integer `n`. The parent node of a node with a label `v` is the node with the label $floor (v / 2)$...., the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n + q)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
