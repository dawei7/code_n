## Function Contract

**Inputs**

- `nums`: A nonempty array of nonnegative integers.

Let $N = \lvert\texttt{nums}\rvert$ and let $B = 30$, the number of bit positions needed to represent every permitted value from $0$ through $10^9$.

**Return value**

Return the maximum number of elements in a subsequence that is strictly increasing and whose cumulative bitwise AND is non-zero. A nonzero single element is a valid length-one subsequence. A zero by itself is not valid because its AND is zero.
