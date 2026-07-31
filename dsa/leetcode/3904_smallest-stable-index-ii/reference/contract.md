## Function Contract

**Inputs**

- `nums`: A non-empty array of non-negative integers.
- `k`: The inclusive upper limit on the instability score of a stable index.

For a candidate index $i$, both aggregate ranges contain `nums[i]`: the prefix is `nums[0..i]`, and the suffix is `nums[i..n - 1]`.

**Return value**

Return the least index $i$ for which

$$
\max(\texttt{nums}[0..i])-\min(\texttt{nums}[i..n-1])\le \texttt{k}.
$$

Return `-1` if no index meets this inequality.
