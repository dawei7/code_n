## General
Given a **0-indexed** integer array `nums`, and you are allowed to **traverse** between its indices. You can traverse between index `i` and index `j`, $i \neq j$, if and only if $gcd(\text{nums}[i], \text{nums}[j]) > 1$, wh..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(M log log M + n log M)$ — Operation count bound.
- **Space Complexity**: $O(M + n)$ — Auxiliary memory allocation bound.
