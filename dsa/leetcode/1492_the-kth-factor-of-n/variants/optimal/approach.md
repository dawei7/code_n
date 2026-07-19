## General
**Use the pairing around the square root**

Whenever $d$ divides $n$, the quotient $n/d$ is also a factor. One member of the pair is at most $\sqrt n$ and the other is at least $\sqrt n$. Therefore checking candidate divisors only through $\lfloor\sqrt n\rfloor$ discovers every factor pair.

The candidates $1,2,\ldots,\lfloor\sqrt n\rfloor$ are already in increasing order. Their successful divisors are exactly the small factors in increasing order. The paired quotients appear in the opposite order: as $d$ decreases, $n/d$ increases.

**Consume the small-factor ranks first**

Scan `divisor` upward from `1` through `isqrt(n)`. On every exact division, decrement `k`. If `k` becomes zero, the current divisor is the answer because all earlier successful candidates are precisely the smaller factors.

If the first scan ends with a positive `k`, the desired rank, if it exists, belongs to the large-factor half.

**Enumerate paired large factors without storing a list**

Scan the same divisor interval downward. For every divisor of $n$, its quotient `n // divisor` is a large factor, and the downward divisor order makes those quotients increase.

A perfect square needs special treatment. When `divisor * divisor == n`, the divisor and quotient are the same middle factor, which was already counted in the upward pass. Skip that quotient so the square root is not counted twice.

For every other factor pair, decrement the remaining `k` and return the quotient when it reaches zero. If the downward scan finishes first, $n$ has too few factors and the answer is `-1`.

**Why the two scans produce the complete sorted order**

Every factor $f$ belongs to exactly one pair $(d,n/d)$ with $d \le \sqrt n$. The upward scan emits all factors on the lower side in increasing order. For two small divisors $a < b$, their partners satisfy $n/b < n/a$; reversing the small-divisor scan therefore emits the upper-side partners in increasing order.

The only pair whose two members can coincide is $(\sqrt n,\sqrt n)$ for a perfect square, and the explicit skip removes its duplicate. Concatenating the conceptual outputs of the two scans is thus exactly the strictly increasing factor list. Rank decrements follow that order, so the returned value is precisely the requested factor.

**Why integer square root avoids boundary errors**

Use `isqrt(n)` rather than a floating-point square root. It returns the exact integer $\lfloor\sqrt n\rfloor$, so a perfect square cannot be rounded below its true root and lose the middle factor. The integer formulation directly matches the number-theoretic boundary.

## Complexity detail
Each scan examines at most $\lfloor\sqrt n\rfloor$ candidates and performs constant work per candidate, for $O(\sqrt n)$ time. Only counters and scalar arithmetic values are stored, so auxiliary space is $O(1)$.

The benchmark uses prime inputs and impossible large ranks, forcing the optimal implementation to complete both square-root scans and a correct linear baseline to examine all integers through $n$.

## Alternatives and edge cases
- **Linear enumeration:** test every integer from `1` through `n` and count divisors. It is simple and $O(1)$ space, but takes $O(n)$ time and does not satisfy the follow-up.
- **Collect all divisor pairs then sort:** discover factors through $\sqrt n$, append both members, sort, and index the result. This needs additional factor storage and sorting work.
- **Store only the small factors:** one upward scan plus reverse indexing into paired quotients also works in $O(\sqrt n)$ time, but requires $O(\sqrt n)$ space in the worst case.
- **Return a quotient during the upward scan:** incorrect for large-factor ranks because quotients discovered from increasing divisors are in decreasing order.
- **One:** `n = 1` has the single factor `1`.
- **Prime number:** the ordered factors are only `1` and `n`.
- **Perfect square:** count $\sqrt n$ once, not once as a divisor and again as its quotient.
- **Rank one:** every positive integer's first factor is `1`.
- **Last valid rank:** may return `n`, the partner of divisor `1`.
- **Rank beyond the factor count:** finish both scans and return `-1`.
- **One-based rank:** decrement on each factor before testing for zero; do not treat `k` as an array index.
