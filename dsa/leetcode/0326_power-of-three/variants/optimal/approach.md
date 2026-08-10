## General

**A power of three can be peeled apart one factor at a time.**

For an integer input, the values that qualify are

$$
3^0=1,
\quad 3^1=3,
\quad 3^2=9,
\quad 3^3=27,
\quad \ldots
$$

Every positive power above `1` is divisible by `3`, and dividing $3^x$ by `3` produces the smaller power $3^{x-1}$. Repeating exact division must eventually reach $3^0=1$.

Conversely, if at any stage a positive value greater than `2` is not divisible by `3`, it contains some factor other than the required threes. It cannot be a pure power of three. This gives the exact iterative test used by the source: while the current value is above `2`, require divisibility by `3`, divide, and continue. After the loop, accept only `1`.

**Why the loop condition is `n > 2`.**

The values at or below `2` can be classified immediately:

- `1` is $3^0$, so it is a power of three;
- `2` is not a power of three;
- `0` is not a power of three;
- negative integers are not powers of positive base `3`.

The loop therefore only needs to process values at least `3`. This condition also safely excludes zero. A loop written only as “while divisible by three” needs a separate positive check because zero remains zero after division and is divisible by three forever. The exact source avoids that trap because `0 > 2` is false.

Once the loop ends, `return n == 1` distinguishes the one valid terminal value from `2`, zero, and negative values without additional branches.

Although the definition says there exists an integer exponent $x$, a negative exponent gives a fraction such as $3^{-1}=1/3$, not a signed integer input. Thus the only relevant exponents here are nonnegative, and `1` must be included.

**Understand the remainder test.**

Inside the loop, the source evaluates `if n % 3`. In Python, the remainder `0` is false, while a nonzero remainder is true. Therefore:

- if `n % 3 == 0`, the `if` body is skipped and exact integer division is allowed;
- if `n % 3 != 0`, the method immediately returns `False`.

The following `n //= 3` is reached only after divisibility has been confirmed. As a result, floor division loses no fractional information: the mathematical quotient is already an integer.

For `n = 27`, the successive current values are

$$
27 \longrightarrow 9 \longrightarrow 3 \longrightarrow 1.
$$

Every remainder is zero. The loop stops at `1`, and the method returns `True`.

For `n = 45`, division first gives `15`, then gives `5`. The value `5` is still greater than `2`, but `5 % 3` is nonzero, so the method returns `False`. This correctly detects the extra factor `5` in $45=3^2\cdot5$.

For `n = 6`, one exact division produces `2`. The loop then stops, but the final comparison rejects `2`. This illustrates why reaching a small value is not by itself enough; the chain must end at exactly `1`.

**A useful loop invariant.**

Suppose the loop has completed $t$ successful divisions. The current value equals the original input divided by $3^t$, and every removed factor was exact. Equivalently,

$$
\text{original } n = \text{current } n \cdot 3^t.
$$

This invariant holds before the first iteration with $t=0$. A successful remainder check and division remove one factor of three, preserving the equation with $t+1$. If a remainder is nonzero, the current value cannot supply the next required factor, so the original cannot consist solely of threes.

If the process terminates at `1`, the invariant gives

$$
\text{original } n = 3^t,
$$

which proves every accepted input really is a power of three. If the original is $3^x$, every one of its first $x$ remainder checks succeeds and division eventually reaches `1`, proving every true power is accepted. Together, these directions establish correctness.

**Why the input shrinks quickly.**

Each successful iteration divides the current positive value by three. After $t$ iterations, it is $n/3^t$. The loop can continue only while this is at least `3`, so the number of iterations is proportional to the exponent in the largest power of three not exceeding the input. Under the signed 32-bit constraint, even the largest valid power requires only nineteen divisions, but the source still genuinely uses a loop rather than a single constant-work divisibility test.

## Complexity detail

For a positive input $n$, each successful iteration divides it by `3`. There are at most $\lfloor\log_3 n\rfloor$ such iterations, with possibly one final failed divisibility check. The worst-case time complexity of the exact implementation is therefore $O(\log_3 n)$, commonly written $O(\log n)$. Nonpositive values and the small values `1` and `2` return in $O(1)$ time.

Only the input variable is updated. There is no collection and no recursion, so auxiliary space is $O(1)$.

The variant manifest currently summarizes a different technique: testing divisibility into the largest signed-32-bit power of three, which would be $O(1)$. The checked-in optimal source instead performs repeated division in a `while` loop. Its actual time bound is $O(\log n)$, while its space bound remains $O(1)$.

## Alternatives and edge cases

- **Largest-power divisibility:** The greatest power of three within signed 32-bit range is $3^{19}=1162261467$. Because its only positive divisors are powers of three, `n > 0 and 1162261467 % n == 0` gives a constant-work test under this exact numeric bound. This matches the manifest summary but is not the source implementation.

- **Repeated multiplication:** Start at `1` and multiply by `3` until reaching or passing `n`. This also takes $O(\log n)$ time and $O(1)$ space, but fixed-width languages must guard against overflow on the final multiplication.

- **Logarithms:** Compute $\log_3 n$ and test whether it is an integer. Floating-point rounding near integral results can cause false classifications, so exact divisibility is safer.

- **Base-three string:** A positive power of three has the base-three representation `1` followed only by zeros. Conversion and string checking work, but require $O(\log n)$ time and string space instead of the source's constant space.

- **`n = 1`:** The loop does not execute, and the final equality returns `True` because $1=3^0$.

- **`n = 0`:** The loop does not execute, preventing an infinite sequence of zero divisions, and the final equality returns `False`.

- **Negative input:** A positive base raised to an integer exponent is always positive. Every negative input skips the loop and is rejected.

- **Small nonpower `2`:** It skips the loop but fails the final `n == 1` check. This is the main reason the loop's lower boundary can be `n > 2` rather than `n > 1`.

- **A power times another factor:** Exact divisions may remove several threes first, but the remaining foreign factor eventually causes a nonzero remainder or a terminal value of `2`, so the input is rejected.
