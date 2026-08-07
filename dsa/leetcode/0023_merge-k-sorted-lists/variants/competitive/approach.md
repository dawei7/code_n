## General
Given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering, linked list node pointers (`val`, `next`) to process sequential node chains. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(N \log k)$ — Operation count bound.
- **Space Complexity**: $O(k)$ — Auxiliary memory allocation bound.
