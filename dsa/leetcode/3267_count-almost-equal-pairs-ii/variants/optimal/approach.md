## General
Given **Attention**: In this version, the number of operations that can be performed, has been increased to **twice**.<!-- notionvc: 278e7cb2-3b05-42fa-8ae9-65f5fd6f7585 -->, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n log n + n d^5)$ — Operation count bound.
- **Space Complexity**: $O(n + d^4)$ — Auxiliary memory allocation bound.
