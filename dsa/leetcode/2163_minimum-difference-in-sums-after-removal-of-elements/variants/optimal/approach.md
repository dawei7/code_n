## General

**Turn each removal into an original-array split**

After removals, some original position separates the first $n$ retained values
from the final $n$. That separator can lie after any index $i$ from $n-1$
through $2n-1$. For a fixed $i$, minimizing the signed difference requires the
$n$ smallest values from `nums[0:i+1]` on the left and the $n$ largest values
from `nums[i+1:3n]` on the right. Any other retained left value could be
exchanged for a smaller available one, and any other retained right value could
be exchanged for a larger available one.

**Build the best left sum for every separator**

Scan the first $2n$ values from left to right while a max-heap retains the
smallest $n$ values seen so far. The negated root identifies the largest
retained value. Once the heap has $n$ entries, replace that root only when a
smaller value arrives. Record the retained sum at every possible separator.

**Combine with the best right sum**

Scan from the end toward index $n$ with a min-heap that retains the largest
$n$ values in the current suffix. Replace its smallest retained value whenever
a larger value arrives. For each separator, subtract this suffix sum from the
previously recorded prefix sum.

Every legal removal has one such separator, and the exchange choices are
optimal for that separator. Taking the minimum over all separators therefore
finds the global minimum difference.

## Complexity detail

There are $3n$ values. Each enters at most one size-$n$ heap, and a heap update
costs $O(\log n)$, so the total time is $O(n\log n)$. The prefix sums and two
heaps use $O(n)$ auxiliary space.

The benchmark defines its `size` as the full array length $3n$. Deterministic
mixed-value tiers force replacements in both directional heaps and avoid
presorted-input shortcuts. A method that re-sorts each candidate prefix and
suffix takes $O(n^2\log n)$ on the same workload.

## Alternatives and edge cases

- **Sort each prefix and suffix independently:** This directly implements the
  fixed-separator choice and is useful as a correctness oracle, but repeats
  sorting for every separator and takes $O(n^2\log n)$ time.
- **Balanced ordered multisets:** Two multisets with running sums can maintain
  the selected and rejected values in $O(n\log n)$ time, but Python has no
  built-in ordered multiset and heaps are simpler.
- The difference is signed; a large right sum can make the optimal answer
  negative.
- Exactly $n$ elements must be removed, even when all values are equal.
- Duplicate values are independent positions, and either copy may be retained
  without changing its contribution.
- When $n=1$, each possible single removal corresponds to one of the two
  separator positions.
