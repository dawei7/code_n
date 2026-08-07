## General
Given an `m x n` grid `grid` of values `0`, `1`, or `2`, where:, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time, a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends.

## Complexity detail
- **Time Complexity**: $O(bmn)$ — Operation count bound.
- **Space Complexity**: $O(mn)$ — Auxiliary memory allocation bound.
