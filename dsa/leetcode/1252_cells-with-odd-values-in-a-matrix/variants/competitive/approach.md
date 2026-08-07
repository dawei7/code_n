## General
Given There is an `m x n` matrix that is initialized to all `0`'s. There is also a 2D array `indices` where each $\text{indices}[i] = [r_{i}, c_{i}]$ represents a **0-indexed location** to perform some increment operations ..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(m+n+k)$ — Operation count bound.
- **Space Complexity**: $O(m+n)$ — Auxiliary memory allocation bound.
