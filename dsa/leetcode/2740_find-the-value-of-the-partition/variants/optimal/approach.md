## General

The two values used by any partition, `max(nums1)` and `min(nums2)`, are elements of the original array. Consequently, no partition can have a value smaller than the minimum absolute difference between any pair of array elements.

**Why adjacent sorted values are sufficient.** Sort `nums` in non-decreasing order. A pair with the minimum absolute difference must be adjacent in this order; if another value lay strictly between its endpoints, one of the two smaller sub-gaps would be no larger. Scan every adjacent pair and keep the smallest difference.

This lower bound is attainable. For adjacent sorted values $a_i$ and $a_{i+1}$, place all values through $a_i$ in `nums1` and all later values in `nums2`. Then the first group's maximum is $a_i$ and the second group's minimum is $a_{i+1}$, so the partition has exactly that adjacent gap. Thus the smallest scanned gap is both a lower bound on every partition and the value of a valid partition.

## Complexity detail

Let $n$ be the number of elements. Sorting takes $O(n\log n)$ time and the adjacent scan takes $O(n)$, for $O(n\log n)$ total time. Python's in-place list sort may use $O(n)$ auxiliary memory in the worst case, so the package records $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Compare every pair:** The minimum pairwise absolute difference gives the same answer, but examining all pairs takes $O(n^2)$ time.
- **Ordered balanced tree:** Inserting values one by one and comparing each insertion with its predecessor and successor also takes $O(n\log n)$ time, with more data-structure overhead.
- **Counting array:** A frequency array can find duplicates and adjacent present values quickly only when the value range is small; values here may reach $10^9$.
- Duplicate values make the optimal partition value zero because separate copies can occupy the two groups.
- With exactly two elements, the answer is their absolute difference.
- Sorting may mutate the app-local input, which is acceptable because no post-call input preservation is required.
- Differences fit within the stated value range, but fixed-width languages should still use their ordinary integer type safely.
