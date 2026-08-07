## General
Given an integer array `instructions`, you are asked to create a sorted array from the elements in `instructions`. You start with an empty container `nums`. For each element from **left to right** in `instructions`, insert ..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n\log M)$ — Operation count bound.
- **Space Complexity**: $O(M)$ — Auxiliary memory allocation bound.
