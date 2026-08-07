## General
Given the heads of two sorted linked lists `list1` and `list2`, the algorithm solves **Merge Two Sorted Lists** directly. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, linked list node pointers (`val`, `next`) to process sequential node chains.

## Complexity detail
- **Time Complexity**: $O(m + n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
