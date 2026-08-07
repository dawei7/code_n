## General
Given an array of distinct integers `arr`, where `arr` is sorted in **ascending order**, return the smallest index `i` that satisfies $\text{arr}[i] = i$. If there is no such index, return `-1`, the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(\log N)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
