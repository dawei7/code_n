## General

Count balanced integers not exceeding a bound, then subtract `count_up_to(low - 1)` from `count_up_to(high)`.

Leading zeros cannot be used because they would shift position parity. Count each exact digit length separately. For shorter lengths, choose a nonzero first digit and use a memoized state `ways(remaining, difference, next_is_odd)` for the unrestricted suffix. `difference` is the odd-position digit sum minus the even-position sum; a completed number is balanced exactly when it is zero.

For numbers having the bound's full length, scan its digits from left to right. At each position, try every smaller legal digit and ask the memoized suffix state how many completions restore the difference to zero. Then follow the bound's actual digit and continue. If the complete bound has difference zero, include it. Starting full-length numbers with digits `1` through `9` enforces the actual representation and preserves the source's leftmost-position rule.

## Complexity detail

Let $D$ be the number of decimal digits in `high`. The difference range has $O(D)$ values for each of $D$ remaining-length values and two parities. With ten digit transitions per state, the time and memoization space are both $O(D^2)$; here $D\leq16$.

## Alternatives and edge cases

- **Enumerate the range:** Test every integer by summing alternating digits. This is straightforward but takes $O((\texttt{high}-\texttt{low}+1)D)$ time.
- **Digit DP with leading zeros:** A generic started/not-started DP is possible, but it must adjust parity using the final significant length; treating padded zeros as positions gives wrong answers.
- **Magnitude pruning:** A suffix state may return zero immediately when `abs(difference) > 9 * remaining`; this preserves the same $O(D^2)$ bound but is not needed for the small digit limit.
- **One-digit numbers:** They are excluded explicitly even though an empty even-position sum might otherwise be compared with the digit.
- **Inclusive endpoints:** Prefix-count subtraction includes both `low` and `high` correctly.
- **Odd digit count:** The two position sets may contain different numbers of digits; only their sums must match.
- **Internal zeros:** Zeros occupy positions and affect which later digits are odd or even, even though they add nothing.
