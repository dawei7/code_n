## General
Given an integer array `prices`, which shows the chocolate prices and a 2D integer array `queries`, where $\text{queries}[i] = [k_{i}, m_{i}]$, the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O((n + q) \log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
