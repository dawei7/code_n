## General
**Determine which alternating targets are possible**

An alternating string has zero and one counts differing by at most one. If the
input counts differ by more, swapping cannot change those counts, so the answer
is `-1`. When zeros are more frequent, the only possible target starts with
zero; when ones are more frequent, it must start with one. Equal counts permit
both `"0101..."` and `"1010..."`.

**Convert mismatches into swaps**

For each feasible starting character, scan `s` against the implied alternating
target and count mismatched positions. Because source and target contain the
same number of each character, the mismatches consist of equally many
misplaced zeros and misplaced ones. One arbitrary swap pairs one of each and
fixes both positions, so the required swaps equal half the mismatch count.

Evaluate the forced target when the counts differ, or take the smaller result
across both targets when the counts are equal. No strategy can use fewer
swaps, since each swap corrects at most two mismatches, and pairing opposite
mismatches shows that this lower bound is always attainable.

## Complexity detail
Counting characters and evaluating at most two target patterns each scan
$O(n)$ characters. The counters and expected-character state use $O(1)$
auxiliary space.

## Alternatives and edge cases
- **Construct and compare target strings:** this remains linear in time but
  allocates $O(n)$ additional string storage.
- **Repeatedly search for a swap partner:** greedily repairing each mismatch is
  correct when partners are chosen carefully, but repeated scans can take
  $O(n^2)$ time.
- A one-character string is already alternating and needs zero swaps.
- Arbitrary-position swaps are essential; counting adjacent swap distance
  solves a different problem.
- When zeros and ones are equally frequent, both starting characters must be
  considered because their swap counts can differ.
