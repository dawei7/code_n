## General
Given two **sorted 0-indexed** integer arrays `nums1` and `nums2` as well as an integer `k`, return *the *$$k^{\text{th}}$$* (**1-based**) smallest product of *$\text{nums1}[i] * \text{nums2}[j]$* where *$0 \le i < \text{nu..., the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(A\log B\log R)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
