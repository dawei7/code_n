## General
Given an integer `mountainHeight` denoting the height of a mountain, the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(w log U)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
