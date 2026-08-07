## General
Given an integer `n` representing the number of tasks in a project, numbered from 0 to $n - 1$. These tasks are connected as an undirected** tree**. This is represented by a 2D integer array `edges` of length $n - 1$, where..., the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
