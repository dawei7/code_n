## General
Given an integer array `prices` where $\text{prices}[i]$ is the price of a stock in dollars on the $$i^{\text{th}}$$ day, and an integer `k`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a dynamic programming memoization table to cache intermediate subproblem states.

## Complexity detail
- **Time Complexity**: $O(n * k)$ — Operation count bound.
- **Space Complexity**: $O(k)$ — Auxiliary memory allocation bound.
