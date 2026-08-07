## General
Given In some array `arr`, the values were in arithmetic progression: the values $arr[i + 1] - \text{arr}[i]$ are all equal for every $0 \le i < \text{arr.length} - 1$, the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(\log n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
