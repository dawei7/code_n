## General
Given There is a computer that can run an unlimited number of tasks **at the same time**. You are given a 2D integer array `tasks` where $\text{tasks}[i] = [\text{start}_{i}, \text{end}_{i}, \text{duration}_{i}]$ indicates ..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time.

## Complexity detail
- **Time Complexity**: $O(N log N)$ — Operation count bound.
- **Space Complexity**: $O(T)$ — Auxiliary memory allocation bound.
