## Function Contract

**Inputs**

- `nums`: A circular integer array of length $n$.
- `k`: The minimum number of peaks required in the final array.

Each operation increases one chosen array element by $1$. Values may become larger than their original constraint range after operations. Peak comparisons use the two circular neighbors and are strict.

**Return value**

Return the fewest unit increases that can produce at least `k` peaks, or $-1$ if the requested count is impossible.
