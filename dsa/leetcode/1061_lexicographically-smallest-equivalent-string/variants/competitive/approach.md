## General
Given two strings of the same length `s1` and `s2` and a string `baseStr`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(P+B+A)$ — Operation count bound.
- **Space Complexity**: $O(A)$ — Auxiliary memory allocation bound.
