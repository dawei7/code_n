## General
Given an integer array `nums` of length `n`, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(M log log M + n log M)$ — Operation count bound.
- **Space Complexity**: $O(n + M)$ — Auxiliary memory allocation bound.
