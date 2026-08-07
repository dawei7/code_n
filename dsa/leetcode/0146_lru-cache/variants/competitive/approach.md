## General
Given Design a data structure that follows the constraints of a **<a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU" target="_blank">Least Recently Used (LRU) cache</a>**, the algorithm solves **LRU Cache** directly. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, linked list node pointers (`val`, `next`) to process sequential node chains.

## Complexity detail
- **Time Complexity**: $O(1)$ — Operation count bound.
- **Space Complexity**: $O(capacity)$ — Auxiliary memory allocation bound.
