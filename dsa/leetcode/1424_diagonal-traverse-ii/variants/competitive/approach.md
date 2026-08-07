## General
Given a 2D integer array `nums`, return *all elements of *`nums`* in diagonal order as shown in the below images*, the algorithm executes a single-pass linear scan through input elements. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(N)$ — Operation count bound.
- **Space Complexity**: $O(N)$ — Auxiliary memory allocation bound.
