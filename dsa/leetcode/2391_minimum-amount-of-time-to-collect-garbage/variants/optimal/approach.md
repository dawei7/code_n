## General
Given a **0-indexed** array of strings `garbage` where $\text{garbage}[i]$ represents the assortment of garbage at the $$i^{\text{th}}$$ house. $\text{garbage}[i]$ consists only of the characters `'M'`, `'P'` and `'G'` repr..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n + S)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
