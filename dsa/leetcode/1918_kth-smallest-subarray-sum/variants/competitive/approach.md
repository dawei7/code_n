## General
Given an integer array `nums` of length `n` and an integer `k`, return *the *$$k^{\text{th}}$$ ***smallest subarray sum**.*, the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(N \log S)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
