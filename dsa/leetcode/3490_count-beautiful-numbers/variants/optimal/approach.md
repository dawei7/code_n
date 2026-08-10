## General

**Split numbers by whether they contain digit zero.** For every positive integer, the digit sum is positive. If any digit is zero, the digit product is zero, and

$$
0\bmod(\text{positive digit sum})=0.
$$

Therefore, every positive number containing a zero is automatically beautiful. The source counts these numbers separately from beautiful numbers whose digits are all nonzero.

For an upper bound $B$, function `count(B)` computes

`B - count_without_zero(B) + count_nonzero_beautiful(B)`.

There are exactly $B$ positive integers from one through $B$. Subtracting the count with no zero leaves all zero-containing integers, each automatically beautiful. The final term adds back exactly the beautiful members of the no-zero group. The groups are disjoint.

The requested inclusive range is then the standard prefix-count difference `count(r) - count(l - 1)`.

**Count no-zero integers up to a bound directly.** `count_without_zero` first includes every shorter length:

$$
\sum_{\ell=1}^{D-1}9^\ell,
$$

because each of $\ell$ positions can be any digit one through nine.

For length $D$, it scans the bound's digits from left to right. At a position whose bound digit is $d>0$, choosing a smaller nonzero digit gives $d-1$ choices, followed by any of $9^{remaining}$ nonzero suffixes. These numbers are added, and scanning continues along the equal-bound prefix.

If the bound digit is zero, no no-zero number can continue with the same prefix, so every eligible number has already been counted and the function returns. If the full scan finishes, the bound itself has no zero and `+1` includes it.

This is a compact digit-counting routine rather than a DP.

**For nonzero digits, test divisibility through the digit sum.** A number is beautiful when its digit product is divisible by its digit sum. The maximum sum for a $D$-digit bound is $9D$, so `count_nonzero_beautiful` enumerates each possible `target_sum` from one through $9D$.

A product of nonzero decimal digits can have only prime factors $2,3,5,7$. If `target_sum` contains any other prime factor, it cannot divide such a product. The source repeatedly divides the candidate sum by $2,3,5,7$ and skips it unless the leftover becomes one.

This filter avoids running digit DP for impossible sums such as $11$.

**Track how much of the target sum still must divide the product.** For one feasible `target_sum`, memoized state is

`dp(position, digit_sum, missing_factor, tight, started)`.

`missing_factor` begins as `target_sum`. When choosing nonzero digit $d$, the source updates it to

$$
\frac{missing\_factor}
{\gcd(missing\_factor,d)}.
$$

The greatest common divisor removes exactly the prime-factor contribution supplied by this digit that is still needed. Repeating over all digits makes `missing_factor == 1` exactly when the full digit product contains every prime power required by `target_sum`.

For example, if the target is $12$ and a digit $6$ is chosen, the missing factor falls to $2$; a later even digit removes that last factor. Extra prime factors in the product are harmless because divisibility needs at least the target factors, not equality.

**Use ordinary digit-DP controls for the bound and shorter numbers.** `tight` says the prefix still equals the bound's prefix. Its digit limit is the bound digit when tight and nine otherwise. `next_tight` stays true only after choosing that exact limiting digit.

`started` distinguishes leading padding zeros from actual number digits. While not started, choosing zero advances without changing sum or product requirements. This lets one $D$-position DP represent positive numbers of every shorter length. After the number has started, the transition deliberately accepts only `digit != 0`, because this function counts the no-zero group.

At the final position, a state contributes one only if a positive number started, its digit sum equals `target_sum`, and its product has supplied the entire `missing_factor`.

The pruning condition rejects a state if its current sum already exceeds the target or even filling every remaining position with nine cannot reach it. The variable `remaining` includes the current position, so `digit_sum + 9 * remaining` is the maximum still possible.

**Why summing target-specific DPs does not double-count.** Every positive number has exactly one digit sum. It appears only in the iteration whose `target_sum` equals that sum. Within that iteration, each digit sequence corresponds to one number and is accepted exactly when its product is divisible by the sum. Thus `answer` counts every no-zero beautiful number exactly once.

Numbers containing zero never enter this DP after they start; they are already counted by the complement term. This separation also avoids representing a zero product with prime-factor state.

For $10$ through $20$, the zero-containing values $10$ and $20$ are automatically included. Other values in that interval fail the no-zero product-divisibility test, giving count two.

**Overall correctness.** The no-zero counter partitions all positive integers into zero-containing and nonzero-digit groups. Every member of the first group is beautiful. For the second group, target-sum enumeration, digit DP, and missing-factor reduction accept exactly those whose product is divisible by their sum. Prefix subtraction then restricts the exact count to $[l,r]$.

## Complexity detail

Let $D$ be the number of decimal digits, at most nine here. There are $O(D)$ target sums. For one target, the memo state ranges over $O(D)$ positions, $O(D)$ digit sums, and a bounded family of `missing_factor` divisors whose coarse size can be treated as $O(D)$ for the stated target range, with constant tight/started flags. Each state tries ten digits.

This gives the manifest's coarse $O(D^4)$ total time across target sums and $O(D^3)$ peak cached state for one target. The cache is defined anew inside each target iteration, so caches from all target sums are not intentionally retained together.

The direct `count_without_zero` routine costs only $O(D)$. `count` runs twice, for $r$ and $l-1$, which changes only a constant factor.

Since $D\le9$, these polynomial-in-digit-count bounds are small and independent of the numeric width of the interval $r-l$.

## Alternatives and edge cases

- **Iterate every integer in \([l,r]\):** The interval can contain almost a billion values, so direct checking is infeasible.
- **One DP state storing the full digit product:** Products grow rapidly and create many states; tracking only missing factors of the target sum is much smaller.
- **Include zero digits in the factor DP:** Their product makes divisibility automatic, so counting them by complement is simpler and avoids a special absorbing product state.
- **Skip the target-prime filter:** Correctness remains, but DP work is wasted on sums containing primes that nonzero decimal digits can never supply.
- **Leading zeros:** They represent shorter numbers and do not count as actual zero digits in the number.
- **Number zero:** The domain is positive; `started` must be true at the terminal state, so zero is excluded.
- **Bound containing zero:** `count_without_zero` stops at the first zero after counting all smaller valid prefixes.
- **Digit sum one:** `missing_factor` starts at one, so every no-zero number with sum one passes the product condition.
- **Repeated prime factors:** Successive gcd divisions correctly accumulate factors supplied by several digits.
- **Product with extra factors:** Once `missing_factor` reaches one, additional digits keep it one and divisibility remains true.
- **Inclusive lower endpoint:** Subtracting `count(l - 1)` preserves numbers equal to `l`.
- **Small bound:** Helpers return zero for nonpositive bounds, making `l=1` safe.
