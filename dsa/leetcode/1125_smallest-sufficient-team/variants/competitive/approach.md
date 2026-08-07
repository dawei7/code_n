## General
Given In a project, you have a list of required skills $\text{req}_{skills}$, and a list of people. The $$i^{\text{th}}$$ person $\text{people}[i]$ contains a list of skills that the person has, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(p2^s)$ — Operation count bound.
- **Space Complexity**: $O(p2^s)$ — Auxiliary memory allocation bound.
