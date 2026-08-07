## General
Given an `m x n` binary matrix `matrix`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(MN)$ — Operation count bound.
- **Space Complexity**: $O(MN)$ — Auxiliary memory allocation bound.
