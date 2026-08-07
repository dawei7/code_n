## General
Given a string `s` and an integer `k`, partition `s` into `k` **substrings** such that the letter changes needed to make each substring a **semi-palindrome** are minimized, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n^3 log(n) + k n^2)$ — Operation count bound.
- **Space Complexity**: $O(n^2 + k n)$ — Auxiliary memory allocation bound.
