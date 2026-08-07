## General
Given an integer array `nums` of length `n` and an integer `numSlots` such that $2 * numSlots \ge n$. There are `numSlots` slots numbered from `1` to `numSlots`, the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(m 3^m)$ — Operation count bound.
- **Space Complexity**: $O(3^m)$ — Auxiliary memory allocation bound.
