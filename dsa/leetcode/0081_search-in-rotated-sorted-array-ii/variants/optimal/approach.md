## General
**Use sorted-range elimination whenever rotation is visible**

Check the midpoint against the target first. If `nums[left] <= nums[mid]` and ambiguity has been excluded, the left half is nondecreasing. Retain it only when `nums[left] <= target < nums[mid]`; otherwise retain the other half. If the left half is not sorted, the right half is, and the symmetric range test applies.

**Equal values at all three probes erase ordering information**

When left, midpoint, and right values are all equal, either side might contain the rotation boundary, so neither half can be certified from values alone. Increment `left` and decrement `right` to discard one copy from each boundary.

This is safe because the midpoint comparison already proved that shared value is not the target. If the target exists elsewhere, removing equal non-target boundary copies leaves an occurrence inside. The price is that an all-equal interval shrinks only linearly rather than being halved.

**The interval retains an occurrence, not necessarily every occurrence**

If the target exists, at least one occurrence remains inside the inclusive interval. Sorted-range comparisons discard only halves that cannot contain it, while ambiguous-boundary shrinking removes values already known unequal to the target.

**Trace a pivot hidden by duplicates**

For `[1,0,1,1,1]` and target 0, equal endpoint and midpoint values first force boundary shrinking. Once the pivot becomes visible, the sorted-half test retains the segment containing 0 and finds it.

**Equal boundaries can be discarded only in the ambiguous case**

When one half is provably sorted, its endpoint range determines exactly whether the target can occur there; the other half is safe to discard or retain by the usual rotated-search rule.

If left, midpoint, and right values are equal, duplicates hide the pivot and neither half can be classified. After the midpoint has failed the target check, equal boundary values cannot be the target either, so removing those endpoints loses no occurrence. These two forms of elimination preserve every possible match until equality is found or the interval becomes empty.

## Complexity detail
Ordinary iterations halve the interval, but all-equal duplicates may shrink it by only two positions, so the worst case is $O(n)$ and the typical distinct-value behavior is $O(\log n)$. Only bounds and a midpoint use $O(1)$ space.

## Alternatives and edge cases
- **Linear scan:** matches the worst-case bound but forfeits logarithmic elimination on informative inputs.
- **Distinct-value rotated binary search:** fails when duplicates hide which side is ordered.
- **Deduplicate into a new array:** spends $O(n)$ space and still requires careful pivot handling.
- Duplicate ambiguity makes linear worst-case time unavoidable for this comparison strategy; `[1,1,...,1,0,1,...,1]` may reveal the distinct value only after many boundary shrinks.
- A one-element interval is checked at its midpoint before any boundary is removed.
