## General
Given the array `houses` where $\text{houses}[i]$ is the location of the $$i^{\text{th}}$$ house along a street and an integer `k`, allocate `k` mailboxes in the street, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(kN^2)$ — Operation count bound.
- **Space Complexity**: $O(N^2)$ — Auxiliary memory allocation bound.
