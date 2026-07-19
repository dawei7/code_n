## General
**Translate all-one notation into a geometric sum**

If `N` has $m + 1$ one digits in base `b`, then $N = 1 + b + b ^{2} + \ldots + b ^{m}$. For a fixed exponent `m`, this sum strictly increases with `b`, so at most one base can work and binary search is valid.

**Search longer representations first**

A longer all-one representation requires a smaller base. Iterate `m` from the largest possible value, `N.bit_length() - 1`, downward. The first exact geometric sum therefore uses the smallest good base.

**Use integer bounds and exact geometric sums**

For each exponent, binary-search from base two to a safe power-of-two upper bound for the integer `m`th root. Python's arbitrary-precision integers let each comparison evaluate $(b^{(m + 1)} - 1) / (b - 1)$ exactly. This avoids floating-point root rounding near exact powers; fixed-width implementations can instead extend the sum term by term and stop after exceeding `N`.

**Fall back to the universal two-digit representation**

Every $N > 2$ is `11` in base $N - 1$, so a solution always exists. If no representation with at least three digits is found, return $N - 1$.

## Complexity detail
There are $O(\log N)$ candidate exponents. Each performs $O(\log N)$ binary-search steps, and each comparison builds at most $O(\log N)$ powers, giving the conservative bound $O(\\log^{3} N)$. Only scalar integers are stored, so space is $O(1)$.

## Alternatives and edge cases
- **Floating-point root candidates:** testing integers around $N^{\frac{1}{m}}$ is faster in practice but needs safeguards against rounding.
- **Extend every sum term by term:** this avoids large intermediate powers in fixed-width languages, but in Python its explicit exponent-length loop adds growth that the exact geometric-series formula delegates to optimized exponentiation.
- **Try every base upward:** is correct but can require `Theta(N)` candidates when only base $N - 1$ works.
- **Closed-form quadratic for three digits:** handles $1 + b + b^{2}$ but does not replace the general exponent search.
- **Mersenne number:** $2^{q} - 1$ has the smallest possible base two.
- **No longer representation:** return $N - 1$ for the two-digit `11` form.
- **Large input:** integer arithmetic prevents precision loss near $10^{18}$.
- **Search order:** longest representation must be checked first to guarantee the smallest base.
