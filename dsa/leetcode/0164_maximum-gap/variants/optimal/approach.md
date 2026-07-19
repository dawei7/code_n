## General
Sorting would expose every adjacent pair, but comparison sorting costs $O(n \log n)$. The linear-time route comes from realizing that the exact internal order of nearby values is irrelevant: only sufficiently separated groups can contain the maximum gap.

Let `lo` and `hi` be the minimum and maximum of $n \ge 2$ values. In sorted order there are $n - 1$ adjacent gaps whose sum is `hi - lo`, so at least one gap is no smaller than

`gap = ceil((hi - lo) / (n - 1))`.

This pigeonhole lower bound becomes the bucket width. Partition `[lo, hi]` into consecutive numeric buckets of width `gap`. For each nonempty bucket, store only its minimum and maximum. Two values assigned to the same bucket differ by less than `gap`, while the true maximum adjacent gap is at least `gap`. Therefore the answer cannot be a pair hidden strictly inside one bucket; it must cross from one nonempty bucket to the next.

Scan the buckets in numeric order. For each nonempty bucket, compare its minimum with the maximum of the previous nonempty bucket. Empty buckets need no special calculation—their absence is exactly what can make that cross-bucket difference large. Then replace `previous_max` with the current bucket's maximum.

For `[3, 6, 9, 1]`, `lo = 1`, `hi = 9`, and the width is $\left\lceil 8 / 3 \right\rceil = 3$. The occupied groups contain extrema `(1, 3)`, `(6, 6)`, and `(9, 9)`. Cross-bucket comparisons give $6 - 3 = 3$ and $9 - 6 = 3$, which is the maximum sorted adjacent gap without constructing the sorted array.

Care is needed in the degenerate case `lo = hi`: every value is equal, division would produce a zero width, and the answer is simply zero. Integer ceiling can be computed without floating point as `(hi - lo + n - 2) // (n - 1)`.

The average-gap argument guarantees that the maximum sorted adjacent gap is at least the chosen bucket width. Every within-bucket difference is strictly smaller than that width, so no within-bucket pair can be the maximum. Buckets are ordered by value; consequently, for any two consecutive nonempty buckets, the previous bucket's maximum and current bucket's minimum are consecutive in the globally sorted sequence. The scan examines all such cross-bucket consecutive pairs, which include the maximum-gap pair, and returns their largest difference.

## Complexity detail
Computing `lo` and `hi`, assigning all values, and scanning at most `n` buckets are each linear passes, for $O(n)$ total time. The bucket minima and maxima require $O(n)$ auxiliary space.

## Alternatives and edge cases
- Ordinary comparison sorting is the simplest baseline but requires $O(n \log n)$ time.
- Radix sort can also be linear in the number of values for a fixed integer width, though it fully orders the data and needs careful digit handling.
- A presence array indexed across `[lo, hi]` uses space proportional to the value range rather than to `n`.
- Fewer than two values, or all-equal values, return zero immediately.
- Duplicate values safely update the same bucket extrema and contribute no positive gap.
- Fixed-width implementations should use a sufficiently wide integer type for `hi - lo` and the ceiling numerator.
