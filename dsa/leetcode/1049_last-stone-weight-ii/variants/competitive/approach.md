## General
Given an array of integers `stones` where $\text{stones}[i]$ is the weight of the $$i^{\text{th}}$$ stone, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(NS)$ — Operation count bound.
- **Space Complexity**: $O(S)$ — Auxiliary memory allocation bound.
