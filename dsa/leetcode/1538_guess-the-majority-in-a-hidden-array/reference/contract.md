## Function Contract

**Inputs**

- `reader`: An `ArrayReader` for a hidden binary array of length $N$, where $5 \le N \le 10^5$.
- `reader.length()` returns $N$ in $O(1)$ time.
- `reader.query(a, b, c, d)` requires $0 \le a < b < c < d < N$ and returns `4`, `2`, or `0` according to the four-bit distribution.

**Return value**

Return any valid index of the majority bit in `nums`, or `-1` when the counts of zeros and ones are equal. The solution may make at most $2N$ calls to `query`.
