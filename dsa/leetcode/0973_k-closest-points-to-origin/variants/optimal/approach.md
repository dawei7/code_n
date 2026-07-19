## General
**Compare squared distances:** Computing a square root cannot change which of two nonnegative squared distances is smaller. The selection can therefore use `x * x + y * y`, avoiding floating-point arithmetic.

**Partition around a candidate distance:** Quickselect uses the same partitioning idea as quicksort. Choose a pivot distance, then move every point with a smaller distance before it and every point with a larger distance after it. Once partitioning finishes, the target index `k - 1` lies either in the left region, in the right region, or between their boundaries. Only the region containing that index can still affect the answer, so the algorithm discards the other region.

The implementation repeats this process until the first `k` positions contain precisely the points whose distances have the $K$ smallest ranks. The uniqueness guarantee rules out an ambiguous tie at the selection boundary. Returning the slice `points[:k]` is valid because the requested order is arbitrary.

**Why the selected prefix is correct:** Each partition permanently separates values below the pivot from values above it. If `k - 1` is left of the completed partition, no point in the discarded right region can belong ahead of that rank; the symmetric argument applies when the target is on the right. When the target falls between the two scan boundaries, every point before the prefix boundary is no farther than every point after it, so the prefix contains exactly the required set.

## Complexity detail
Let $N$ be the number of points and $K$ the requested count. A partition scans the active region once. With representative pivots, the active region shrinks geometrically, giving expected $O(N)$ time. Deterministic pivot choices can produce a worst case of $O(N^2)$ on adversarial orderings. Partitioning itself uses $O(1)$ auxiliary space; the returned list contains $K$ points, so total result space is $O(K)$.

## Alternatives and edge cases
- **Sort all points:** Sorting by squared distance is concise and deterministic, but it spends $O(N\log N)$ time even though only the first $K$ ranks are required.
- **Size-$K$ max-heap:** Keeping the closest $K$ points seen so far gives $O(N\log K)$ time and $O(K)$ space, with predictable performance when adversarial quickselect behavior is a concern.
- **All points requested:** When $K=N$, every input point belongs in the answer; its order remains unrestricted.
- **Negative and zero coordinates:** Squaring each coordinate handles every quadrant and points on either axis without special cases.
- **Equal internal distances:** Several points may share a distance away from the cutoff; the guarantee only ensures that the final selected set is unique.
