## Function Contract

**Inputs**

- `nums`: A nonempty list of positive integers.
- `x`: A digit from `1` through `9` whose equality with both boundary digits of each subarray sum is tested.

For indices $0 \le l \le r < n$, `nums[l..r]` denotes the contiguous, nonempty interval beginning at `l` and ending at `r`. Its sum is positive, so its decimal representation has a well-defined first digit and last digit without a sign or leading zero.

**Return value**

Return the number of index pairs $(l,r)$ for which the decimal representation of $\sum_{i=l}^{r}\texttt{nums[i]}$ begins with `x` and ends with `x`.
