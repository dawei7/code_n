## General
Given a **0-indexed** integer array `nums` and an integer `p`. Find `p` pairs of indices of `nums` such that the **maximum** difference amongst all the pairs is **minimized**. Also, ensure no index appears more than once am..., the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n\log n+n\log D)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
