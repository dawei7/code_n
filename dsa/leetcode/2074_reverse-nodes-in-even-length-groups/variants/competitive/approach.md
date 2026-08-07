## General
Given the `head` of a linked list, the algorithm executes a single-pass linear scan through input elements. It utilizes linked list node pointers (`val`, `next`) to process sequential node chains. Edge case handling: guards against empty/null inputs via early returns, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
