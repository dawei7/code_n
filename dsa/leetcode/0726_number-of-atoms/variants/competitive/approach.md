## General
Given a string `formula` representing a chemical formula, return *the count of each atom*, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n + A \log A)$ — Operation count bound.
- **Space Complexity**: $O(A + d)$ — Auxiliary memory allocation bound.
