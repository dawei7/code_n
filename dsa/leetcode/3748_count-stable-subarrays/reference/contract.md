## Function Contract

**Inputs**

- `nums`: The integer array whose contiguous subarrays are classified.
- `queries`: A list of inclusive index pairs `[l_i,r_i]` into `nums`.

Let $n=\texttt{nums.length}$ and $q=\texttt{queries.length}$. Each result counts subarrays by their index ranges, so equal-valued subarrays at different positions count separately.

**Return value**

Return $q$ integers, one per query, giving the number of nonempty, non-decreasing subarrays wholly contained in its requested segment.
