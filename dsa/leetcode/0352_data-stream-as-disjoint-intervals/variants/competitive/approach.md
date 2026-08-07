## General
Given a data stream input of non-negative integers $a_{1}, a_{2}, ..., a_{n}$, summarize the numbers seen so far as a list of disjoint intervals, the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(1) / O(k \log k)$ — Operation count bound.
- **Space Complexity**: $O(v)$ — Auxiliary memory allocation bound.
