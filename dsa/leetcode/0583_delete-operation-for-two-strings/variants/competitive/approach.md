## General
Given two strings `word1` and `word2`, return *the minimum number of **steps** required to make* `word1` *and* `word2` *the same*, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(m n)$ — Operation count bound.
- **Space Complexity**: $O(\min(m, n))$ — Auxiliary memory allocation bound.
