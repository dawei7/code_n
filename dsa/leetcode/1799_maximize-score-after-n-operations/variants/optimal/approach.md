## General
Given `nums`, an array of positive integers of size $2 * n$. You must perform `n` operations on this array, the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates, the walrus operator (`:=`) for inline assignment and evaluation. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(m^2 2^m)$ — Operation count bound.
- **Space Complexity**: $O(m^2 + 2^m)$ — Auxiliary memory allocation bound.
