## General
Given a 2D integer array `intervals`, where $\text{intervals}[i] = [l_{i}, r_{i}, \text{weight}_{i}]$. Interval `i` starts at position $l_{i}$ and ends at $r_{i}$, and has a weight of $\text{weight}_{i}$. You can choose *up..., the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
