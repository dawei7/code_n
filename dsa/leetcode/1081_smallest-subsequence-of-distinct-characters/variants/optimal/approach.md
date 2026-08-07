## General
Given a string `s`, return *the **lexicographically smallest* *subsequence** of* `s` *that contains all the distinct characters of* `s` *exactly once*, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
