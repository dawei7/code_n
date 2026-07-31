## General

**Only primes at most the target matter.** A selected prime is positive, so any prime greater than `n` can never appear in a valid sum. Sieve the integers through `n`, scan the primes in increasing order, and stop after collecting `m` of them. If fewer than `m` primes lie at or below the target, all remaining members of the first-`m` prime prefix are too large and can be ignored safely.

Before filling the table, test whether `n` itself is usable or whether two usable primes sum to `n`. These exact checks return the globally minimal answers `1` and `2` immediately. Besides avoiding unnecessary work on common inputs, they keep large easy targets within the app's execution budget without changing the worst-case bound.

**Use the target sum as the dynamic-programming state.** Let `dp[total]` be the minimum number of usable primes needed to form `total`. Initialize `dp[0] = 0`; every other sum starts unreachable. For each total from $1$ through `n`, try every usable prime `p` with `p <= total`. If `total - p` is formable, appending one copy of `p` gives the candidate `dp[total - p] + 1`. Repetition is naturally allowed because smaller totals have already incorporated every prime any number of times.

Every multiset forming `total` has some final selected prime `p`; removing it leaves a representation of `total - p`. The transition examines that choice and combines it with the minimum representation of the remainder. Conversely, every transition appends an allowed prime to a valid smaller sum. Induction over increasing totals therefore makes each finite `dp[total]` exact. Return `dp[n]`, or `-1` if it remains unreachable.

## Complexity detail

Let $P=\min(m,\pi(n))$, where $\pi(n)$ is the number of primes at most `n`. The sieve takes $O(n\log\log n)$ time. The dynamic program considers at most $P$ primes for each of `n` totals, taking $O(nP)$ time; this is $O(nm)$ in the stated parameters. The sieve, prime list, and DP array use $O(n)$ space.

## Alternatives and edge cases

- **Greedy selection of the largest prime:** Prime denominations are not a canonical coin system. For `n = 22, m = 6`, greedy starts with `13` and needs three terms, while `11 + 11` uses two.
- **Breadth-first search over sums:** Treating sums as nodes also finds the minimum number of terms in $O(nP)$ time and $O(n)$ space, but the DP expresses the recurrence more directly.
- **Two-dimensional count-by-sum DP:** Tracking every possible term count is correct but uses $O(n^2)$ space and can require $O(n^2P)$ time despite only the minimum count being needed.
- **Target below the first prime:** `n = 1` is unreachable for every valid `m`.
- **Only the prime 2 is available:** Even targets require exactly `n / 2` terms; odd targets are impossible.
- **Target itself is available:** If `n` is prime and belongs to the first `m` primes, the answer is `1`.
- **Large `m`:** Generating primes beyond `n` is unnecessary because none can contribute to the sum.
