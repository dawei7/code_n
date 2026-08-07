## Function Contract

**Inputs**

- `nums`: A non-empty array of positive integers that may be increased through contiguous-subarray operations.

Let $n = \lvert\texttt{nums}\rvert$.

**Return value**

Return the minimum sum of all positive increment values `x` needed to reach an array satisfying $\texttt{nums[i]} \le \texttt{nums[i + 1]}$ for every $0 \le i < n-1$. Return `0` when the input is already non-decreasing.
