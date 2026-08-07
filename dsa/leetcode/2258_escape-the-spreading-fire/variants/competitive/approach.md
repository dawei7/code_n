## General
Given a **0-indexed** 2D integer array `grid` of size `m x n` which represents a field. Each cell has one of three values:, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(m n log 10^9)$ — Operation count bound.
- **Space Complexity**: $O(m n)$ — Auxiliary memory allocation bound.
