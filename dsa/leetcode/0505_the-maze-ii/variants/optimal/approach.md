## General
Given There is a ball in a `maze` with empty spaces (represented as `0`) and walls (represented as `1`). The ball can go through the empty spaces by rolling **up, down, left or right**, but it won't stop rolling until hitti..., the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends.

## Complexity detail
- **Time Complexity**: $O(rows \cdot cols \log(rows \cdot cols))$ — Operation count bound.
- **Space Complexity**: $O(rows \cdot cols)$ — Auxiliary memory allocation bound.
