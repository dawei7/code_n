## General
Given Design a Todo List Where users can add **tasks**, mark them as **complete**, or get a list of pending tasks. Users can also add **tags** to tasks and can filter the tasks by certain tags, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(q^2 log q)$ — Operation count bound.
- **Space Complexity**: $O(q + S)$ — Auxiliary memory allocation bound.
