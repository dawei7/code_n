## General
Given an integer `rowIndex`, return the $rowIndex^th$ (**0-indexed**) row of the **Pascal's triangle**, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(rowIndex)$ — Operation count bound.
- **Space Complexity**: $O(rowIndex)$ — Auxiliary memory allocation bound.
