## General
Given There is a rooted tree consisting of `n` nodes numbered `0` to $n - 1$. Each node's number denotes its **unique genetic value** (i.e. the genetic value of node `x` is `x`). The **genetic difference** between two genet..., the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O((N+Q)B)$ — Operation count bound.
- **Space Complexity**: $O(NB+Q)$ — Auxiliary memory allocation bound.
