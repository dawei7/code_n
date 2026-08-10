## General

An ugly number is defined entirely by its prime factors: it must be positive, and every prime in its factorization must belong to `{2, 3, 5}`. The exact solution follows that definition directly. It removes every occurrence of each allowed factor, then checks whether anything remains.

**Reject nonpositive values before division**

The first condition is `if n < 1: return False`. Negative integers and zero are not positive, so they cannot be ugly.

This guard is also operationally essential for zero. Since `0 % 2 == 0` and `0 // 2 == 0`, entering the repeated-division loop with zero would never make progress. Rejecting it first prevents an infinite loop while matching the mathematical definition.

**Remove the complete exponent of each permitted prime**

For each `x` in `[2, 3, 5]`, the loop

```text
while n % x == 0:
    n //= x
```

keeps dividing until `x` is no longer a factor. One division would not be enough: a number such as `8 = 2 * 2 * 2` contains three copies of the factor `2`, and all three must be removed.

If the original positive number has prime factorization

$$
n=2^a3^b5^cR,
$$

where $R$ contains no factor `2`, `3`, or `5`, the three loops reduce it to exactly $R$. The exponents $a$, $b$, and $c$ may be zero, in which case the corresponding inner loop performs no division.

**Why the final comparison is sufficient**

By the fundamental theorem of arithmetic, every positive integer has a unique prime factorization. After every permitted prime factor has been divided away, two cases remain:

- If the residual value is `1`, there is no unpermitted prime factor. The original number consisted only of powers of `2`, `3`, and `5`, so it is ugly.
- If the residual value is greater than `1`, its prime factorization contains at least one prime other than `2`, `3`, or `5`. The original number is not ugly.

The return statement `n == 1` expresses exactly this distinction.

The order `2`, then `3`, then `5` is convenient but not required for correctness. Prime factors commute under multiplication, and dividing by one permitted prime does not create a new copy of another that was previously absent. Any order that exhausts all three would leave the same residual factor.

**Trace for an ugly number**

For `n = 6`:

- The factor-2 loop divides `6` to `3`, then stops because `3` is not divisible by `2`.
- The factor-3 loop divides `3` to `1`.
- The factor-5 loop does nothing.
- The residual is `1`, so the function returns `True`.

For a larger example, `n = 360 = 2^3 * 3^2 * 5`:

- repeated division by `2` changes `360 -> 180 -> 90 -> 45`;
- division by `3` changes `45 -> 15 -> 5`;
- division by `5` changes `5 -> 1`.

Every prime factor was allowed, so the final result is true.

**Trace for a number with a forbidden factor**

For `n = 14 = 2 * 7`, division by `2` leaves `7`. Neither `3` nor `5` divides it, so the residual remains `7`. Since it is not `1`, the function returns `False`, correctly exposing the forbidden factor `7`.

For `n = 42 = 2 * 3 * 7`, removing `2` and `3` also leaves `7`. Allowed factors can coexist with a forbidden one; the algorithm does not accept merely because it finds at least one allowed factor.

**Why one is ugly**

The number `1` has no prime factors. The statement “it has no prime factor other than 2, 3, and 5” is therefore vacuously true. It passes the positivity guard, none of the loops divides it, and the final comparison returns `True`.

## Complexity detail

Let $N$ be the original positive input. Every successful inner-loop iteration divides the current value by at least two. If there are $k$ successful divisions in total, then $2^k\le N$, so $k\le\log_2N$. The three outer iterations add only a constant number of failed divisibility checks. Total time is $O(\log N)$.

The algorithm modifies only the local integer variable `n` and stores the current factor `x`. It allocates no factor list, recursion stack, or other size-dependent structure, so auxiliary space is $O(1)$.

Under the stated fixed-width integer bound, arithmetic operations are treated as constant time. The logarithmic count refers to how many times the numeric value can be reduced by division.

## Alternatives and edge cases

- **Prime-factorize by testing every divisor:** General trial division can discover all prime factors but may take $O(\sqrt n)$ time. Only three allowed primes matter here, so testing anything else is unnecessary.
- **Recursive division:** Recursively divide by an allowed factor until reaching one or failure. It can be correct but uses $O(\log n)$ call-stack space instead of the loop's constant space.
- **Repeated greatest common divisor:** Divide by `gcd(n, 30)` until no progress. Since `30 = 2 * 3 * 5`, this removes allowed factors in batches, but it is less direct than the three simple loops.
- **`n = 1`:** It is positive and has no forbidden prime factor, so it is correctly accepted.
- **`n = 0`:** It must be rejected before division; otherwise repeated divisibility by every factor would never change it.
- **Negative input:** Ugly numbers are defined as positive, so sign handling is not a factorization question and the method rejects immediately.
- **A pure allowed prime power:** Values such as `2^k`, `3^k`, or `5^k` reduce fully to one and are accepted.
- **A permitted product with repeated factors:** The `while` loops, rather than single `if` statements, remove every copy.
- **A forbidden prime alone:** No allowed loop changes it, so the final residual exposes it directly.
- **Mixed allowed and forbidden factors:** Allowed factors are removed, leaving the forbidden portion greater than one and producing `False`.
- **Largest 32-bit values:** The loops never multiply, so there is no overflow risk; division only reduces magnitude.
- **Order of allowed factors:** Changing `[2, 3, 5]` to another ordering leaves the same residual because prime factorization is unique.
