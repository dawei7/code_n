## General
Given an integer array `matchsticks` where $\text{matchsticks}[i]$ is the length of the $$i^{\text{th}}$$ matchstick. You want to use **all the matchsticks** to make one square. You **should not break** any stick, but you c..., the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n \cdot 2^n)$ — Operation count bound.
- **Space Complexity**: $O(2^n)$ — Auxiliary memory allocation bound.
