## Function Contract

**Inputs**

- `nums`: The integer array in which the contiguous subarray is selected.
- `k`: The minimum permitted subarray length.

**Return value**

Return the maximum value of

$$
\frac{\text{sum of the selected contiguous subarray}}{\text{length of that subarray}}
$$

over all contiguous subarrays of length at least `k`. The returned floating-point value must have calculation error less than $10^{-5}$.
