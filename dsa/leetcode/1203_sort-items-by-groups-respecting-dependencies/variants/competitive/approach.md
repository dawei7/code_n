## General
Given There are `n` items each belonging to zero or one of `m` groups where $\text{group}[i]$ is the group that the `i`-th item belongs to and it's equal to `-1` if the `i`-th item belongs to no group. The items and the gro..., the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time, a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n+g+e)$ — Operation count bound.
- **Space Complexity**: $O(n+g+e)$ — Auxiliary memory allocation bound.
