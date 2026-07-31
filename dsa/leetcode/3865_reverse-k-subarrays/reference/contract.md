## Function Contract

**Inputs**

- `nums`: A nonempty array of integers.
- `k`: The number of equal-length contiguous subarrays into which `nums` is partitioned.

Let $N=\lvert\texttt{nums}\rvert$ and $B=N/k$. The divisibility guarantee makes $B$ an integer. Block $b$, for $0 \le b < k$, consists of the original positions from $bB$ through $(b+1)B-1$, inclusive. Reversal changes order only within those boundaries.

**Return value**

Return the length-$N$ array formed by reversing each of the `k` blocks and concatenating the blocks from left to right.
