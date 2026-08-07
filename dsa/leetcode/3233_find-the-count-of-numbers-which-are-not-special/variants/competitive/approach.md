## General
Given 2 **positive** integers `l` and `r`. For any number `x`, all positive divisors of `x` *except* `x` are called the **proper divisors** of `x`, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window.

## Complexity detail
- **Time Complexity**: $O(sqrt(r) log log sqrt(r))$ — Operation count bound.
- **Space Complexity**: $O(sqrt(r))$ — Auxiliary memory allocation bound.
