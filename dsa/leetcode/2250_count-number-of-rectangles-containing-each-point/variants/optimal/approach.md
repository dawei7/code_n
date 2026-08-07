## General
Given a 2D integer array `rectangles` where $\text{rectangles}[i] = [l_{i}, h_{i}]$ indicates that $$i^{\text{th}}$$ rectangle has a length of $l_{i}$ and a height of $h_{i}$. You are also given a 2D integer array `points` ..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(R log R + P H log R)$ — Operation count bound.
- **Space Complexity**: $O(R + H)$ — Auxiliary memory allocation bound.
