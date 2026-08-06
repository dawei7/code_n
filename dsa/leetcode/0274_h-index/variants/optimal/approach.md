## General
**Counts above `n` are equivalent for the h-index**

An h-index cannot exceed the number of papers `n`, so place every citation count at least `n` into bucket `n`; otherwise use its exact count as the bucket index.

**Descending accumulation tests candidates from best to worst**

Scan buckets downward while maintaining how many papers have at least the current citation threshold. The first threshold whose cumulative count reaches that threshold is the largest valid h-index.

At bucket index `h`, the cumulative total equals exactly the number of papers with at least `h` citations.

**The first feasible threshold is maximal**

At threshold `h`, the cumulative bucket total counts precisely the papers with at least `h` citations. Thus `total >= h` is exactly the h-index feasibility condition. Since thresholds are tested from `n` downward, no larger value is feasible when the first success is reached, making it the maximum h-index.

## Complexity detail

Populating the $n + 1$ buckets scans all papers once, and the descending cumulative scan examines every bucket at most
once. The total time is $O(n)$, and the bucket array uses $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Sort citations:** is simple but takes $O(n \log n)$.
- **Count qualifying papers separately for every candidate h:** takes $O(n^2)$.
- **Empty input:** the app-local implementation returns zero defensively, although the native contract requires at least one paper.
- **All-zero input:** the descending scan reaches bucket zero and returns zero.
- **Citation count above n:** capping it at `n` preserves every possible h-index threshold while keeping the bucket array linear.
