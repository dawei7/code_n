## General
Given a **0-indexed** integer array `nums` and an integer `d`, return *the number of triplets* `(i, j, k)` *such that* `i < j < k` *and* $(\text{nums}[i] + \text{nums}[j] + \text{nums}[k]) \% d = 0$, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(N^2)$ — Operation count bound.
- **Space Complexity**: $O(N)$ — Auxiliary memory allocation bound.
