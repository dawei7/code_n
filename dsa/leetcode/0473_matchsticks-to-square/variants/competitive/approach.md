## General
Given an integer array `matchsticks` where $\text{matchsticks}[i]$ is the length of the $$i^{\text{th}}$$ matchstick. You want to use **all the matchsticks** to make one square. You **should not break** any stick, but you c..., the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n \cdot 2^n)$ — Operation count bound.
- **Space Complexity**: $O(2^n)$ — Auxiliary memory allocation bound.
