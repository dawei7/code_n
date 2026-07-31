## Function Contract

**Inputs**

- `nums`: An integer array of length $n$.
- `p`: The exact GCD required from a good subsequence.
- `queries`: A list of point updates. Each entry is `[ind_i, val_i]` and assigns `nums[ind_i] = val_i`.

Queries are processed from left to right on the same mutable logical array. A selected subsequence must contain at least one element, may skip arbitrary positions, and must omit at least one of the $n$ array elements.

**Return value**

Return the number of updates after which at least one non-empty proper subsequence has GCD exactly `p`.
