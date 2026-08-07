## General
Given a **0-indexed** integer array `tasks`, where $\text{tasks}[i]$ represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the **same difficulty level**, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(u)$ — Auxiliary memory allocation bound.
