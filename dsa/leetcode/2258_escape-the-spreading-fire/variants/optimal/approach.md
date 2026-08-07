## General
Given a **0-indexed** 2D integer array `grid` of size `m x n` which represents a field. Each cell has one of three values:, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(m n log 10^9)$ — Operation count bound.
- **Space Complexity**: $O(m n)$ — Auxiliary memory allocation bound.
