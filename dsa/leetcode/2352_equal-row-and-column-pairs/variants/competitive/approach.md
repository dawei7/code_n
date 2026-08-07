## General
Given a **0-indexed** `n x n` integer matrix `grid`, *return the number of pairs *$(r_{i}, c_{j})$* such that row *$r_{i}$* and column *$c_{j}$* are equal*, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n^2)$ — Operation count bound.
- **Space Complexity**: $O(n^2)$ — Auxiliary memory allocation bound.
