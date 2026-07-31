## General

Because `nums` is non-decreasing, its values form at most three contiguous regions: negatives, then zeros, then positives. The insertion position of `0` before any existing zeros is exactly the number of negative values. The insertion position after all existing zeros is the first positive index, so subtracting it from $n$ gives the positive count.

Use a lower-bound binary search for the first value greater than or equal to zero and an upper-bound binary search for the first value greater than zero. These definitions also handle a missing region naturally: an all-positive array has lower bound zero, an all-negative array has upper bound $n$, and an all-zero array produces zero for both counts. Returning the larger boundary-derived count gives the required answer.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. Each boundary search halves its remaining interval and takes $O(\log n)$ time; performing two searches preserves that bound. Only indices and counts are stored, so the auxiliary-space bound is $O(1)$.

## Alternatives and edge cases

- **Linear counting pass:** Testing every element is simple and uses $O(1)$ space, but costs $O(n)$ time and does not exploit the sorted-order guarantee.
- **One custom search plus scanning zeros:** Finding one boundary and then walking across the zero block can still degrade to $O(n)$ when most values are zero.
- **Zeros:** Both searches deliberately exclude zeros from their returned counts.
- **All one sign:** A boundary may lie at index `0` or `n`; the formulas remain valid without special cases.
- **Tied counts:** Returning `max` handles equality directly.
- **Non-decreasing duplicates:** Repeated negative or positive values do not affect boundary correctness.
