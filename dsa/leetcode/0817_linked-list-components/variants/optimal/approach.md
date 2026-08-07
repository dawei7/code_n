## General
Given the `head` of a linked list containing unique integer values and an integer array `nums` that is a subset of the linked list values, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, linked list node pointers (`val`, `next`) to process sequential node chains.

## Complexity detail
- **Time Complexity**: $O(n + m)$ — Operation count bound.
- **Space Complexity**: $O(m)$ — Auxiliary memory allocation bound.
