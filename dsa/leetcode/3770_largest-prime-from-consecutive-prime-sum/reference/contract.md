## Function Contract

**Inputs**

- `n`: The inclusive upper bound for both the returned prime and its consecutive-prime sum.

Let $N=\texttt{n}$, and list the primes as $p_1=2,p_2=3,p_3=5,\ldots$. The only candidate sums are the prefixes $S_j=\sum_{i=1}^{j}p_i$.

**Return value**

Return the largest $S_j\leq N$ that is prime. Return `0` when no such prefix sum exists; in particular, this occurs when `n = 1`.
