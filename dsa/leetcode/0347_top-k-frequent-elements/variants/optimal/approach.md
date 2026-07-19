## General
**Use frequencies as bucket indices**

Sorting values by frequency would organize more information than the answer needs and costs $O(u \log u)$ for `u` distinct values. Frequencies have a small integer range that makes bucket grouping linear: no value can occur fewer than once or more than `n` times.

First count every value with a hash map. Create $n + 1$ buckets, where bucket index `f` stores all values whose frequency is `f`. Place each distinct value into the bucket selected by its count, then scan bucket indices from `n` downward. Append values encountered until exactly `k` have been collected.

**Why the first k emitted values are correct**

After counting, the map contains the exact frequency of every distinct value. Bucket placement preserves that information because a value goes into precisely the bucket equal to its count. During the descending scan, every value emitted before another has frequency at least as large. Therefore the first `k` emitted values form the required top-frequency set; the uniqueness guarantee ensures no ambiguous boundary can require choosing among equally frequent values.

**Trace the occupied buckets**

For `[1, 1, 1, 2, 2, 3]`, the buckets at indices `3`, `2`, and `1` contain `1`, `2`, and `3`. Scanning downward returns `1` and `2` and stops.

## Complexity detail
Counting visits `n` input positions. Placing `u` distinct values and scanning the $n + 1$ bucket array take $O(u + n)$, so total time is $O(n)$. The frequency map, buckets, and result together use $O(n)$ space in the worst case.

## Alternatives and edge cases
- **Sort distinct values by frequency:** takes $O(n + u \log u)$ time for `u` distinct values.
- **Size-k min-heap:** takes $O(n + u \log k)$ and may use less selection storage when `k` is small, but misses the required worst-case linear bound.
- **Quickselect:** offers expected $O(n)$ time but needs delicate partitioning and can degrade to quadratic time without stronger pivot guarantees.
- Negative values and zero are ordinary hash keys.
- When `k` equals the number of distinct values, every distinct value must be returned.
- Output order is irrelevant, but the result cannot contain duplicates because the buckets store map keys rather than input occurrences.
