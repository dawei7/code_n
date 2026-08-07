## General
Given A **transformation sequence** from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words $beginWord -> s_{1} -> s_{2} -> ... -> s_{k}$ such that:, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends.

## Complexity detail
- **Time Complexity**: $O(N)$ — Operation count bound.
- **Space Complexity**: $O(N)$ — Auxiliary memory allocation bound.
