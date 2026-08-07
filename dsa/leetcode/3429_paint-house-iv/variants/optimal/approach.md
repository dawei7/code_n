## General
Given an **even** integer `n` representing the number of houses arranged in a straight line, and a 2D array `cost` of size `n x 3`, where $\text{cost}[i][j]$ represents the cost of painting house `i` with color $j + 1$, the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a dynamic programming memoization table to cache intermediate subproblem states.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
