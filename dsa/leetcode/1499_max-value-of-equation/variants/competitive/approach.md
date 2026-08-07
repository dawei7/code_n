## General
Given an array `points` containing the coordinates of points on a 2D plane, sorted by the x-values, where $\text{points}[i] = [x_{i}, y_{i}]$ such that $x_{i} < x_{j}$ for all $1 \le i < j \le \text{points.length}$. You are..., the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends.

## Complexity detail
- **Time Complexity**: $O(N)$ — Operation count bound.
- **Space Complexity**: $O(N)$ — Auxiliary memory allocation bound.
