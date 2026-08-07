## Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers whose ordered index pairs are examined.

Only the earlier value `nums[i]` is reversed. The condition is therefore directional when a value ends in zero: `120` followed by `21` matches, whereas `21` followed by `120` does not.

**Return value**

Return the minimum value of $\lvert i-j\rvert$ over all mirror pairs `(i,j)` with $i<j$, or `-1` if there is no such pair.
