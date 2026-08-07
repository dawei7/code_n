## General
Given two integer arrays `costs` and `capacity`, both of length `n`, where $\text{costs}[i]$ represents the purchase cost of the $$i^{\text{th}}$$ machine and $\text{capacity}[i]$ represents its performance capacity, the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(N log N)$ — Operation count bound.
- **Space Complexity**: $O(N)$ — Auxiliary memory allocation bound.
