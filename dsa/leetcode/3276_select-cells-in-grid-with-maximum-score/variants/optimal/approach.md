## General
Given a 2D matrix `grid` consisting of positive integers, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(V m 2^m)$ — Operation count bound.
- **Space Complexity**: $O(V 2^m)$ — Auxiliary memory allocation bound.
