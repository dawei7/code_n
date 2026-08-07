## Function Contract

**Inputs**

- `nums`: The integer array whose non-empty contiguous subarrays are examined.

Let $n=\lvert\texttt{nums}\rvert$. Every legal value uses at most 30 bits because it lies between $0$ and $10^9$ inclusive.

For any subarray, each indexed occurrence is retained when testing whether its aggregate OR equals a value present in that same range. Equal values at different positions do not merge subarrays or witnesses.

**Return value**

Return the number of index intervals $[l,r]$ whose bitwise OR equals `nums[k]` for at least one index $k$ with $l\le k\le r$.
