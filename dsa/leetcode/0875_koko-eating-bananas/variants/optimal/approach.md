## General

The unknown is an integer eating speed $k$. For any proposed speed, the exact number of hours needed can be computed. That creates a decision question:

> Can Koko finish all piles within `h` hours at speed `k`?

This question is monotonic. If a speed is fast enough, every larger speed is also fast enough. If a speed is too slow, every smaller speed is also too slow. Therefore the possible speeds form a sequence of failures followed by successes, and binary search can find the first success.

**Compute the hours for one pile.** A pile containing `x` bananas requires

$$
\left\lceil\frac{x}{k}\right\rceil
$$

hours. Koko can consume at most `k` bananas from that one pile in an hour, and she does not use leftover time from a smaller final portion to start another pile. This is why ordinary total-bananas division would be wrong: every pile rounds its own time upward separately.

The exact solution evaluates the ceiling with integer arithmetic:

```text
(x + k - 1) // k
```

For positive integers, adding $k-1$ before floor division produces the ceiling. If `x` is exactly divisible by `k`, the quotient is unchanged; otherwise the addition pushes the partial group into one extra hour.

The helper `check(k)` sums that value over all piles and returns whether the total is at most `h`. “At most” matters: finishing exactly when the guards return is valid.

**Choose a complete search interval.** The slowest possible positive speed is 1. The fastest speed ever needed is `max(piles)`. At that speed, every pile takes exactly one hour, and the constraint `h >= len(piles)` guarantees completion. Any faster speed cannot reduce a pile below one hour, so it cannot improve feasibility in a way needed for the minimum.

The exact code represents all candidates with `range(1, max(piles) + 1)`. These are the speeds $1,2,\ldots,M$, where $M$ is the largest pile.

**How `bisect_left` is used on a virtual boolean sequence.** Python's `bisect_left` can accept a `key` function. Here it conceptually views the speed range through `check`:

```text
[check(1), check(2), ..., check(M)]
```

Because of monotonicity, this list has zero or more `False` entries followed by one or more `True` entries. The call searches for `True` and returns the zero-based index of the first true entry.

The range starts at speed 1, so index zero corresponds to speed 1, index one to speed 2, and in general index $p$ corresponds to speed $p+1$. That is why the solution returns `1 + bisect_left(...)`. The added one converts a range index back into the actual eating speed.

**Why feasibility is monotonic.** For a fixed positive pile size $x$, increasing $k$ can never increase $\lceil x/k\rceil$; it either reduces the number of hourly chunks or leaves it unchanged. Summing these nonincreasing terms across piles gives a nonincreasing total hour count. Once the total falls to `h` or less, it stays within `h` for every greater speed.

**Why the returned speed is minimal.** Binary search returns the first candidate for which `check` is true. That candidate is feasible. Every smaller candidate occurs before it in the monotonic sequence and is false, so no smaller positive integer speed can finish in time. These two facts establish both validity and minimality.

For `piles = [3,6,7,11]` and `h = 8`, speed 3 requires $1+2+3+4=10$ hours and fails. Speed 4 requires $1+2+2+3=8$ hours and succeeds. The transition from false to true therefore occurs at speed 4, which binary search returns.

The solution never builds the conceptual boolean list. `range` is lazy, and `bisect_left` calls `check` only at logarithmically many candidate speeds. That is the performance advantage over testing every speed from 1 upward.

## Complexity detail

Let $n$ be the number of piles and $M=\max(\texttt{piles})$. A feasibility check reads all $n$ piles and costs $O(n)$. Binary search over $M$ candidate speeds performs $O(\log M)$ checks.

- **Time complexity:** $O(n\log M)$.
- **Space complexity:** $O(1)$ auxiliary space. The `range` is a compact range object rather than a materialized list, and the generator expression is consumed while summing.

The input array is read but not modified. Arithmetic uses Python integers, so the sum remains exact even when `h` and pile sizes are large.

## Alternatives and edge cases

- **Linear speed search:** Test 1, 2, 3, and so on until one succeeds. It finds the right boundary but can require $O(nM)$ time when the largest pile is near $10^9$.
- **Use total bananas divided by hours:** This ignores that Koko chooses only one pile per hour and cannot transfer unused capacity from a finished pile to another pile in the same hour.
- **Binary search with explicit pointers:** Maintaining `low`, `high`, and `mid` implements the same lower-bound search and may be more portable than Python's keyed `bisect_left`.
- **Floating-point ceiling:** Calling a floating-point ceiling operation is unnecessary and risks precision issues for wider bounds. The integer formula is exact.
- **One pile:** The condition becomes $\lceil x/k\rceil\le h$, and the same binary search finds the smallest speed.
- **`h` equals the number of piles:** Every pile must finish in one hour, so the answer is the largest pile size.
- **Very large `h`:** Speed 1 may already be feasible. The lower-bound index is then zero, and adding one correctly returns 1.
- **Exact division:** When `x % k == 0`, the ceiling formula produces exactly `x // k` without adding a false extra hour.
- **Partial final hour:** A remainder requires one full counted hour even if only a few bananas remain.
- **Duplicate pile sizes:** Each pile contributes its own rounded hour count. Duplicates need no special handling.
- **Guaranteed successful upper bound:** At speed `max(piles)` every pile takes one hour, and `h >= n` guarantees that `bisect_left` sees at least one true candidate.
- **Positive speed domain:** The range begins at 1, so division by zero is impossible and speed zero is never considered.
