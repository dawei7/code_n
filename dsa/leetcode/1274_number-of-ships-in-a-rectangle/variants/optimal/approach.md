## General
Given *(This problem is an **interactive problem**.)*, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(s \log C)$ — Operation count bound.
- **Space Complexity**: $O(\log C)$ — Auxiliary memory allocation bound.
