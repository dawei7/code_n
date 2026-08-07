## General
Given Design a HashMap without using any built-in hash table libraries, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, linked list node pointers (`val`, `next`) to process sequential node chains. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(q)$ — Operation count bound.
- **Space Complexity**: $O(U + B)$ — Auxiliary memory allocation bound.
