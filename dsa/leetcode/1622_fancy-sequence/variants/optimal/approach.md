## General
Given Write an API that generates fancy sequences using the `append`, `addAll`, and `multAll` operations, the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(Q\log M)$ — Operation count bound.
- **Space Complexity**: $O(A)$ — Auxiliary memory allocation bound.
