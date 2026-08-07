## General
Given an equation, represented by `words` on the left side and the `result` on the right side, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time.

## Complexity detail
- **Time Complexity**: $O(10!)$ — Operation count bound.
- **Space Complexity**: $O(U+L)$ — Auxiliary memory allocation bound.
