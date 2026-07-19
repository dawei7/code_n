## General
**Claim the smallest remaining value first.** An odd input length is
impossible. Otherwise, count every value and scan a sorted copy of `changed`.
Whenever the current `value` still has unused occurrences, require an unused
occurrence of `2 * value`. Append `value` to the recovered array and consume
one occurrence of both values. If the double is unavailable, no valid recovery
exists.

**Why the greedy pairing cannot steal a needed value.** All values are
nonnegative. For a positive `value`, its double is larger, so ascending order
processes the only possible smaller role before considering that double as an
original candidate. Any valid reconstruction must pair each remaining
smallest occurrence with its double; choosing that forced pair preserves
feasibility for the rest. For zero, the value and its double coincide, and
each successful step consumes two zero occurrences. An odd zero count
therefore fails exactly when the final zero has no partner.

When the scan finishes, every occurrence has been consumed and the recovered
array contains exactly half as many elements as `changed`, proving that its
values and their doubles reproduce the input multiset.

## Complexity detail
Here $N$ is the length of `changed`. Sorting takes $O(N\log N)$ time, while the
frequency-table construction and scan take $O(N)$ time. The sorted sequence,
frequency table, and returned array use $O(N)$ space.

## Alternatives and edge cases
- **Repeated linear searches and removals:** Select a value, search a list for
  its double, and remove both. This can take $O(N^2)$ time because searches and
  shifts are repeated.
- **Counting over the bounded value domain:** A frequency array can process
  values from $0$ through $10^5$ in $O(N+M)$ time and $O(M)$ space, where
  $M=10^5$; it trades sorting for a domain-sized scan.
- An odd input length is rejected before any pairing attempt.
- Zero occurrences must come in pairs because zero is its own double.
- Duplicate originals require equally many unused doubled occurrences; one
  double cannot satisfy multiple copies.
