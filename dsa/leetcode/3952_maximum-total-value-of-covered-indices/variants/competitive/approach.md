## General
Given an integer array `nums` of length `n` and a binary string `s` of length `n`, where $s[i] = '1'$ means index `i` initially contains a **token** and $s[i] = '0'$ means it does not, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
