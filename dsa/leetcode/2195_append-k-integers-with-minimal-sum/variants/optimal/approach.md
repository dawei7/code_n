## General

**The optimum is the first missing positives**

If a chosen integer is larger than an available positive integer, replacing
it with that smaller value preserves validity and lowers the sum. Therefore,
the unique optimum consists of the `k` smallest positive integers absent from
`nums`.

Deduplicate and sort `nums` so its values become ordered exclusion points.
Maintain `next_missing`, the smallest positive value not yet processed.
Before each excluded value, the whole interval from `next_missing` through
`value - 1` is available.

**Consume a gap in constant time**

Take as many values from the start of each available interval as are still
needed. If these are the `take` consecutive integers from $a$ through $b$,
add their arithmetic-series sum

$$
\frac{(a+b)\cdot\texttt{take}}{2}.
$$

Stop immediately when `k` reaches zero. If exclusions finish first, consume
the remaining consecutive values beginning at `next_missing` with the same
formula.

Every processed gap contributes its smallest available values before any
larger gap is considered. The exchange argument shows that skipping one of
these values for a later value cannot be optimal. Deduplication prevents a
repeated input value from incorrectly creating or consuming another gap, so
the accumulated arithmetic sums equal the unique minimum.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Deduplication and sorting take
$O(n\log n)$ time, and the sorted exclusions are scanned once. Arithmetic
gap consumption is independent of the magnitude of `k`. The distinct-value
set and sorted sequence use $O(n)$ space.

## Alternatives and edge cases

- **Enumerate positive candidates:** Test `1, 2, 3, ...` against a set until
  `k` missing values have been selected. This takes $O(n+k)$ expected time and
  is too slow when `k` is large.
- **Boolean presence array:** Mark every value through the largest relevant
  integer. The value range reaches $10^9$, so this can require prohibitive
  space.
- Duplicate entries in `nums` exclude their value only once.
- If `1` is absent, it is always the first appended integer.
- When an exclusion lies beyond all `k` needed values, processing can stop
  before that exclusion.
- The answer can exceed 32-bit integer range.
- Large gaps and a large `k` must be summed arithmetically, not materialized.
