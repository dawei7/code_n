## General
Given the `head` of a sorted linked list, *delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list*. Return *the linked list **sorted** as well*, the algorithm solves **Remove Duplicates from Sorted List II** directly. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, linked list node pointers (`val`, `next`) to process sequential node chains.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
