## General

Distinct primes are coprime, so the two-denomination Frobenius theorem applies.
For coprime positive integers $p$ and $q$, the greatest integer that cannot be
written as $xp+yq$ with nonnegative integers $x,y$ is

$$
pq-p-q.
$$

**Why the formula value is impossible.** If
$xp+yq=pq-p-q$, then $(x+1)p+(y+1)q=pq$. Reducing modulo $p$ shows that
$y+1$ must be a multiple of $p$, because $p$ and $q$ are coprime. Its term is
therefore already at least $pq$, while the positive $(x+1)p$ term remains, a
contradiction.

**Why every larger value is possible.** For an integer $t>pq-p-q$, choose the
unique $y$ from `0` through $p-1$ such that $yq\equiv t\pmod p`; these residues
exist because multiplication by $q$ permutes residues modulo $p$. Then
$x=(t-yq)/p$ is an integer. If $x$ were negative, the positive multiple
$yq-t$ of $p$ would be at least $p$, but the bounds $y\le p-1$ and
$t>pq-p-q$ make it at most $p-1$. Hence $x\ge0$, proving the representation.

Substituting the two given primes into the formula therefore returns exactly
the requested price.

## Complexity detail

The algorithm performs a fixed number of arithmetic operations, taking $O(1)$
time and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Reachability dynamic programming:** Marking every sum through the denomination product is correct under the bounds but takes $O(pq)$ time and space.
- **Scan each price with divisibility tests:** Searching until enough consecutive prices are reachable also does work proportional to the denomination values.
- **Coprimality requirement:** A greatest impossible price would not exist for denominations with a common divisor, but distinct primes guarantee gcd one.
- **Smallest primes:** For `2` and `3`, the formula returns `1`, the only impossible positive price.
- **Denomination order:** The formula is symmetric in the two primes.
- **Product bound:** The returned value fits comfortably in the declared integer range, though the proof does not depend on that implementation constraint.
