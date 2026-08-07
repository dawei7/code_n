## Function Contract

**Inputs**

- `nums`: The cyclic array to divide into consecutive parts.
- `k`: The maximum number of subarrays in the partition.

Using fewer than `k` parts is permitted. A one-element part has range `0`.

For complexity notation, let $n=\texttt{nums.length}$ and

$$
q=\min\left(k,\left\lfloor\frac{n}{2}\right\rfloor\right).
$$

Only $q$ positive-range parts can matter because each such part needs at least two positions.

**Return value**

Return the maximum sum of subarray ranges over all cyclic partitions containing at most `k` parts.
