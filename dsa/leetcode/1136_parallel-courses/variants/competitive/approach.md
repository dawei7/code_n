## General
Given an integer `n`, which indicates that there are `n` courses labeled from `1` to `n`. You are also given an array `relations` where $\text{relations}[i] = [\text{prevCourse}_{i}, \text{nextCourse}_{i}]$, representing a ..., the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n+r)$ — Operation count bound.
- **Space Complexity**: $O(n+r)$ — Auxiliary memory allocation bound.
