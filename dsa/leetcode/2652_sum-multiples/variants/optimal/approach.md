## General

For a positive divisor $d$, let $q=\lfloor n/d\rfloor$. The divisible values at most $n$ are $d,2d,\ldots,qd$, so their sum is

$$
S(d)=d\frac{q(q+1)}{2}.
$$

Adding $S(3)$, $S(5)$, and $S(7)$ initially counts every qualifying integer, but values divisible by two chosen divisors are counted twice. Subtract the pairwise intersections, whose least common multiples are $15$, $21$, and $35$.

A value divisible by all three divisors was added three times and then subtracted three times, leaving it absent. Add the triple intersection, whose least common multiple is $105$, once. Inclusion-exclusion therefore gives

$$
S(3)+S(5)+S(7)-S(15)-S(21)-S(35)+S(105).
$$

Every integer divisible by at least one target divisor has final coefficient one, while every other integer has coefficient zero. The formula therefore sums exactly the required set without iterating through the range.

## Complexity detail

The algorithm evaluates the arithmetic-series helper for seven fixed divisors. Each evaluation uses a constant number of integer operations, so the total time is $O(1)$ and the auxiliary space is $O(1)$.

The benchmark uses `n` as its scaling size. A direct scan is a correct $O(n)$ alternative that finishes every legal tier but grows relative to the constant-time reference.

## Alternatives and edge cases

- **Direct scan:** Check every value from `1` through `n` and add it when any remainder is zero. This is simple and correct but takes $O(n)$ time.
- **Set of generated multiples:** Generate multiples of each divisor into a set before summing. It avoids duplicate counting but requires $O(n)$ time and space.
- Pairwise and triple overlaps must not be counted more than once; `15`, `21`, `35`, and `105` are the relevant least common multiples.
- When `n < 3`, no number qualifies and every arithmetic-series count is zero.
- The interval is inclusive, so `n` itself contributes when divisible by $3$, $5$, or $7$.
