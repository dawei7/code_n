## Function Contract

**Inputs**

- `nums`: The positive integer array to divide into two nonempty contiguous parts.

A split after index $i$ produces `left = nums[0..i]` and `right = nums[i+1..n-1]`. Adjacent values in `left` must increase strictly; adjacent values in `right` must decrease strictly.

**Return value**

Return the minimum value of $\lvert\operatorname{sum}(\texttt{left})-\operatorname{sum}(\texttt{right})\rvert$ over valid splits, or `-1` if none exists.
