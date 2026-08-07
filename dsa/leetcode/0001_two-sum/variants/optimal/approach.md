## General
Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include the walrus operator (`:=`) for inline assignment and evaluation.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
