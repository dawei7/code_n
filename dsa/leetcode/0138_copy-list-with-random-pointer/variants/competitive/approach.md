## General
Given A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`, the algorithm solves **Copy List with Random Pointer** directly. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, linked list node pointers (`val`, `next`) to process sequential node chains.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
