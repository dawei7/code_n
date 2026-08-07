## General
Given a 2D integer array `lists`, where each $\text{lists}[i]$ is a non-empty array of integers **sorted** in **non-decreasing** order, the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering, a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(3^L + N * 2^L + N log N)$ — Operation count bound.
- **Space Complexity**: $O(2^L + N)$ — Auxiliary memory allocation bound.
