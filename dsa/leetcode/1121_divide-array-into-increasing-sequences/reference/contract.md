## Function Contract

**Inputs**

- `nums`: a nonempty integer array of length $n$, sorted in non-decreasing order.
- `k`: the minimum permitted length of every resulting subsequence.

A valid division assigns every array occurrence to exactly one subsequence. Each subsequence retains the original relative order of its selected occurrences, has strictly increasing values, and contains at least `k` elements.

**Return value**

- `true` exactly when a valid division exists; otherwise, `false`.
