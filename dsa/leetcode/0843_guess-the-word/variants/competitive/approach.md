## General
Given an array of unique strings `words` where $\text{words}[i]$ is six letters long. One word of `words` was chosen as a secret word, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(qg^2)$ — Operation count bound.
- **Space Complexity**: $O(g)$ — Auxiliary memory allocation bound.
