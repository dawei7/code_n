## General

The sequence of positive integers divisible by `a`, `b`, or `c` may be dense, and `n` can reach one billion. Generating qualifying numbers one by one is too slow. Instead, the solution asks a monotone counting question:

> How many ugly numbers are at most a candidate value $x$?

If that count is at least `n`, the $n$th ugly number is at most $x$. If it is smaller than `n`, the answer is larger. This monotonic boundary can be found with binary search.

**Count multiples without double counting**

There are $\lfloor x/a\rfloor$ positive multiples of `a` up to $x$, and similarly for `b` and `c`. Simply adding the three counts would count numbers divisible by two divisors twice and numbers divisible by all three three times.

The least common multiple identifies intersections. A number is divisible by both `a` and `b` exactly when it is divisible by `lcm(a, b)`. The code precomputes `ab`, `bc`, `ac`, and `abc`.

Inclusion-exclusion gives:

$$
F(x)=
\left\lfloor\frac{x}{a}\right\rfloor+
\left\lfloor\frac{x}{b}\right\rfloor+
\left\lfloor\frac{x}{c}\right\rfloor-
\left\lfloor\frac{x}{\operatorname{lcm}(a,b)}\right\rfloor-
\left\lfloor\frac{x}{\operatorname{lcm}(b,c)}\right\rfloor-
\left\lfloor\frac{x}{\operatorname{lcm}(a,c)}\right\rfloor+
\left\lfloor\frac{x}{\operatorname{lcm}(a,b,c)}\right\rfloor.
$$

The pair intersections are subtracted because they were counted twice. A number divisible by all three was initially added three times and then subtracted three times, leaving zero, so the triple intersection is added once to give the correct single count.

This formula handles divisors that share factors or divide one another. For example, when `c` is already a multiple of `a`, the LCM terms cancel the redundant subset correctly.

**Binary-search the first candidate with enough numbers**

The search interval starts at `l = 1` and ends at `r = 2 * 10**9`. The contract guarantees that the answer lies in this range.

At each step, `mid = (l + r) >> 1` computes the integer midpoint. A right shift by one is floor division by two for these nonnegative bounds.

If `F(mid) >= n`, then at least `n` ugly numbers occur by `mid`. The answer could equal `mid` or be smaller, so the code keeps `mid` by setting `r = mid`.

If `F(mid) < n`, then `mid` and every smaller value contain too few qualifying numbers. The code discards them with `l = mid + 1`.

The interval shrinks until `l == r`. The maintained boundary property makes this value the smallest integer $x$ such that $F(x)\geq n$.

**Why that lower bound is the nth ugly number**

As $x$ increases by one, `F(x)` increases by one exactly when $x$ is divisible by at least one divisor, and otherwise it does not change. Even if $x$ is divisible by several divisors, it represents one integer and inclusion-exclusion increases the union count only once.

Therefore, the first $x$ whose count reaches `n` is itself an ugly number and has exactly `n-1` ugly positive integers before it. It is the $n$th ugly number.

For `n = 4` with divisors two, three, and four, `F(5)=3` for values two, three, and four, while `F(6)=4` because six qualifies. Binary search locates six as the first sufficient candidate.

**Why precomputing LCMs matters**

The divisors do not change during the search. Computing their LCMs once keeps each count evaluation to a fixed number of integer divisions and additions. It also makes the inclusion-exclusion structure explicit.

## Complexity detail

Let $U=2\cdot10^9$ be the upper search bound.

Binary search halves the interval each iteration, so it performs $O(\log U)$ iterations—about 31 for this bound. Each iteration evaluates a constant-size inclusion-exclusion formula, taking $O(1)$ arithmetic operations under the usual integer model. Total time complexity is $O(\log U)$.

Computing the constant number of LCMs involves greatest-common-divisor arithmetic, which takes logarithmic time in divisor magnitude at the bit-operation level, but it is a one-time fixed count of operations and does not change the binary-search structure.

The algorithm stores four LCMs, two bounds, a midpoint, and scalar arithmetic results. Auxiliary-space complexity is $O(1)$.

Python integers avoid overflow. In fixed-width languages, computing an LCM as `a / gcd(a, b) * b` in that order and using a wide type is important because naive multiplication may overflow even when later division would reduce it.

## Alternatives and edge cases

- **Generate multiples with a heap:** Repeatedly take the next multiple and deduplicate overlaps. This needs work proportional to `n` and is infeasible when `n` is near one billion.
- **Merge three multiple sequences:** Three pointers still advance once per produced ugly number, so the same large-`n` problem remains.
- **One divisor divides another:** Inclusion-exclusion cancels the redundant multiples; no manual removal is needed.
- **All divisors equal:** Every pair and triple LCM equals that divisor, reducing the count to one ordinary multiple count.
- **`n = 1`:** Binary search finds the smallest among `a`, `b`, and `c`.
- **Overlapping multiples:** Pair LCM subtraction and triple LCM addition ensure each integer contributes once.
- **Upper-bound guarantee:** Setting `r` to two billion is safe only because the contract guarantees the result is within that interval.
- **Lower-bound update:** On a sufficient midpoint, keep `mid` with `r = mid`; using `mid - 1` would require a different binary-search invariant.
- **Modulo is not involved:** The answer itself must be returned exactly, so all counting and search arithmetic remains unmodified.
- **LCM overflow in fixed-width languages:** Divide by the GCD before multiplying and use 64-bit or wider intermediates.
