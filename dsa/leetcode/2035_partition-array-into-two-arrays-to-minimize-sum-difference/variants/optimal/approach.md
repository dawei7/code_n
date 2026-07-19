## General
**Reframe the partition as a fixed-cardinality selection**

Let $T$ be the sum of all input elements, and suppose the first output group
has sum $A$. Its complement then has sum $T-A$, so the objective becomes
$\lvert 2A-T\rvert$. It is therefore enough to choose exactly $n$ elements
whose sum is as close as possible to $T/2$; the unchosen elements automatically
form the other valid group.

**Split and group the subset sums**

Divide `nums` into left and right halves of $n$ elements each. Enumerate every
subset of each half, but group its sum by the number of selected elements. A
left subset containing $k$ elements can combine only with a right subset
containing $n-k$ elements. This count grouping preserves the equal-length
requirement that an ordinary subset-sum search could accidentally lose.

Sort every right-hand sum group. Across both halves there are $2^n$ subsets
per side, far fewer than the subsets of the full $2n$-element array.

**Pair each left sum with its nearest compatible right sum**

For a left sum $L$ from the $k$-element group, the ideal compatible right sum
is $T/2-L$. Binary-search the sorted right group for count $n-k$. Only the
insertion position and its predecessor can be closest to that target, so test
both and update the answer with $\lvert T-2(L+R)\rvert$.

Every legal length-$n$ choice has a unique split into $k$ selected elements
from the left half and $n-k$ from the right. The enumeration therefore
considers its two component sums. Binary search chooses a compatible right sum
at least as close to the ideal as that choice's right component, so the best
recorded difference is no worse than any legal partition. Since every tested
pair is itself legal, the recorded minimum is exactly optimal.

## Complexity detail
There are $2^n$ subsets in each half. Computing their sums, grouping them by
cardinality, sorting the right groups, and searching once for each left subset
takes $O(n2^n)$ time in total. The grouped subset sums occupy $O(2^n)$ space.

## Alternatives and edge cases
- **Enumerate full length-$n$ combinations:** Testing all
  $\binom{2n}{n}$ choices is correct but approaches $4^n/\sqrt{n}$ work and is
  substantially slower than meet-in-the-middle.
- **Value-indexed dynamic programming:** Tracking reachable sums by chosen
  count depends on the total value range, which can reach hundreds of millions
  here and is not bounded suitably for a dense table.
- With $n=1$, the two input values must be separated, so their absolute
  difference is forced.
- Negative values do not change the reduction; subset sums and the target may
  both be negative.
- Duplicate values represent distinct array elements and may be chosen
  independently.
- An odd total sum can still have an even or odd minimum difference depending
  on the available fixed-size subset sums.
- The two middle binary-search candidates must both be checked, especially
  when the ideal sum lies between integers.
