## General
Given the array `queries` of positive integers between `1` and `m`, you have to process all $\text{queries}[i]$ (from `i=0` to `i=queries.length-1`) according to the following rules:, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O((m+q)\log(m+q))$ — Operation count bound.
- **Space Complexity**: $O(m+q)$ — Auxiliary memory allocation bound.
