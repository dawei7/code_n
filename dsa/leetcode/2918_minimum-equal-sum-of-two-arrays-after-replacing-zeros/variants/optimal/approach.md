## General

**Find each array's minimum attainable sum.** Every zero must become a
strictly positive integer, so assigning one to each zero produces the smallest
possible sum. For an array with original sum $s$ and $z$ zeros, that minimum is
$s+z$. If $z>0$, one replacement can absorb any additional non-negative
amount, so every sum at least $s+z$ is attainable. If $z=0$, the array has only
the single fixed sum $s$.

**Intersect the two attainable ranges.** When both arrays contain a zero,
their attainable sums are upward-unbounded intervals, whose smallest common
value is the larger minimum. The same value works when only the lower-minimum
array is flexible, because it can grow to the fixed or larger target. The only
impossible situation is therefore a lower-minimum array with no zero: its
fixed sum cannot reach the other array's minimum. Checking that condition in
both directions proves that returning the larger minimum in every remaining
case is both attainable and minimal.

## Complexity detail

Let $n=\lvert\texttt{nums1}\rvert$ and
$m=\lvert\texttt{nums2}\rvert$. Computing the two sums and zero counts
takes $O(n+m)$ time. Only a constant number of integer totals and counters are
stored, so the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Search replacement assignments:** Enumerating positive values for zeros has an unbounded search space and ignores that each flexible array attains every sum above its minimum.
- **Sort the arrays:** Ordering does not affect either sum or the number of zeros, so sorting adds unnecessary $O(n\log n+m\log m)$ work.
- **No zeros in either array:** Both sums are fixed; they succeed only when already equal.
- **Zeros in both arrays:** The larger of their two minimum attainable sums is always reachable by both.
- **Only one flexible array:** It can match the fixed array exactly when its own minimum does not exceed the fixed sum.
- **Every entry is zero:** Replacing each entry by one gives that array's minimum; any one zero can absorb further required growth.
- **Large totals:** Array sums can exceed 32-bit signed range, so implementations in fixed-width languages need a 64-bit total.

