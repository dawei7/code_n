## General
Convert the requested descending rank to the ascending target index $n - k$. Quickselect can place that index without sorting every other value.

Within an active range, sample three positions independently, use the median sampled value as the pivot, and apply a
Dutch-national-flag partition:

- values smaller than the pivot occupy the left region,
- values equal to it occupy one contiguous middle region,
- values greater than it occupy the right region.

After partitioning, every index in the middle region has its final rank value even though the outer regions are internally unsorted. If the target index lies there, return the pivot. Otherwise continue only in the side containing the target.

The three-way partition is particularly important for duplicates. In `[3,2,3,1,2,4,5,5,6]`, a pivot value appearing several times is resolved as one block; the search never repeatedly partitions those equal values. Duplicate occurrences still count as separate ranks because the middle block spans one index per occurrence.

The reviewed candidate samples a fresh median-of-three pivot from the active range and mutates `nums`. Randomization
makes the expected bound independent of the input's initial ordering, while taking the sample median reduces the chance
of an extreme pivot. If preserving the input is required, a copy is necessary and changes the auxiliary-space bound.

Partitioning establishes that every left-region value is below every pivot-equal value and every right-region value is above it. Thus the equal block occupies exactly the pivot's final rank interval. If the target lies inside, the pivot is the required value. If it lies outside, all values in the discarded regions have final ranks on the wrong side, so restricting the active range preserves the target. Repeating eventually places the target in an equal block and returns the kth-largest value.

## Complexity detail
Each sample position is uniform over the active range, so its median is biased away from extreme ranks. The expected
active range therefore shrinks geometrically and the expected total partition work is $O(n)$. The worst case remains
$O(n^2)$ if chance repeatedly produces extreme pivots; median-of-medians can guarantee linear worst-case time at greater
implementation cost. Partitioning is in place and uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Full sorting:** It takes $O(n \log n)$ time but is simple and deterministic.
- **Bounded min-heap:** A heap of size `k` takes $O(n \log k)$ time and $O(k)$ space and supports streaming input.
- **Median-of-medians:** It guarantees $O(n)$ worst-case selection but is substantially more complex.
- **Distinct-only ranking:** It is incorrect because duplicate occurrences occupy separate ranks.
- **Boundary ranks and values:** All-equal arrays terminate through the middle block; negative values and $k = 1$ or
  $k = n$ need no special handling.
