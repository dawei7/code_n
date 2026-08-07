## General
Given a 2D integer array `logs` where each $\text{logs}[i] = [\text{birth}_{i}, \text{death}_{i}]$ indicates the birth and death years of the $$i^{\text{th}}$$ person, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n+Y)$ — Operation count bound.
- **Space Complexity**: $O(Y)$ — Auxiliary memory allocation bound.
