## Function Contract

**Inputs**

- `nums`: the integer array traversed by the window.
- `k`: the number of consecutive elements in every window.

Let $n = \lvert\texttt{nums}\rvert$. The contract guarantees that `k` is at least one and at most `n`, so every
window is nonempty and there are exactly $n-k+1$ window positions.

**Return value**

Return a floating-point list of length $n-k+1$. Entry $i$ is the median of `nums[i:i + k]`: the central ordered value
when `k` is odd, or the mean of the two central ordered values when `k` is even.
