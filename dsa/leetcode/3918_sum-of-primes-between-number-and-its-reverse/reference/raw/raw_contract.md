## Function Contract

**Inputs**

- `n`: The positive integer whose decimal digits are reversed to obtain the other endpoint.

Let `r` be the integer obtained by reversing the digits of `n`, $L=\min(\texttt{n},r)$, and $U=\max(\texttt{n},r)$.

**Return value**

Return the sum of all primes $p$ satisfying $L\le p\le U$. Return `0` when the interval contains no prime.
