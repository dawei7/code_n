## General
**Backward merging protects unread values in `nums1`**

Point `i` to the last valid value in `nums1`, `j` to the last value in `nums2`, and `write` to the final reserved position of `nums1`. Compare the two source endpoints, write the larger one at `write`, and move that source pointer and the destination left.

The destination is never before an unread `nums1` value: it begins after the valid prefix, and every write consumes one source value. This is why merging backward needs no buffer, while merging from the front would overwrite data still needed.

**Only a remaining `nums2` prefix needs explicit copying**

If `nums2` is exhausted first, any remaining `nums1` prefix is already in its final positions and the algorithm can stop. If `nums1` is exhausted first, copy the remaining `nums2` prefix backward into the open beginning. A single loop conditioned on $j \ge 0$ captures both cases.

**The filled suffix contains the globally largest merged values**

Positions after the destination pointer contain exactly the largest already-merged values in sorted order. Unconsumed source prefixes remain sorted, so their larger final value is always the correct next value to place.

**Trace equal values without losing multiplicity**

For `[1,2,3,0,0,0]` and `[2,5,6]`, place 6, then 5, then 3 at the right. Compare the two 2s and finish the remaining prefix, producing `[1,2,2,3,5,6]` without overwriting unread values.

**The largest remaining endpoint belongs at the destination end**

Because both unread prefixes are sorted, their greatest unmerged value must be one of their two current endpoints. Writing the larger endpoint into the rightmost open destination position therefore fixes that position permanently.

The destination index moves backward into reserved space or positions whose original value has already been consumed, so no unread `nums1` value is overwritten. Repeating until `nums2` is exhausted leaves either already-correct `nums1` values or a fully written merged prefix, making the entire array sorted and complete.

## Complexity detail
Each input value is compared and written at most once, giving $O(m+n)$ time. Three indices use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Merge from the front:** overwrites unread `nums1` values unless they are shifted or copied.
- **Concatenate and sort:** costs $O((m+n) \log(m+n))$ time and ignores existing order.
- **Allocate a merged array:** is straightforward but uses $O(m+n)$ extra space.
- $n = 0$ leaves `nums1` unchanged. $m = 0$ copies all of `nums2` into the reserved array.
- Either equal endpoint may be selected first; both copies remain and sorted order is preserved.
