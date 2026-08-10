## General

**Break motion into one-way traversals**

Moving from child 0 to child $n-1$ takes exactly $n-1$ seconds. The next $n-1$ seconds move back to child 0. Direction alternates after every traversal.

The code uses

`k, mod = divmod(k, n - 1)`.

After assignment:

- `k` is the number of complete end-to-end traversals;
- `mod` is the remaining steps into the next traversal.

Although reusing name `k` for the quotient is compact, it no longer holds the original seconds afterward.

**Map remainder according to direction**

After an even number of complete traversals, the ball is at child 0 and moving right. Remainder $r$ places it at child $r$, so return `mod`.

After an odd number, it is at child $n-1$ and moving left. Moving $r$ steps left gives

$$
n-1-r,
$$

implemented as `n - mod - 1`.

Parity test `k & 1` distinguishes these cases.

**Example**

For $n=3$, traversal length is 2. At $k=5$ seconds, quotient is 2 and remainder 1. Two traversals are even and return to child 0, then one step right reaches child 1.

For $n=5$, $k=6$ gives quotient 1 and remainder 2. One traversal ends at child 4, then two steps left reach child $4-2=2$.

**Relation to full period**

The complete position pattern repeats every $2(n-1)$ seconds. An equivalent formula first reduces time by that period and mirrors values greater than $n-1$.

The exact quotient-parity method avoids explicitly calculating a second modulus. Every pair of complete traversals has even parity and returns to the same position and direction.

**Triangle-wave interpretation**

Positions over time form

$$
0,1,2,\ldots,n-1,n-2,\ldots,1,0,1,\ldots
$$

This is a triangle wave, not circular motion. Modulo $n$ would be wrong because an endpoint reverses rather than wrapping.

Dividing by $n-1$ identifies which straight side contains the target time. The quotient selects its orientation and the remainder gives distance traveled along that side.

For $n=4$, traversal length is 3. Times 0 through 3 reach positions 0,1,2,3. Times 4 and 5 have odd quotient and remainders 1 and 2, giving positions 2 and 1. Time 6 has even quotient and remainder zero, returning position 0.

At an exact endpoint, remainder zero and quotient parity select the correct end. Direction is needed only to interpret the remainder; it need not be returned or stored afterward.

The two arithmetic branches are mirror images around the line's midpoint, which is why the same remainder works on both legs.


Inductively, after $q$ complete length-$(n-1)$ traversals, the ball is at child 0 for even $q$ and child $n-1$ for odd $q$. Direction is right in the even case and left in the odd case.

The division algorithm uniquely writes original seconds as $q(n-1)+r$ with $0\le r<n-1$. The remainder does not reach another endpoint, so direction stays fixed for those $r$ steps. The two return formulas are therefore exact.

**Endpoint times**

When remainder is zero, the ball is exactly at an endpoint. Even quotient returns 0; odd quotient returns $n-1$. Reversal affects the next pass, not the position at that instant.

The source constraint $n\ge2$ ensures divisor $n-1$ is positive.

**Why simulation is unnecessary**

Each second is fully predictable and the movement forms a triangle wave. Arithmetic jumps directly to the requested time, even if $k$ were far larger than the given bound.

Child indices, not counts, are returned; formulas remain within 0 through $n-1$ because remainder is less than $n-1$.

## Complexity detail

The method performs one `divmod`, one parity test, and constant arithmetic. Time is $O(1)$ and auxiliary space is $O(1)$.

The result is one integer. No queue or position history is stored.

Under arbitrary-precision analysis, division cost depends on integer bit length, but standard problem analysis treats bounded integer arithmetic as constant.

Input scalars are local; rebinding `k` has no caller-visible mutation.

## Alternatives and edge cases

- **Second-by-second simulation:** Correct but costs $O(k)$ time.
- **Modulo full period:** Let `r = k % (2*(n-1))` and return `r` on outbound leg or `2*(n-1)-r` on return leg.
- **Direction variable simulation:** Still unnecessary once traversal parity is known.
- **Remainder zero:** Ball is exactly at an endpoint.
- **k less than n-1:** Quotient is zero and result equals k.
- **k equals n-1:** Quotient one, remainder zero, result is last child.
- **Several complete periods:** Even pairs disappear through quotient parity.
- **n equals two:** Traversal length one; children alternate every second.
- **Positive k:** Time zero is not queried, though formula would return child zero.
- **Index bounds:** Both branches always return from 0 through $n-1$.
- **Variable shadowing:** Returned behavior uses quotient `k`, not original seconds, after `divmod`.
- **Same as pass-the-pillow:** The triangular periodic motion is identical despite different story wording.
- **Quotient parity as direction:** Every complete traversal of `n - 1` edges ends at the opposite endpoint. An even quotient means movement is forward from child zero; an odd quotient reflects the remainder from child `n - 1`.
