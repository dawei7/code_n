## General

**Compare the versions as integer-revision sequences**

The candidate splits both strings at dots and walks corresponding components with the conventional position `i`.
When one list ends first, it supplies `"0"` for each missing revision, implementing the contract's trailing-zero
padding.

Normalize each supplied revision by removing leading zeroes and representing an all-zero component as `"0"`. Two
normalized strings can be compared without integer conversion: the one with more digits is numerically larger, and
equal-length digit strings have the same order lexicographically. This remains safe independently of integer width.

The first unequal revision determines the version order, so return immediately after a digit-count or lexicographic
difference. If every aligned component is equal after zero padding, return zero.

Normalization preserves every revision's integer value. Comparing normalized revisions in left-to-right priority
order is therefore exactly lexicographic comparison of the integer sequences described by the contract, including
implicit trailing zeroes.

## Complexity detail

Let $m$ and $n$ be the two input string lengths. Splitting, stripping leading zeroes, and comparing components visit
$O(m + n)$ characters in total. The materialized component lists and normalized strings use $O(m + n)$ auxiliary
space.

## Alternatives and edge cases

- **Convert each revision to an integer:** is concise and safe under this source contract, but the normalized-string
  comparison also works without relying on integer width.
- **Compare complete version strings:** incorrectly orders values such as `"1.2"` and `"1.10"`.
- **Compare raw component strings:** mishandles leading zeroes and unequal digit counts.
- Leading zeroes do not affect a revision's numeric value.
- Missing trailing revisions are zero, so `"1"`, `"1.0"`, and `"1.0.0"` compare equal.
- The first unequal revision fixes the result regardless of every later component.
