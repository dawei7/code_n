## General
Given a binary array `pattern` and an object `stream` of class `InfiniteStream` representing a **0-indexed** infinite stream of bits, the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(S + M)$ — Operation count bound.
- **Space Complexity**: $O(M)$ — Auxiliary memory allocation bound.
