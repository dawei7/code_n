## General
**Exact matches must be removed before counting values**

Scan aligned positions once. Equal digits are bulls and must not also participate in cow matching. For every mismatch, record the unmatched secret digit and unmatched guess digit in separate ten-entry frequency arrays.

**Cow matching is the overlap of the remaining digit multisets**

After bulls are excluded, let $s_d$ and $g_d$ be the unmatched frequencies of digit $d$ in the secret and guess. The number of cows is
$\sum_{d=0}^{9} \min(s_d,g_d)$.
This overlap pairs every available equal value without reusing any occurrence.

For `secret = "1123"` and `guess = "0111"`, the third position is the only bull. The unmatched secret digits are `1, 1, 3`; the unmatched guess digits are `0, 1, 1`. Their frequency overlap contains one additional `1`, producing `1A1B`.

**Frequency overlap is both attainable and maximal**

For each digit, occurrences cannot pair with any other value, so no solution can use more than the smaller of its two unmatched counts. Pairing that many occurrences is always possible because position no longer matters after exact matches were removed. The per-digit minima therefore construct the maximum legal cow count, while the first pass already counted every bull exactly once.

## Complexity detail
The aligned scan visits each of the `n` positions once, and the final overlap examines ten digit buckets. This gives $O(n)$ time. Two fixed ten-entry arrays use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Search the secret separately for every unmatched guess digit:** can take $O(n^2)$ time and needs careful occurrence marking.
- **Count all matching values before bulls:** double-counts exact matches unless the bull count is subtracted afterward.
- Repeated digits are limited by frequency overlap. All bulls produce `nA0B`; disjoint digit sets produce `0A0B`.
