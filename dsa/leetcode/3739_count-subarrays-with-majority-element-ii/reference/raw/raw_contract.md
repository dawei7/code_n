## Function Contract

**Inputs**

- `nums`: The integer array whose non-empty contiguous subarrays are examined.
- `target`: The value that must be a strict majority in a counted subarray.

For a subarray of length $L$, let $f$ be the number of positions whose value equals `target`. The subarray is counted precisely when $2f > L$.

**Return value**

Return the total number of subarrays for which `target` satisfies that strict-majority condition. The count can be as large as $n(n+1)/2$, which exceeds a 32-bit signed integer when $n$ is near its upper bound.
