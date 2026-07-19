## General
**Turn the count condition into a sorted boundary.** Sort the values in ascending order. At index $i$, the suffix from $i$ through the end contains exactly $x=n-i$ elements. This suffix is precisely the set of values at least $x$ when `nums[i] >= x` and either $i=0$ or `nums[i - 1] < x`.

**Check each possible suffix size once.** For every sorted index, compute `candidate = n - i` and test those two boundary inequalities. The current value proves all $x$ suffix members are at least $x$; the preceding-value test proves every element outside the suffix is smaller than $x$. Together they establish that the qualifying count is exactly $x$, not merely at least $x$.

If no boundary satisfies both conditions, no positive candidate works. The value $x=0$ cannot work for a nonempty non-negative array because all $n$ elements are at least zero, so returning `-1` is then correct.

## Complexity detail
Sorting $n$ values costs $O(n\log n)$ time, and the boundary scan costs $O(n)$. The app-local implementation creates a sorted copy, using $O(n)$ space and leaving the supplied array unchanged.

## Alternatives and edge cases
- **Count separately for every candidate:** Trying every $x$ from 0 through $n$ and rescanning the array is correct but takes $O(n^2)$ time.
- **Frequency buckets:** Since values are bounded, suffix counts over buckets can solve the problem in $O(n+M)$ time and $O(M)$ space for maximum value $M$.
- **Binary search with repeated lower bounds:** Sorting permits each threshold count to be found in $O(\log n)$, but the direct boundary scan is simpler and already linear after sorting.
- The candidate does not need to be present in `nums`; `[3, 5]` has answer 2.
- Elements equal to $x$ count because the comparison is greater than or equal to.
- All-zero nonempty arrays have no answer, including $x=0$.
- A one-element positive array has answer 1, while `[0]` has no answer.
