## General
Given a **0-indexed** binary string `s` which represents a sequence of train cars. $s[i] = '0'$ denotes that the $$i^{\text{th}}$$ car does **not** contain illegal goods and $s[i] = '1'$ denotes that the $$i^{\text{th}}$$ c..., the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a dynamic programming memoization table to cache intermediate subproblem states.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
