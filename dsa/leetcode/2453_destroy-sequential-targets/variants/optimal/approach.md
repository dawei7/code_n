## General

Two values differ by an integer multiple of `space` exactly when they have the same remainder modulo `space`. A seed can only destroy targets from its own remainder class.

Within one remainder class, choose its smallest value as the seed. Every other value in that class is at least as large and differs from the seed by a non-negative multiple of `space`, so the seed reaches the entire class. Any larger seed from the same class misses at least the targets below it and can never do better.

Count the number of array entries in every remainder class, including duplicates. The destruction score of the smallest member of a class is exactly that class's frequency. Select a value whose class has maximum frequency, breaking ties by the value itself. A tuple key `(-frequency, value)` expresses both rules directly.

Every possible seed belongs to one counted class and cannot destroy outside it, so no seed can exceed its class frequency. The smallest member achieves that upper bound. Comparing these achievable class scores and applying the required tie-break therefore returns the optimal seed.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Counting remainders and selecting the best value each take $O(n)$ time.

There are at most $\min(n,\texttt{space})$ represented remainder classes, so the counter uses $O(\min(n,\texttt{space}))$ auxiliary space.

## Alternatives and edge cases

- **Sort by remainder and value:** Sorting can identify class sizes and minima but costs $O(n\log n)$ time.
- **Simulate every seed:** Testing each array value against every target is correct but takes $O(n^2)$ time.
- **Store count and minimum together:** A map from each remainder to `(count, minimum)` supports the same $O(n)$ bound and avoids a second selection over `nums`.
- **Duplicate targets:** Every occurrence contributes to its remainder frequency and destruction count.
- **`space == 1`:** All targets share one class, and the minimum array value destroys all of them.
- **No shared remainder:** Every class has frequency one, so the globally smallest value wins.
- **Non-negative multiplier:** A seed cannot destroy a smaller target; choosing the class minimum is what makes the full remainder count attainable.
- **Large values:** Only remainders, counts, and comparisons are needed; no sequence is generated up to $10^9$.
