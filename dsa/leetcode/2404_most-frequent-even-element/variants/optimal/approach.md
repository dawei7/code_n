## General

**Count only eligible values.** Scan `nums` and add each value divisible by 2
to a frequency map. Odd elements can be discarded immediately because neither
their identities nor their frequencies participate in the answer.

**Encode both selection priorities.** If the map is empty, no even element
exists and the answer is `-1`. Otherwise choose the key whose ordering tuple is
`(-frequency, value)`. Minimizing this tuple prefers a larger frequency because
of the negation, then a smaller value when frequencies tie.

The frequency map contains exactly one entry for every distinct even value and
its exact occurrence count. The tuple comparison therefore selects an element
with globally maximal frequency and applies precisely the required numeric
tie break. The empty-map branch covers the only case with no valid candidate.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$ and let $u$ be the number of distinct even
values. Counting takes expected $O(n)$ time with hash-table operations, and
selecting the best of $u\le n$ entries takes $O(u)$, so total expected time is
$O(n)$. The map uses $O(u)$ auxiliary space.

## Alternatives and edge cases

- **Sort the even elements:** After filtering, sorting groups equal values and
  makes tie handling straightforward, but costs $O(n\log n)$ time.
- **Repeated full-array counts:** Counting each distinct even value by scanning
  all of `nums` is correct but can take $O(nu)$, which becomes $O(n^2)$.
- **Bounded frequency array:** The value limit permits a fixed array through
  $10^5$; this avoids hashing but scans or allocates the entire domain.
- **No even values:** Return `-1`, not the smallest odd value.
- **Zero:** `0 % 2 == 0`, so zero must be counted normally and wins any tied
  frequency against larger even values.
- **One even occurrence:** It wins when it is the only even candidate,
  regardless of how many odd values occur.
- **Frequency tie:** Numeric value, not first appearance order, determines the
  winner.
