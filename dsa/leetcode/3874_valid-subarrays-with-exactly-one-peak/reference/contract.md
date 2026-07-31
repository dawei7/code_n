## Function Contract

**Inputs**

- `nums`: The integer array whose contiguous subarrays are counted.
- `k`: The maximum allowed distance from the unique contained peak to either selected endpoint.

Peak status is evaluated in the complete input array, not relative to a selected subarray. Therefore a length-one subarray containing a global peak contains exactly one peak even though that element has no neighbors inside the subarray.

Let $n=\lvert\texttt{nums}\rvert$.

**Return value**

Return the total number of index intervals `[l, r]` that contain exactly one original-array peak `i` and satisfy both distance bounds.
