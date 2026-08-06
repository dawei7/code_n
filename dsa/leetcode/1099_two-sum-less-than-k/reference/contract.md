## Function Contract

**Inputs**

- `nums`: an array of $n$ integers.
- `k`: the exclusive upper bound for a pair sum.

The two chosen values must occupy distinct positions ordered as $i < j$. Equal numeric values may be paired when they occur at two different indices. A sum equal to `k` is not eligible.

**Return value**

Return the maximum `nums[i] + nums[j]` that is strictly less than `k`. Return `-1` if no eligible pair exists.
