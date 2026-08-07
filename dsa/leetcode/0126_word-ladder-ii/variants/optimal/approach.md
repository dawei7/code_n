## General
Given A **transformation sequence** from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words $beginWord -> s_{1} -> s_{2} -> ... -> s_{k}$ such that:, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends.

## Complexity detail
- **Time Complexity**: $O(N + R)$ — Operation count bound.
- **Space Complexity**: $O(N + R)$ — Auxiliary memory allocation bound.
