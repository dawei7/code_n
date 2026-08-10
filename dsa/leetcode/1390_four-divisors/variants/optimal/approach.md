## General

**Divisors arrive in pairs**

If positive integer $i$ divides $x$, then $x/i$ also divides $x$. One of the two values is at most $\sqrt{x}$ and the other is at least $\sqrt{x}$. Therefore checking candidate divisors only through the square root discovers every pair.

The helper `f(x)` begins by assuming the universal divisors 1 and $x$:

- `cnt = 2` records two divisors.
- `s = x + 1` records their sum.

It then tests possible smaller divisors starting at two. For normal $x>1$, this avoids rediscovering 1 and $x$.

For $x=1$, the initialization conceptually counts the same divisor twice. The loop does not run and `cnt` is not four, so the helper still correctly returns zero. A more general divisor routine might special-case one, but the exact four-divisor decision is unaffected.

**Why the loop condition reaches exactly the square root**

`while i <= x // i` is an integer-safe form of $i^2\le x$. In languages with fixed-width integers it avoids overflow from multiplying large `i` values. In Python overflow is not a concern, but the condition remains exact and avoids floating-point square roots.

For each `i` that divides `x`, the code adds `i` as one divisor. If `i * i != x`, the paired quotient `x // i` is different and is added as a second divisor. If $i^2=x$, the pair is the same middle divisor and must be counted only once.

For $x=21$, initialization records 1 and 21. Candidate 3 divides it and pairs with 7, bringing the count to four and the sum to 32. No other candidate divides it, so `f(21)` returns 32.

For $x=4$, candidate 2 is the square root. It is counted once, producing three divisors 1, 2, and 4. The helper returns zero because the number does not have exactly four.

**Why the helper does not stop at four**

Finding four divisors partway through is not enough; later factor pairs may raise the count beyond four. The code continues through the full square-root range and returns the sum only if final `cnt == 4`. This prevents numbers with six or more divisors from contributing an early partial sum.

It could stop early once `cnt > 4` because the count can never decrease, but the exact implementation favors simple complete enumeration. The asymptotic bound is unchanged.

**Summing across the input**

`sum(f(x) for x in nums)` calls the helper independently for every array occurrence. A qualifying number contributes its divisor sum; a nonqualifying number contributes zero.

Duplicate input values are separate elements and contribute repeatedly. Thus `[21,21]` returns $32+32=64$, matching the Reference.

**Why the algorithm is correct**

For $x>1$, the initialization records exactly divisors 1 and $x$. Every other divisor belongs to a pair $(i,x/i)$ with $2\le i\le\sqrt{x}$ for the smaller member. The loop visits every such possible `i`, adds both distinct pair members, and counts a perfect-square middle divisor once. Therefore final `cnt` and `s` are the exact divisor count and sum.

The helper returns that exact sum if and only if the count is four, otherwise zero. Summing these results includes precisely the divisor sums of qualifying array elements, with multiplicity, so the final answer is correct.

**The number-theory shape behind four divisors**

Unique prime factorization gives another perspective. A number has exactly four divisors only when it is either $p^3$ for a prime $p$, producing divisors $1,p,p^2,p^3$, or $pq$ for two distinct primes, producing $1,p,q,pq$. The enumeration does not need to factor numbers into primes explicitly; its count naturally recognizes both forms.

## Complexity detail

Let $m$ be the number of input elements and $V$ the maximum value. For one $x$, the helper tests $O(\sqrt{x})$ candidates. Across the array this is

$$
O\left(\sum_{x\in\texttt{nums}}\sqrt{x}\right)
\subseteq O(m\sqrt V).
$$

Only counters and arithmetic variables are used inside the helper, so auxiliary space is $O(1)$. The generator feeds one result at a time to `sum` and does not allocate a result list. These bounds match the manifest.

## Alternatives and edge cases

- **Prime-factor classification:** Factor $x$ and test whether its exponent pattern is either three or one-plus-one. It reaches a similar square-root bound but requires careful prime bookkeeping.
- **Sieve preprocessing:** Precompute divisor counts and sums for every value through $V$, then answer each array element in constant time. It can help for many inputs but uses $O(V)$ space.
- **Precompute $p^3$ and $pq$ forms:** Generate primes and map all four-divisor values to their sums. It leverages the classification but is more elaborate for a single array.
- **Early exit after count exceeds four:** Safe because divisor count only grows, though the exact code scans the full range.
- **`x = 1`:** It has one divisor and contributes zero despite the helper's harmless doubled initialization.
- **Prime number:** Only 1 and itself are found, so it contributes zero.
- **Prime cube:** Exactly one nonsquare or square-pair structure yields four total divisors and is accepted.
- **Product of two distinct primes:** Its one inner factor pair plus 1 and itself yields four.
- **Perfect square:** The square-root divisor is counted once, preventing a duplicate.
- **More than four divisors:** Full enumeration raises `cnt` beyond four, and the entire sum is discarded.
- **Duplicate array values:** Each occurrence contributes separately.
- **Integer loop bound:** `i <= x // i` avoids floating-point rounding and fixed-width multiplication overflow.
