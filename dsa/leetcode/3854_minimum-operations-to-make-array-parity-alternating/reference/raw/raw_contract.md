## Function Contract

**Inputs**

- `nums`: A nonempty array of integers.

If $N=\lvert\texttt{nums}\rvert$, the resulting array must satisfy

$$
\texttt{nums[i]}\bmod 2 \ne \texttt{nums[i+1]}\bmod 2
$$

for every $0\le i<N-1$. Each operation adds either `1` or `-1` to one chosen element.

The operation count is optimized first. Only arrays obtained with exactly that optimal count participate in the separate minimization of the final range.

**Return value**

Return `[minimum operations, minimum final range]`, where the range is the final maximum element minus the final minimum element.
