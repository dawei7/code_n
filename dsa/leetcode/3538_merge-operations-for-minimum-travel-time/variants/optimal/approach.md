## General
Given a straight road of length `l` km, an integer `n`, an integer `k`**, **and **two** integer arrays, `position` and `time`, each of length `n`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a dynamic programming memoization table to cache intermediate subproblem states.

## Complexity detail
- **Time Complexity**: $O(n * k^3)$ — Operation count bound.
- **Space Complexity**: $O(n * k^2)$ — Auxiliary memory allocation bound.
