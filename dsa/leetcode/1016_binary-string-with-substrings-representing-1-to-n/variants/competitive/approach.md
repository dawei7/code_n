## General
Given a binary string `s` and a positive integer `n`, return `true`* if the binary representation of all the integers in the range *`[1, n]`* are **substrings** of *`s`*, or *`false`* otherwise*, the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(ML)$ — Operation count bound.
- **Space Complexity**: $O(\min(n,ML))$ — Auxiliary memory allocation bound.
