## General
Given a **(0-indexed)** integer array `nums` and two integers `low` and `high`, return *the number of **nice pairs***, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(nB)$ — Operation count bound.
- **Space Complexity**: $O(nB)$ — Auxiliary memory allocation bound.
