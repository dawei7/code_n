## General
Given There is a line chart consisting of `n` points connected by line segments. You are given a **1-indexed** integer array `y`. The $$k^{\text{th}}$$ point has coordinates $(k, y[k])$. There are no horizontal lines; that ..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(N log N)$ — Operation count bound.
- **Space Complexity**: $O(N)$ — Auxiliary memory allocation bound.
