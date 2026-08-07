## General
Given an integer array `nums`, return* an integer array *`counts`* where *$\text{counts}[i]$* is the number of smaller elements to the right of *$\text{nums}[i]$, the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n \log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
