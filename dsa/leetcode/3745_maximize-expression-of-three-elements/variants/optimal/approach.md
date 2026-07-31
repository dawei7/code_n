## General

The expression increases whenever either added value becomes larger, and it also increases whenever the subtracted value becomes smaller. Therefore, `a` and `b` should be the two largest occurrences in the array, while `c` should be the smallest remaining occurrence.

These choices always respect distinct indices. If the smallest numeric value is also among the two largest numeric values, then all or several values are equal; because the array has at least three positions, the required occurrences can still come from three different indices. Tracking occurrences rather than a set also preserves duplicate candidates.

A single scan maintains the smallest value and the largest two values seen so far. The final combination of those three extrema is at least as good as any other distinctly indexed assignment, so `largest + second_largest - smallest` is the optimum.

## Complexity detail

The scan examines all $n$ values once, giving $O(n)$ time. It stores only three extrema, so the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Sort the array:** The answer is immediately available from the first and last two sorted elements, but sorting costs $O(n\log n)$ time.
- **Try all triples:** Direct enumeration is correct but takes $O(n^3)$ time.
- **Recompute two maxima for every `c`:** This respects distinct indices but repeats scans and takes $O(n^2)$ time.
- **Duplicate values:** Equal numeric extrema can be selected from different positions; deduplicating the array would be incorrect.
- **All negative values:** Choosing the least negative two added values and subtracting the most negative value still follows the same rule.
- **Exactly three values:** All positions must be used, with the smallest assigned to `c`.
