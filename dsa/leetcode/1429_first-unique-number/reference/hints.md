## Hints

1. Keep the values that are unique now in a doubly linked list, and map each such value to its list node. A first occurrence can be appended; when a value repeats, remove its node if it is present. The list head then answers `showFirstUnique()`.
2. A queue can also work if its front is maintained as a value that is still unique.
3. A set or heap offers another route with $O(\log n)$ operations.
