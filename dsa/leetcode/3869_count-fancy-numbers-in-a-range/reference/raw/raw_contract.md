## Function Contract

**Inputs**

- `l`: The inclusive lower endpoint of the integer range.
- `r`: The inclusive upper endpoint, with `l <= r`.

Use each integer's ordinary decimal representation without leading zeros. For a number with digits $d_1,d_2,\ldots,d_k$, its digit sum is $d_1+d_2+\cdots+d_k$. A multi-digit sequence is strictly monotone only when every adjacent comparison points in the same strict direction; equal adjacent digits invalidate both directions.

**Return value**

Return an integer equal to the number of values $x$ satisfying $l\le x\le r$ for which $x$ is good, its digit sum is good, or both.
