## General
Given You have `n` processes forming a rooted tree structure. You are given two integer arrays `pid` and `ppid`, where $\text{pid}[i]$ is the ID of the $$i^{\text{th}}$$ process and $\text{ppid}[i]$ is the ID of the $$i^{\t..., the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
