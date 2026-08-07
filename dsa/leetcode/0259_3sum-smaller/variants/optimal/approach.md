## General
Given an array of `n` integers `nums` and an integer `target`, find the number of index triplets `i`, `j`, `k` with $0 \le i < j < k < n$ that satisfy the condition $\text{nums}[i] + \text{nums}[j] + \text{nums}[k] < target$, the algorithm executes a single-pass linear scan through input elements.

## Complexity detail
- **Time Complexity**: $O(n^2)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
