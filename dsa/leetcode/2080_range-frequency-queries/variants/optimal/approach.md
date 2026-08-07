## General
Given Design a data structure to find the **frequency** of a given value in a given subarray, the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n+Q\log n)$ — Operation count bound.
- **Space Complexity**: $O(n+Q)$ — Auxiliary memory allocation bound.
