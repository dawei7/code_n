## General
Given the `head` of a singly linked list and two integers `left` and `right` where $left \le right$, reverse the nodes of the list from position `left` to position `right`, and return *the reversed list*, the algorithm solves **Reverse Linked List II** directly. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, linked list node pointers (`val`, `next`) to process sequential node chains.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
