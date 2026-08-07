## General
Given a **0-indexed** array of positive integers `tasks`, representing tasks that need to be completed **in order**, where $\text{tasks}[i]$ represents the **type** of the $$i^{\text{th}}$$ task, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
