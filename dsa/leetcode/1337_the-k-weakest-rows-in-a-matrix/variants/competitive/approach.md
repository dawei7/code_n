## General
Given an `m x n` binary matrix `mat` of `1`'s (representing soldiers) and `0`'s (representing civilians). The soldiers are positioned **in front** of the civilians. That is, all the `1`'s will appear to the **left** of all ..., the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(m\log n+m\log m)$ — Operation count bound.
- **Space Complexity**: $O(m)$ — Auxiliary memory allocation bound.
