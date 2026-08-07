## General
Given The **distance of a pair** of integers `a` and `b` is defined as the absolute difference between `a` and `b`, the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n \log n + n \log W)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
