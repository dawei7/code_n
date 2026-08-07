## General
Given There is a rooted tree consisting of `n` nodes numbered `0` to $n - 1$. Each node's number denotes its **unique genetic value** (i.e. the genetic value of node `x` is `x`). The **genetic difference** between two genet..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O((N+Q)B)$ — Operation count bound.
- **Space Complexity**: $O(NB+Q)$ — Auxiliary memory allocation bound.
