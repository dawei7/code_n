## Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.
- `k`: The exact number of distinct integers required in a counted subarray.
- `m`: The minimum frequency required for each distinct integer inside that
  subarray.

Let $N = \lvert\texttt{nums}\rvert$ and $K = \texttt{k}$. A subarray is a
contiguous interval `nums[left:right + 1]`; no elements may be skipped. Both
the exact-distinct-count rule and the per-value frequency rule are evaluated
within that interval alone.

**Return value**

Return the number of subarrays that contain exactly $K$ distinct integers and
give each of those integers a frequency of at least `m`.
