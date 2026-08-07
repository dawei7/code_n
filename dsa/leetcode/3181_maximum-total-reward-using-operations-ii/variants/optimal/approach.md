## General
Given an integer array `rewardValues` of length `n`, representing the values of rewards, the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n log n + nV / w)$ — Operation count bound.
- **Space Complexity**: $O(n + V / w)$ — Auxiliary memory allocation bound.
