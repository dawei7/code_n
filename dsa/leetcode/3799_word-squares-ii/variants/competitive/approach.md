## General
Given a string array `words`, consisting of **distinct** 4-letter strings, each containing lowercase English letters, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(W^3 + A)$ — Operation count bound.
- **Space Complexity**: $O(W + A)$ — Auxiliary memory allocation bound.
