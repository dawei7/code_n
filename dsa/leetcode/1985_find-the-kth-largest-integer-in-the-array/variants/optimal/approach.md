## General
**Compare magnitude before digits**

For canonical non-negative decimal strings without leading zeros, a value with
more digits is always numerically larger. When two strings have equal length,
their ordinary lexicographic order is also their numeric order because the
first differing digit determines both comparisons.

Use the pair `(len(value), value)` as each entry's sorting key. This compares
arbitrarily long values directly as strings and avoids relying on language
support for integers wider than the stated 100 digits.

**Select the descending rank**

Sort the entries in non-decreasing numeric order under that key. The largest
entry is last, the second largest is immediately before it, and the `k`th
largest is therefore at index `-k`. Sorting preserves duplicate copies as
separate list positions, exactly matching the ranking rule.

The returned object is one of the supplied canonical strings, so no formatting
or conversion back to decimal is necessary.

## Complexity detail
Sorting $N$ entries performs $O(N\log N)$ key comparisons. Comparing
equal-length strings may inspect up to $L$ digits, giving the conservative time
bound $O(N\log N \cdot L)$. The ordered list and its keys require $O(N)$
references or key records; the input strings themselves are not duplicated.

## Alternatives and edge cases
- **Convert to arbitrary-precision integers:** Sorting by parsed integer values
  is concise in languages with suitable support, but direct string ordering is
  portable and avoids conversion.
- **Min-heap of size `k`:** Retain the `k` largest numeric strings while
  scanning. This uses $O(k)$ heap space and $O(N\log k \cdot L)$ time.
- **Quickselect:** Partitioning can achieve expected $O(NL)$ time, but requires
  careful custom comparison and has a quadratic worst case without stronger
  pivot guarantees.
- Repeated values must not be collapsed into a set because every occurrence
  consumes a rank.
- `"0"` is the only representation beginning with zero; length comparison
  therefore remains valid without stripping digits.
- A 100-digit value outranks every shorter value regardless of its individual
  digits.
- For `k = 1`, return a maximum; for `k = N`, return a minimum.
