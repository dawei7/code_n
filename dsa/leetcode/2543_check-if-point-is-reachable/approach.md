## General

**The greatest common divisor captures reachability**

The exact criterion is:

$$
\gcd(\texttt{targetX},\texttt{targetY})
\text{ is a power of two}.
$$

The method computes the gcd and applies the standard power-of-two bit test.

Understanding why requires tracking what the permitted coordinate operations can do to common prime factors.

**Subtraction preserves the gcd**

For all integers `x` and `y`:

$$
\gcd(x,y-x)=\gcd(x,y),
$$

and symmetrically

$$
\gcd(x-y,y)=\gcd(x,y).
$$

Any common divisor of `x` and `y` divides their difference, and any common divisor of `x` and `y-x` also divides `(y-x)+x=y`. The sets of common divisors are identical.

Therefore, the two subtraction moves never change the gcd.

**Doubling can introduce only factor two**

Consider replacing `x` by `2x`. Any odd prime dividing both `2x` and `y` already divides `x` and `y`, so it was already present in the old gcd.

The only new prime factor that doubling can introduce into the gcd is 2. The same reasoning applies when doubling `y`.

Starting from `gcd(1,1)=1`, no odd prime can ever appear in the coordinate gcd. Any reachable positive target must have gcd

$$
1,2,4,8,\ldots,
$$

a power of two. This proves necessity.

**Why the condition is also sufficient**

The allowed operations are powerful enough to generate every coprime positive coordinate pair from `(1,1)` through sequences of doubling and subtraction; this is the constructive reachability lemma behind the solution. Intuitively, doublings provide a sufficiently large power-of-two scale, while Euclidean-style subtractions shape the two coordinates without changing their odd gcd structure.

If target coordinates have gcd $2^t$, write

$$
(\texttt{targetX},\texttt{targetY})
=
2^t(a,b),
\qquad \gcd(a,b)=1.
$$

Reach the coprime pair `(a,b)` using the lemma, then introduce the common factor $2^t$ by doubling both coordinates `t` times. Each coordinate doubling is an allowed step. This reaches the target.

Thus absence of odd gcd factors is both necessary and sufficient.

**The power-of-two bit pattern**

A positive power of two has binary form with exactly one set bit:

$$
1000\ldots0.
$$

Subtracting one flips that set bit to zero and all lower bits to one:

$$
0111\ldots1.
$$

The two values share no set bit, so

`x&(x-1)==0`.

For a positive non-power-of-two, at least two bits are set. Subtracting one clears only the lowest set bit while a higher set bit remains in both values, so their AND is nonzero.

**Read the exact expression**

`x=gcd(targetX,targetY)` is positive because both targets are at least one.

Python evaluates bitwise AND before the equality comparison, so

`x & (x-1) == 0`

means

`(x & (x-1)) == 0`.

The usual bit trick also accepts zero, but zero cannot arise as this gcd under the input contract.

**Trace the examples**

For target `(6,9)`:

$$
\gcd(6,9)=3,
$$

which has odd prime factor 3 and binary form `11`. `3&2=2`, so the method returns false.

For `(4,7)`:

$$
\gcd(4,7)=1=2^0.
$$

The bit test passes, consistent with the explicit path in the statement.

**Why coordinate size does not require grid search**

The grid is infinite and targets reach $10^9$. Breadth-first search would explore an unbounded state space. The gcd invariant condenses the entire reachability question to logarithmic arithmetic.

**A closer look at one-coordinate doubling**

Write `x=g*a` and `y=g*b` with `g=gcd(x,y)` and `gcd(a,b)=1`. After doubling `x`,

$$
\gcd(2x,y)
=
g\gcd(2a,b).
$$

Because `a` and `b` are coprime, `gcd(2a,b)` can only be one or two. The new gcd is therefore either `g` or `2g`. This proves formally that a doubling can preserve the gcd or add one factor of two, but can never introduce an odd prime.

Repeated doublings consequently keep the gcd in the family of powers of two that began at one.


Subtractions preserve all gcd factors, and doublings can add only factor two, so every reachable target passes the test. The constructive lemma for coprime pairs plus common doublings reaches every target whose gcd is a power of two. The bit expression recognizes exactly those positive gcd values.

## Complexity detail

Euclid's gcd algorithm takes

$$
O(\log\min(\texttt{targetX},\texttt{targetY}))
$$

time. The power-of-two check is constant time.

Only the gcd value is stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Repeatedly divide gcd by two:** Remove factors of two and test whether the remainder is one; equivalent but longer than the bit trick.
- **Grid search:** The state space is infinite and infeasible.
- **Gcd one:** It is $2^0$ and always passes.
- **Equal target coordinates:** Reachable exactly when that common coordinate is a power of two.
- **Odd gcd above one:** It contains an odd factor and fails.
- **One coordinate equal to one:** Gcd is one, so the target is reachable.
- **Positive-input guarantee:** It prevents gcd zero.
- **Subtraction moves:** They preserve gcd exactly.
- **Doubling moves:** They cannot introduce odd common primes.
- **Operator precedence:** The expression tests `(x&(x-1))==0`.
