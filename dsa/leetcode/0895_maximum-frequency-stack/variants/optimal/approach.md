## General
Given Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack, the algorithm solves **Maximum Frequency Stack** directly. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O(1)$ — Operation count bound.
- **Space Complexity**: $O(q)$ — Auxiliary memory allocation bound.
