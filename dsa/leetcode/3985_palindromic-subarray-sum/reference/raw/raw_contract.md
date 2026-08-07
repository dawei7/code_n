## Function Contract

`solve(nums) -> int`

Let $n = \lvert\texttt{nums}\rvert$.

**Inputs**

- `nums`: A nonempty array of positive integers.

For indices $0 \le l \le r < n$, the subarray `nums[l..r]` is palindromic exactly when `nums[l + j] == nums[r - j]` for every valid offset $j$.

**Output**

Return the maximum element sum among all palindromic subarrays of `nums`. The result may exceed a 32-bit signed integer.
