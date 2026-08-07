## General
Given a **0-indexed** integer array `nums`. In one step, **remove** all elements $\text{nums}[i]$ where $nums[i - 1] > \text{nums}[i]$ for all `0 < i < nums.length`, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
