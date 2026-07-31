## Function Contract

**Inputs**

- `nums`: A non-empty array of non-negative integers.
- `k`: The inclusive upper bound for a stable index's instability score.

Both ranges used at index $i$ include `nums[i]`: the prefix is `nums[0..i]`, and the suffix is `nums[i..n - 1]`.

**Return value**

Return the least index $i$ satisfying

$$
\max(\texttt{nums}[0..i])-\min(\texttt{nums}[i..n-1])\le \texttt{k}.
$$

Return `-1` when no index satisfies the inequality.
