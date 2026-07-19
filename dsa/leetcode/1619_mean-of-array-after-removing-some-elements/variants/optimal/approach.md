## General
**Expose the two exact tails by sorting.** Sort a copy of `arr` in ascending order. Because $n$ is divisible by 20, `trim = n // 20` is exactly 5% of the input size. The first `trim` positions are the required smallest elements and the final `trim` positions are the required largest elements, including the correct multiplicity when boundary values are tied.

**Average only the middle slice.** Keep the half-open slice `ordered[trim:n - trim]`. It contains exactly $n-2\cdot\texttt{trim}=0.9n$ elements. Divide its sum by its length using floating-point division.

Sorting establishes a total order over every element occurrence, so removing those two positional tails removes exactly the requested groups. Every remaining occurrence lies in the middle slice once, making the computed quotient precisely the trimmed mean.

## Complexity detail
Sorting $n$ values takes $O(n\log n)$ time. Summing the middle slice takes $O(n)$ additional time. The sorted copy and middle slice use $O(n)$ space; the original array is not mutated.

## Alternatives and edge cases
- **Counting frequencies:** Since values are bounded by $10^5$, a frequency array can trim counts from both ends in $O(n+10^5)$ time, but it uses domain-sized storage and more boundary bookkeeping.
- **Selection algorithms:** Finding both cutoff order statistics can avoid a full sort in expected $O(n)$ time, but ties at the cutoffs still require exact multiplicity accounting.
- **Repeated minimum and maximum removal:** Deleting one extreme at a time is simple but can take $O(n^2)$ time with ordinary arrays.
- Values equal to a cutoff are removed by occurrence count, not all at once.
- Exactly 10% of the elements are discarded in total, leaving a nonempty 90% middle.
- If every value is equal, trimming does not change the mean.
- The returned division must be floating point even when the exact mean is an integer.
