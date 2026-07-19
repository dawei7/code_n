## General
**Characterize a legal boundary**

A cut after index `i` is valid exactly when every value in `arr[:i + 1]` is no greater than every value in `arr[i + 1:]`. This is equivalent to `prefix_max[i] <= suffix_min[i + 1]`. If the inequality fails, some left value must appear after a smaller right value in the concatenated chunk results, contradicting global sorted order.

**Precompute one side and scan the other**

Build `suffix_min`, where each entry is the minimum value from that index to the end. Then scan left to right while maintaining the prefix maximum. Count every boundary satisfying the inequality, and add one for the final chunk.

Every counted boundary separates two value ranges that are already globally ordered. Applying this condition at all chosen boundaries ensures that after each chunk is internally sorted, no value crosses a boundary out of order. Conversely, every valid chunk partition must use only boundaries satisfying the same necessary inequality. Counting all such boundaries therefore gives the maximum possible number of chunks, including when equal values lie on both sides.

## Complexity detail
Constructing suffix minima and scanning prefix maxima each take $O(n)$ time. The suffix array uses $O(n)$ space; the remaining state is constant.

## Alternatives and edge cases
- **Monotonic stack of chunk maxima:** Start a new chunk for nondecreasing values and merge prior chunks after a drop; each value is pushed and popped once for $O(n)$ time and $O(n)$ space.
- **Compare prefixes with the globally sorted array:** Matching frequency maps at each index gives a valid $O(n \log n)$ approach because of the initial sort.
- **Rescan both sides at every boundary:** Directly testing each prefix maximum and suffix minimum is correct but takes $O(n^2)$ time.
- **Strictly descending array:** Only one chunk is possible.
- **Already nondecreasing array:** Every element can be a separate chunk.
- **Equal values across a boundary:** Equality is allowed, so the condition uses `<=`, not `<`.
- **Single element:** It forms one chunk.
