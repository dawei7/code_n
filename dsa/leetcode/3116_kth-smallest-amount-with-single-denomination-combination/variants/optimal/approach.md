## General
Given an integer array `coins` representing coins of different denominations and an integer `k`, the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(2^m (m + log U))$ — Operation count bound.
- **Space Complexity**: $O(2^m + m)$ — Auxiliary memory allocation bound.
