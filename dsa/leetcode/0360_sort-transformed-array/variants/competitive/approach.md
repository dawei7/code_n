## General
Given a **sorted** integer array `nums` and three integers `a`, `b` and `c`, apply a quadratic function of the form $f(x) = ax^2 + bx + c$ to each element $\text{nums}[i]$ in the array, and return *the array in a sorted order*, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
