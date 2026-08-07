## General
Given an integer `n`. There are `n` rooms numbered from `0` to $n - 1$, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O(m log m + m log n)$ — Operation count bound.
- **Space Complexity**: $O(m + n)$ — Auxiliary memory allocation bound.
