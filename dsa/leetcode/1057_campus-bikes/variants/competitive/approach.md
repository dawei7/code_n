## General
Given On a campus represented on the X-Y plane, there are `n` workers and `m` bikes, with $n \le m$, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O(WB+D)$ — Operation count bound.
- **Space Complexity**: $O(WB+D)$ — Auxiliary memory allocation bound.
