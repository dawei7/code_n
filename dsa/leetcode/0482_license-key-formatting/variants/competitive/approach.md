## General
Given a license key represented as a string `s` that consists of only alphanumeric characters and dashes. The string is separated into $n + 1$ groups by `n` dashes. You are also given an integer `k`, the algorithm executes a single-pass linear scan through input elements. Edge case handling: guards against empty/null inputs via early returns, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
