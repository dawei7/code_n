## General
Given an integer array `nums` of size `n`. For **each** index `i` where $0 \le i < n$, define a subarray `nums[start ... i]` where $start = max(0, i - \text{nums}[i])$, the algorithm executes a single-pass linear scan through input elements.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
