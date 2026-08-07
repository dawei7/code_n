## General
Given an integer array `cookies`, where $\text{cookies}[i]$ denotes the number of cookies in the $$i^{\text{th}}$$ bag. You are also given an integer `k` that denotes the number of children to distribute **all** the bags of..., the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(k^n)$ — Operation count bound.
- **Space Complexity**: $O(nk)$ — Auxiliary memory allocation bound.
