## General
Given a binary array `nums` containing only the integers `0` and `1`. Return* the number of **subarrays** in nums that have **more** *`1`'*s than *`0`*'s. Since the answer may be very large, return it **modulo** *$10^{9} + 7$, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a dynamic programming memoization table to cache intermediate subproblem states. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(N)$ — Operation count bound.
- **Space Complexity**: $O(N)$ — Auxiliary memory allocation bound.
