## General
Given a **directed** graph of `n` nodes numbered from `0` to $n - 1$, where each node has **at most one** outgoing edge, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends. Key operations include the walrus operator (`:=`) for inline assignment and evaluation.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
