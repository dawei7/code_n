## General
Given the `head` of a linked list, return *the node where the cycle begins. If there is no cycle, return *`null`, the algorithm solves **Linked List Cycle II** directly. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, linked list node pointers (`val`, `next`) to process sequential node chains.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
