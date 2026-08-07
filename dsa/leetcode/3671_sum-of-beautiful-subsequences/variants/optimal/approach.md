## General
Given an integer array `nums` of length `n`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(V log log V + n sqrt(V) + T log V)$ — Operation count bound.
- **Space Complexity**: $O(V log V)$ — Auxiliary memory allocation bound.
