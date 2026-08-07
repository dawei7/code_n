## Function Contract

**Inputs**

- `nums`: A nonempty integer array whose fixed consecutive blocks may be cyclically rotated.

Let $n = \lvert\texttt{nums}\rvert$, and let $D$ be the number of positive divisors of $n$.

For a candidate $k$, the partition consists of `nums[0:k]`, `nums[k:2*k]`, and so on. Each block may be rotated independently, but its values cannot move to another block.

**Return value**

Return the sum of all positive divisors $k$ of $n$ for which the permitted block rotations can make `nums` non-decreasing.
