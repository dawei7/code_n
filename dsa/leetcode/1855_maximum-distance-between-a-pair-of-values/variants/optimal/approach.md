## General
Scan `nums2` from left to right with index `j`, while maintaining the smallest not-yet-discarded index `i` in `nums1`. If `nums1[i] > nums2[j]`, that `i` cannot pair with the current `j` or any later position of `nums2`, because later values are no larger. Advance `i` until its value is small enough or the first array is exhausted.

When `nums1[i] <= nums2[j]`, this `i` is the earliest remaining first-array index that can satisfy the value condition. If $i\le j$, it therefore gives the greatest distance ending at this `j`; update the answer with $j-i$.

Neither pointer moves backward. Discarded first-array indices are permanently impossible for all future second-array values, while every feasible current endpoint is paired with its farthest eligible start. Taking the maximum of those candidates yields the global optimum.

## Complexity detail
The `j` scan visits all $m$ entries of `nums2` at most once, and `i` advances through at most $n$ entries of `nums1`. The total time is $O(n+m)$. The two indices and running answer use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate all index pairs:** Directly checks the definition but costs $O(nm)$ time.
- **Binary search for every `i`:** Find the last qualifying `j` in the non-increasing second array for $O(n\log m)$ time.
- **Index condition:** A value-compatible pair with $i>j$ is invalid and must not produce a negative or reversed distance.
- **Equal values:** The comparison is non-strict, so equality is valid.
- **No positive distance:** The initialized answer 0 is correct.
- **Unequal lengths:** Either array may finish first; indices always belong to their own arrays.
- **Repeated plateaus:** Pointer monotonicity remains valid when many adjacent values are equal.
- **Exhausted first array:** Once every `nums1` value is too large, later smaller `nums2` values cannot recover a valid pair.
