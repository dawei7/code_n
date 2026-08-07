## General
Given A **ramp** in an integer array `nums` is a pair `(i, j)` for which `i < j` and $\text{nums}[i] \le \text{nums}[j]$. The **width** of such a ramp is $j - i$, the algorithm executes a single-pass linear scan through input elements. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(N)$ — Operation count bound.
- **Space Complexity**: $O(N)$ — Auxiliary memory allocation bound.
