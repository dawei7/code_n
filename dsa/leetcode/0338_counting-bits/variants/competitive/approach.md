## General
Given an integer `n`, return *an array *`ans`* of length *$n + 1$* such that for each *`i`* *($0 \le i \le n$)*, *$\text{ans}[i]$* is the **number of ***`1`***'s** in the binary representation of *`i`, the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
