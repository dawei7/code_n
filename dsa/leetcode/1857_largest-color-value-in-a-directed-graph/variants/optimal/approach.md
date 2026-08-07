## General
Given There is a **directed graph** of `n` colored nodes and `m` edges. The nodes are numbered from `0` to $n - 1$, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends, a dynamic programming memoization table to cache intermediate subproblem states.

## Complexity detail
- **Time Complexity**: $O(26(n+m))$ — Operation count bound.
- **Space Complexity**: $O(26n+m)$ — Auxiliary memory allocation bound.
