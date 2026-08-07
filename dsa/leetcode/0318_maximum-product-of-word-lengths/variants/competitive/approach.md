## General
Given a string array `words`, return *the maximum value of* $length(\text{word}[i]) * length(\text{word}[j])$ *where the two words do not share common letters*. If no such two words exist, return `0`, the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(C + n^2)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
