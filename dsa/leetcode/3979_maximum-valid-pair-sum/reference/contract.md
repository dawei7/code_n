## Function Contract

`solve(nums, k) -> int`

Let $n = \lvert\texttt{nums}\rvert$.

**Inputs**

- `nums`: A positive integer array whose values contribute to the pair sum.
- `k`: The minimum allowed index distance between the first and second selected positions.

**Output**

Return the maximum `nums[i] + nums[j]` over all indices satisfying $0 \le i < j < n$ and $j - i \ge k$. Indices, rather than value differences, determine validity.
