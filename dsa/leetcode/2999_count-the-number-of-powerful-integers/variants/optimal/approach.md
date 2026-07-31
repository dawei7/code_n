## General

**Separate the fixed suffix.** Let `suffix = int(s)` and let $P=10^{\lvert
\texttt{s}\rvert}$. Every positive integer ending with `s` has one unique
representation `prefix * P + suffix`, including `prefix = 0` when the number
is exactly the suffix. Since all suffix digits already satisfy `limit`, only
the prefix digits remain to be checked.

**Turn an integer bound into a prefix bound.** For an upper bound `bound`, no
candidate exists when it is below `suffix`. Otherwise the largest possible
prefix is `(bound - suffix) // P`. The task is now to count nonnegative prefix
integers no larger than this value whose digits are all at most `limit`.

Scan the prefix bound from its most significant digit. At each position,
count choices smaller than the bound's current digit; every remaining position
then has `limit + 1` choices. If the bound digit itself exceeds `limit`, the
equal-prefix path cannot continue. Otherwise keep matching it. Include the
bound itself after a complete valid scan. Leading zeroes merely pad the unique
nonnegative prefix and do not create duplicate integers.

Finally subtract the count through `start - 1` from the count through
`finish`, which enforces both inclusive range boundaries.

## Complexity detail

Each upper-bound count scans at most $D$ decimal digits and stores only scalar
state. The total complexity is $O(D)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate digit-limited prefixes:** This is correct but may visit $(\texttt{limit}+1)^D$ candidates.
- **Digit DP with tight state:** A general memoized digit DP works, but the fixed suffix makes the direct positional count simpler.
- **Suffix alone:** `prefix = 0` must be counted when the suffix value lies inside the range.
- **Lower boundary:** Counting through `start - 1` prevents a valid suffix below `start` from leaking into the answer.
- **Bound shorter than the suffix:** Such a bound contributes zero candidates.
- **Zeroes inside the suffix:** They are ordinary digits; only a leading zero is excluded by the contract.
