## General
Given an array of strings `patterns` and a string `word`, return *the **number** of strings in *`patterns`* that exist as a **substring** in *`word`, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time, a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(T+PM)$ — Operation count bound.
- **Space Complexity**: $O(L)$ — Auxiliary memory allocation bound.
