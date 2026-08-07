## General
Given two jugs with capacities `x` liters and `y` liters. You have an infinite water supply. Return whether the total amount of water in both jugs may reach `target` using the following operations:, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time.

## Complexity detail
- **Time Complexity**: $O(\log \min(x,y))$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
