## General

**Take every zero**

A retained zero never increases the represented number relative to omitting
that same zero while preserving all other selected bits. It may shift earlier
selected bits left, but processing from right to left accounts for that
position through its binary weight. Every zero itself can always be included
and increases the answer by one.

**Consider ones from least to most significant**

Scan `s` from right to left with `place` equal to the current power of two for
the selected suffix.
Maintain the value of the selected ones. Include a one exactly when adding
`place` keeps the value at most `k`; otherwise skip it. Double `place` after
every retained bit, because an earlier selected bit appears to the left of all
retained later positions. A skipped bit occupies no subsequence position.

Among available ones, smaller positional weights are never worse than larger
weights for maximizing count under a value budget. The right-to-left greedy
therefore selects the cheapest feasible ones first. All zeroes are retained,
and each selected one preserves the limit, so the result is valid. Any solution
with more ones would have to replace a rejected weight with an equal or larger
one and would exceed the same budget.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. The scan visits each character once, giving
$O(n)$ time. The running value, place, and count use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Subsequence dynamic programming:** Tracking attainable values or lengths is correct but uses substantially more time and space than the positional greedy.
- **Enumerate subsequences:** Testing all $2^n$ choices is infeasible.
- **Rebuild each candidate number:** Reconstructing and parsing the chosen suffix for every one can take $O(n^2)$ time.
- **Leading zeroes:** Every zero can be counted, including zeros before the first selected one.
- **All zeroes:** The whole string represents zero and is valid.
- **No affordable one:** The answer is still the number of zeroes.
- **Inclusive limit:** A subsequence representing exactly `k` qualifies.
- **Subsequence position:** The power of two advances only when a bit is retained.
- **Large prefix:** Once `place > k`, no earlier one can be selected, though earlier zeroes still count.
