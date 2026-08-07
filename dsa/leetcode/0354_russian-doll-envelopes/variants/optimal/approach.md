## General
Given a 2D array of integers `envelopes` where $\text{envelopes}[i] = [w_{i}, h_{i}]$ represents the width and the height of an envelope, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n \log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
