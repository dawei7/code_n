## General
Given an integer `n`, return *the number of positive integers in the range *`[1, n]`* that have **at least one** repeated digit*, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(D^2)$ — Operation count bound.
- **Space Complexity**: $O(D)$ — Auxiliary memory allocation bound.
