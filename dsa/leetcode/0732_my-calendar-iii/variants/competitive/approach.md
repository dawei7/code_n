## General
Given A `k`-booking happens when `k` events have some non-empty intersection (i.e., there is some time that is common to all `k` events.), the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(q \log C)$ — Operation count bound.
- **Space Complexity**: $O(q \log C)$ — Auxiliary memory allocation bound.
