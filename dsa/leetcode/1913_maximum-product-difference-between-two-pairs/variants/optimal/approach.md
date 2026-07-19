## General
**Reduce the choice to four extrema**

Because every value is positive, increasing either factor in the added product can only improve the result. Its best possible factors are therefore the largest and second-largest array elements. Likewise, decreasing either factor in the subtracted product improves the result, so that product uses the smallest and second-smallest elements.

These four order statistics correspond to four distinct positions. If values are equal, sequential tracking still records two separate occurrences, which satisfies the distinct-index requirement.

**Track the extrema in one pass**

Maintain two slots for the smallest values and two for the largest values. A new value that reaches the first slot shifts its former occupant into the second slot; otherwise it may replace only the second slot. Use inclusive comparisons for the first slots so duplicate extrema occupy both positions when they occur twice.

After the scan, return `largest * second_largest - smallest * second_smallest`. Every alternative added product is no larger, and every alternative subtracted product is no smaller, so no other four-index selection can produce a greater difference.

## Complexity detail
The algorithm examines each of the $N$ values once and performs constant work per value, giving $O(N)$ time. The four tracked extrema use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Sort the array:** Sorting and using the first two and last two values is concise, but takes $O(N\log N)$ time and may use nonconstant auxiliary space.
- **Selection sort:** It also exposes the needed endpoints but takes $O(N^2)$ comparisons.
- **Exactly four elements:** All positions must be used, although their assignment to the two products remains determined by the extrema.
- **Duplicate extrema:** Two equal minimum or maximum values at different indices are both valid factors.
- **All values equal:** The two products are equal, so the answer is zero.
- **Domain extremes:** Products fit the required result range, but implementations in fixed-width languages should still use an adequately wide numeric type.
