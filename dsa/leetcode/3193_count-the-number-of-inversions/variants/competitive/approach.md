## General
Given an integer `n` and a 2D array `requirements`, where $\text{requirements}[i] = [\text{end}_{i}, \text{cnt}_{i}]$ represents the end index and the **inversion** count of each requirement, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(nC)$ — Operation count bound.
- **Space Complexity**: $O(n + C)$ — Auxiliary memory allocation bound.
