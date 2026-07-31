## Function Contract

**Inputs**

- `s`: The multiset of lowercase letters that the result must permute exactly.
- `target`: The equal-length string that the result must exceed lexicographically and strictly.

A palindromic permutation uses every character occurrence from `s` and reads identically from left to right and right to left. Equality with `target` is insufficient.

**Return value**

Return the smallest qualifying palindrome in lexicographic order, or `""` when no qualifying palindromic permutation exists.
