## General
Given a **0-indexed** 2D integer array `peaks` where $\text{peaks}[i] = [x_{i}, y_{i}]$ states that mountain `i` has a peak at coordinates $(x_{i}, y_{i})$. A mountain can be described as a right-angled isosceles triangle, ..., the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
