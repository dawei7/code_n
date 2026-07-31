## General

Let $L$ be the largest trim length requested. Ordering by the last digit is
the first pass of a least-significant-digit radix sort. If indices are already
ordered by the last $t-1$ digits, a stable counting sort by the digit $t$
places from the right orders them by the last $t$ digits.

**Answer queries during the radix passes**

Group queries by their `trim` value while retaining each query's original
position. Begin with indices `0` through `n - 1`; this order supplies the
required lower-index tie break. For each trim length from 1 through $L$, place
the indices into ten digit buckets in their current order and concatenate the
buckets. Answer every query registered for this trim by reading position
`k - 1` from the new order.

Stability preserves the established order of less significant digits inside
each new digit bucket. Inductively, after pass $t$, indices are ordered by
their complete length-$t$ suffix. Indices whose suffixes are identical have
never been reordered relative to the initial ascending-index order, so ties
also satisfy the contract. Each query therefore reads exactly its requested
rank.

## Complexity detail

For $n$ strings, $q$ queries, and maximum requested trim $L$, each radix pass
visits all indices and ten fixed buckets. The total time is $O(nL+q)`.
The current index order, buckets, grouped queries, and answer array use
$O(n+q)$ auxiliary space.

## Alternatives and edge cases

- **Sort independently per query:** Sorting `(trimmed suffix, index)` pairs is
  simple, but costs $O(qn\log n)$ time and repeats work for equal trim lengths.
- **Cache one comparison sort per trim:** This avoids duplicate-query work but
  still pays $O(n\log n)$ for each distinct requested trim.
- **Leading zeros:** Compare equal-length suffix strings directly; converting
  them to integers is unnecessary.
- **Equal suffixes:** Stable radix passes preserve ascending original indices,
  which implements the specified tie break.
- **Unused long prefixes:** Stop after the largest requested trim rather than
  processing digits that no query observes.
