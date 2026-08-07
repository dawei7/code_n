## General
Given two integer arrays `persons` and `times`. In an election, the $$i^{\text{th}}$$ vote was cast for $\text{persons}[i]$ at time $\text{times}[i]$, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(v+r\log v)$ — Operation count bound.
- **Space Complexity**: $O(v)$ — Auxiliary memory allocation bound.
