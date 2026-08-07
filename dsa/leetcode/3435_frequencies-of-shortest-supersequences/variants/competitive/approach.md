## General
Given an array of strings `words`. Find all **shortest common supersequences (SCS)** of `words` that are not permutations of each other, the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(W + 2^C C^2)$ — Operation count bound.
- **Space Complexity**: $O(C)$ — Auxiliary memory allocation bound.
