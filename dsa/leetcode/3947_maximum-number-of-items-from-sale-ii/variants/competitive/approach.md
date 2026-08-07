## General
Given a 2D integer array `items`, where $\text{items}[i] = [\text{factor}_{i}, \text{price}_{i}]$ represents the $$i^{\text{th}}$$ item. You are also given an integer `budget`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
