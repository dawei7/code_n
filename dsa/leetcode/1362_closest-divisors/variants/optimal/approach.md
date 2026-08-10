## General

The answer must be a factor pair of either `num + 1` or `num + 2`. For a fixed product, factor pairs closest to each other lie closest to the square root. The helper searches downward from the integer square root and returns the first divisor it finds.

**Why the square root is the right starting point**

For positive `x`, any factor pair can be written as `(a, x // a)` with `a <= x // a`. The smaller factor then satisfies `a <= sqrt(x)`.

As `a` grows toward `sqrt(x)`, its paired factor `x / a` decreases toward the same value, reducing their difference. Therefore, among divisors no greater than the square root, the largest divisor produces the closest factor pair.

More explicitly, for real `a` in the interval from one through `sqrt(x)`, the difference is `x / a - a`. Increasing `a` makes the first term smaller and the second subtracted term larger, so the difference strictly decreases. Restricting `a` to actual integer divisors does not change that monotonic direction. The largest eligible divisor is therefore optimal.

The helper initializes its loop at `int(sqrt(x))` and checks values downward. The first `i` satisfying `x % i == 0` is the largest divisor at or below the square root. It returns `[i, x // i]`.

The loop always succeeds because one divides every positive integer. Prime values simply fall all the way to `i = 1` and return one with the number itself.

**Evaluate both permitted products**

`a = f(num + 1)` finds the closest pair for the first candidate product. `b = f(num + 2)` does the same for the second.

The final conditional compares `abs(a[0] - a[1])` with the corresponding difference for `b`. It returns `a` only when its difference is strictly smaller; otherwise it returns `b`.

If the two best differences tie, either pair is globally optimal because the problem only minimizes the absolute difference and allows the factors in any order. Choosing `b` on a tie is therefore valid.

For `num = 8`, the first product is nine. Starting at three immediately finds `3 * 3` with difference zero. The second product is ten; its closest pair is two and five with difference three. The method selects three and three.

For `num = 123`, the candidates are 124 and 125. The downward search for 124 finds four and thirty-one. The search for 125 finds five and twenty-five. Their differences are twenty-seven and twenty, so the method returns five and twenty-five.

The helper performs a fresh square-root search for each candidate. It cannot reuse the first factorization directly because consecutive integers may have completely different divisor structures.

**Why separate local optima give the global optimum**

Every valid answer belongs to exactly one of the two product choices. For each product, `f` returns the minimum-difference pair by choosing its largest divisor no greater than the square root. Comparing those two local minimum differences therefore selects the minimum across the entire allowed answer set.

The returned pair’s product is exact because the helper checks divisibility before using integer quotient. No floating approximate factor is returned.

The final strict comparison does not attempt another tie-break such as smaller factors or preferring `num + 1`. None is required by the contract. Returning the second pair on equality remains globally optimal.

## Complexity detail

For an input `x`, the helper examines at most $\lfloor\sqrt{x}\rfloor$ candidate divisors. It is called for `num + 1` and `num + 2`, so total time is $O(\sqrt{\texttt{num}})$.

The loop uses only scalar variables and returns two fixed-length lists. Auxiliary working space is $O(1)$, and the fixed two-element output is also constant-sized.

`sqrt` returns a floating-point value. For values around the stated maximum of one billion, its integer part is represented accurately enough for this use. A generalized implementation can use `math.isqrt` to obtain an exact integer square root without floating-point concerns.

## Alternatives and edge cases

- **Exact integer square root:** Start from `isqrt(x)`. It preserves the same search and complexity while avoiding floating rounding.
- **Scan upward from one:** It eventually finds all divisors but does not know the closest pair until reaching the square-root region.
- **Enumerate every factor pair:** Correct but unnecessary; the first divisor found in the downward search is already optimal for that product.
- **Prime candidate product:** The helper returns one and the prime.
- **Perfect square:** The square root divides exactly, producing equal factors and difference zero, the best possible.
- **Tie between products:** The source returns the `num + 2` pair because the comparison is strict; either tied pair satisfies the problem.
- **Return order:** The helper returns the smaller factor first, although the contract accepts either order.
- **Large `num`:** Only about the square root number of modulus tests are needed, not a scan through the product itself.
- **Guaranteed positive products:** Since `num >= 1`, both candidates are positive and divisor one always exists.
- **Floating start point:** The current constraints make it safe in practice, while `isqrt` is the robust general choice.
- **Candidate values differ by one:** Being numerically close does not imply their best factor gaps are close; both must be searched independently.
- **First successful divisor:** Continuing farther downward would only decrease the smaller factor and increase its partner, producing a larger gap.
