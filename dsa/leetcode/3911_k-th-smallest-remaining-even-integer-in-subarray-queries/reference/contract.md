## Function Contract

**Inputs**

- `nums`: A strictly increasing array of positive integers.
- `queries`: Query triples `[l, r, k]`, where `l` and `r` delimit an inclusive subarray and `k` is a one-based rank in the remaining-even sequence.

Let $n = \lvert\texttt{nums}\rvert$ and $q = \lvert\texttt{queries}\rvert$.

**Return value**

Return an array of length $q$. Its $i$-th value is the $k_i$-th smallest positive even integer left after removing the even values present in `nums[l_i..r_i]`.
