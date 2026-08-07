## General
Given an array of `events` where $\text{events}[i] = [\text{startDay}_{i}, \text{endDay}_{i}, \text{value}_{i}]$. The $$i^{\text{th}}$$ event starts at $\text{startDay}_{i}$_ and ends at $\text{endDay}_{i}$, and if you atte..., the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states.

## Complexity detail
- **Time Complexity**: $O(n\log n+nk)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
