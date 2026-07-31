## General

Each window needs an order statistic, but sorting every window repeats almost all of the previous window's work. The crucial constraint is that every negative value belongs to the fixed set $\{-50,-49,\ldots,-1\}$. Maintain one frequency for each possible negative value while the window slides: add the entering value when it is negative and remove the departing value when it is negative.

To find the beauty, visit possible values from `-50` through `-1` by scanning magnitudes from `50` down to `1`. Subtract each frequency from a counter initially equal to `x`. The first value that makes the counter non-positive is the $x$-th smallest negative and therefore the window's beauty. If the counter remains positive after all negative buckets, the window has fewer than `x` negative elements, so its beauty is `0`.

The frequency table always describes exactly the current length-`k` window because every entering negative is added once and every negative leaving the window is removed once. Its ordered cumulative frequencies reproduce the negative prefix of the window's sorted order, including duplicates. Thus the scan returns the requested negative order statistic when it exists and `0` precisely when it does not.

## Complexity detail

Let $n$ be the length of `nums`. Each element enters and leaves the frequency table at most once, and each completed window scans exactly $50$ negative buckets. Because $50$ is a fixed constraint rather than an input-dependent quantity, the running time is $O(n)$.

The frequency table uses $O(1)$ auxiliary space. The returned array contains $n-k+1$ values, so total space including the required output is $O(n)$.

The benchmark scales both the array and window lengths. A correct implementation that sorts every window completes all tiers but grows quadratically relative to the fixed-domain sliding-window method.

## Alternatives and edge cases

- **Sort every window:** Sorting each length-`k` slice and reading its $x$-th value is direct, but costs $O((n-k+1)k\log k)$ time.
- **Balanced ordered multiset:** A data structure supporting deletions and order statistics can handle a wider value domain in $O(n\log k)$ time, but it is more complex and unnecessary for only $50$ negative values.
- Duplicate negative values must be counted separately because each occurrence occupies its own position in sorted order.
- Nonnegative values never need frequency buckets: if fewer than `x` negatives exist, the $x$-th smallest value cannot be negative and the required answer is `0`.
- When `k = 1`, each negative element is its own beauty and each nonnegative element produces `0`.
- When `k = n`, exactly one beauty is returned.
