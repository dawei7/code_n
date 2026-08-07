## General
Given a **0-indexed** integer array `nums` containing `n` **distinct** positive integers. A permutation of `nums` is called special if:, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n^2 2^n)$ — Operation count bound.
- **Space Complexity**: $O(n 2^n)$ — Auxiliary memory allocation bound.
