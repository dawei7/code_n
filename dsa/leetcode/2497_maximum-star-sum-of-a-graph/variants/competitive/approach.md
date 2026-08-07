## General
Given There is an undirected graph consisting of `n` nodes numbered from `0` to $n - 1$. You are given a **0-indexed** integer array `vals` of length `n` where $\text{vals}[i]$ denotes the value of the $$i^{\text{th}}$$ node, the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n + m log(k + 1))$ — Operation count bound.
- **Space Complexity**: $O(n + m)$ — Auxiliary memory allocation bound.
