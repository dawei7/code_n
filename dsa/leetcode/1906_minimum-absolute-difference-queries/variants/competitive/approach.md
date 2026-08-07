## General
Given The **minimum absolute difference** of an array `a` is defined as the **minimum value** of $|a[i] - a[j]|$, where $0 \le i < j < \text{a.length}$ and $a[i] \neq a[j]$. If all elements of `a` are the **same**, the mini..., the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O((n+q)V)$ — Operation count bound.
- **Space Complexity**: $O(nV)$ — Auxiliary memory allocation bound.
