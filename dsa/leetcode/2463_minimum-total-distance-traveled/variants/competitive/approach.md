## General
Given There are some robots and factories on the X-axis. You are given an integer array `robot` where $\text{robot}[i]$ is the position of the $$i^{\text{th}}$$ robot. You are also given a 2D integer array `factory` where $..., the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends, a dynamic programming memoization table to cache intermediate subproblem states.

## Complexity detail
- **Time Complexity**: $O(R\log R+F\log F+RF)$ — Operation count bound.
- **Space Complexity**: $O(R+F)$ — Auxiliary memory allocation bound.
