## Function Contract

**Inputs**

- `reader`: A read-only `ArrayReader` for an array of length $N$, where $2 \leq N \leq 5 \cdot 10^5$.
- Every hidden value is an integer; exactly one value is strictly larger than all other identical values.
- `reader.length()` returns $N$ in $O(1)$ time.
- `reader.compareSub(l, r, x, y)` compares two valid inclusive subarray sums in $O(1)$ time: returns 1 if `sum(l..r) > sum(x..y)`, 0 if equal, and -1 if `sum(l..r) < sum(x..y)`.

**Return value**

Return the zero-based index of the unique larger value while making at most 20 calls to `compareSub`.
