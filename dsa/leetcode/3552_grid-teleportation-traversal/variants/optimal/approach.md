## General
Given a 2D character grid `matrix` of size `m x n`, represented as an array of strings, where $\text{matrix}[i][j]$ represents the cell at the intersection of the $$i^{\text{th}}$$ row and $$j^{\text{th}}$$ column. Each cel..., the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends.

## Complexity detail
- **Time Complexity**: $O(mn)$ — Operation count bound.
- **Space Complexity**: $O(mn)$ — Auxiliary memory allocation bound.
