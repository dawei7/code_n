## General
Given a string `s` that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time.

## Complexity detail
- **Time Complexity**: $O(2^p \cdot n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
