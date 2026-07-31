## Function Contract

**Inputs**

- `s`: A binary string of length $n$ containing only `0` and `1`.
- `strs`: An array of $m$ patterns. Every pattern has length $n$ and contains only `0`, `1`, and `?`.

A subsequence keeps the selected indices in their original order; the operation sorts only the characters selected at those indices.

**Return value**

Return a length-$m$ boolean array. Its element at index `i` is `true` exactly when at least one complete binary replacement of `strs[i]` is reachable from `s`; otherwise it is `false`.
