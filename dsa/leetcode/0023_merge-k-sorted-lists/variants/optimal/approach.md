## General
Given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order, the algorithm executes a single-pass linear scan through input elements. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering, linked list node pointers (`val`, `next`) to process sequential node chains.

## Complexity detail
- **Time Complexity**: $O(N \log k)$ — Operation count bound.
- **Space Complexity**: $O(k)$ — Auxiliary memory allocation bound.
