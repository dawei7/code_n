## General
Given an array of strings `words` (**without duplicates**), return *all the **concatenated words** in the given list of* `words`, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(sum(|word|^2))$ — Operation count bound.
- **Space Complexity**: $O(sum(|word|))$ — Auxiliary memory allocation bound.
