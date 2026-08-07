## General
Given a **0-indexed** 2D integer array `flowers`, where $\text{flowers}[i] = [\text{start}_{i}, \text{end}_{i}]$ means the $$i^{\text{th}}$$ flower will be in **full bloom** from $\text{start}_{i}$ to $\text{end}_{i}$ (**in..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O((F + P) log F)$ — Operation count bound.
- **Space Complexity**: $O(F)$ — Auxiliary memory allocation bound.
