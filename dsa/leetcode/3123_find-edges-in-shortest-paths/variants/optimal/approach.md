## General
Given an undirected weighted graph of `n` nodes numbered from 0 to $n - 1$. The graph consists of `m` edges represented by a 2D array `edges`, where $\text{edges}[i] = [a_{i}, b_{i}, w_{i}]$ indicates that there is an edge ..., the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O((n + m) log n)$ — Operation count bound.
- **Space Complexity**: $O(n + m)$ — Auxiliary memory allocation bound.
