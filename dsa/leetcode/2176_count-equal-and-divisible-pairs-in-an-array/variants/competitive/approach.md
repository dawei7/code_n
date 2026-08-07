## General
Given a **0-indexed** integer array `nums` of length `n` and an integer `k`, return *the **number of pairs*** `(i, j)` *where* $0 \le i < j < n$, *such that* $\text{nums}[i] = \text{nums}[j]$ *and* $(i * j)$ *is divisible b..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n \sqrt{k})$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
