## Function Contract

**Inputs**

- `s`: The multiset of lowercase letters that must all appear in the result, including their original multiplicities.
- `target`: The equal-length lowercase string that the result must exceed strictly.

**Return value**

Return the lexicographically smallest qualifying permutation of `s`, or `""` when even the greatest permutation of `s` is not strictly greater than `target`.
