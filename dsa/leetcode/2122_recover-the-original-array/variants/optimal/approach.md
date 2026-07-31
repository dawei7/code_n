## General

**The smallest observed value must be a lower copy**

Sort `nums`. Its first value cannot be a higher copy: the corresponding lower
copy would be smaller and would also appear. Therefore, for the correct $k$,
the partner of this minimum is some later sorted value, and their difference
is exactly $2k$.

Enumerate every later value as that possible partner. Reject a nonpositive or
odd difference because $k$ must be a positive integer. For each remaining
difference $d$, create a frequency map of all observed values.

**Greedily pair the smallest unused value**

Scan the sorted values. Whenever a value $x$ still has positive frequency, it
must be a lower copy for this candidate gap: if it were a higher copy, its
smaller unused partner $x-d$ would have appeared earlier. Require one copy of
`x + d`, remove both frequencies, and append their midpoint `x + d // 2`.
If the partner is absent, reject this gap.

When $n$ pairs are formed, their lower and higher copies consume the entire
input multiset, so the recovered midpoints are valid with $k=d/2$. For the
true gap, the smallest-unused argument ensures every greedy pair is forced and
available, so that candidate succeeds. Returning the first successful
candidate is valid even when others also work.

## Complexity detail

Sorting $2n$ values takes $O(n\log n)$ time. There can be $O(n)$ candidate
gaps, and each builds and scans an $O(n)$ frequency multiset, for $O(n^2)$
total time. The sorted values, counter, and recovered result use $O(n)$ space.

## Alternatives and edge cases

- **Backtracking all pairings:** Choose whether each unused value is lower or
  higher and try partners recursively. This explores exponentially many
  assignments that sorted greedy pairing makes unnecessary.
- **Repeated linear partner search:** Search and delete a partner from a list
  for every pair and every candidate. This can add another linear factor,
  taking $O(n^3)$ time.
- A zero difference is invalid because $k$ must be positive.
- An odd difference cannot equal $2k$ for integer $k$.
- Duplicate counts must be removed one copy at a time.
- A lower copy from one original may equal a higher copy from another.
- The recovered order is unrestricted, and any valid positive array may be
  returned when the answer is non-unique.
