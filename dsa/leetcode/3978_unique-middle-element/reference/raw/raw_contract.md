## Function Contract

`solve(nums) -> bool`

Let $n = \lvert\texttt{nums}\rvert$.

**Inputs**

- `nums`: An odd-length integer array. Its middle element is `nums[n // 2]` in the original order.

**Output**

Return `true` if `nums[n // 2]` has total frequency exactly one in `nums`; otherwise return `false`. The odd-length guarantee means the middle position always exists and is unique, including when $n = 1$.
