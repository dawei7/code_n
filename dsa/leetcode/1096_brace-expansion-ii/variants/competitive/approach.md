## General
Given Under the grammar given below, strings can represent a set of lowercase words. Let `R(expr)` denote the set of words the expression represents, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time.

## Complexity detail
- **Time Complexity**: $O(E + S + RL \log R)$ — Operation count bound.
- **Space Complexity**: $O(E + S)$ — Auxiliary memory allocation bound.
