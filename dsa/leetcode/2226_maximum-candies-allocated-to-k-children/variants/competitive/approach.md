## General
Given a **0-indexed** integer array `candies`. Each element in the array denotes a pile of candies of size $\text{candies}[i]$. You can divide each pile into any number of **sub piles**, but you **cannot** merge two piles t..., the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n log V)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
