## General
Given Alice is a caretaker of `n` gardens and she wants to plant flowers to maximize the total beauty of all her gardens, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n log n + n log target)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
