## General
Given a string `caption` of length `n`. A **good** caption is a string where **every** character appears in groups of **at least 3** consecutive occurrences, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
