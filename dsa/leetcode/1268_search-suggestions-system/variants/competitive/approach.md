## General
Given an array of strings `products` and a string `searchWord`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(S+m)$ — Operation count bound.
- **Space Complexity**: $O(S+m)$ — Auxiliary memory allocation bound.
