## General
Given You have `n` coins and you want to build a staircase with these coins. The staircase consists of `k` rows where the $$i^{\text{th}}$$ row has exactly `i` coins. The last row of the staircase **may be** incomplete, the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(1)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
