## General
Given an array `books` where $\text{books}[i] = [\text{thickness}_{i}, \text{height}_{i}]$ indicates the thickness and height of the $$i^{\text{th}}$$ book. You are also given an integer `shelfWidth`, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n^2)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
