## General
Given an integer array `matches` where $\text{matches}[i] = [\text{winner}_{i}, \text{loser}_{i}]$ indicates that the player $\text{winner}_{i}$ defeated player $\text{loser}_{i}$ in a match, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(m + p log p)$ — Operation count bound.
- **Space Complexity**: $O(p)$ — Auxiliary memory allocation bound.
