## General
Given an integer array `nums` where the $$i^{\text{th}}$$ bag contains $\text{nums}[i]$ balls. You are also given an integer `maxOperations`, the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n\log M)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
