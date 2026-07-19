## General
**Retain the same minimum-containing closed interval**

As in problem 153, maintain `[left,right]` containing at least one global minimum and compare `nums[mid]` with the right endpoint. Strict comparisons still expose which rotation segment contains `mid`; duplicates add one ambiguous case.

**Greater and smaller midpoint values retain logarithmic elimination**

If `nums[mid] > nums[right]`, discard through `mid` because the minimum lies strictly right. If `nums[mid] < nums[right]`, retain `mid` and discard positions after it. These cases remove approximately half the interval exactly as in the distinct array.

**Equality permits removing only a redundant endpoint**

When `nums[mid] = nums[right]`, either side may contain the pivot. Decrement `right` by one. If that removed endpoint was a minimum, the equal midpoint inside the retained interval is another occurrence of the same minimum; otherwise removing it plainly cannot lose the minimum.

No comparison can safely discard half in this case. An array of all equal values therefore forces linear endpoint shrinking.

**The interval contains at least one minimum occurrence**

The closed search interval always contains a minimum value. Strict comparisons discard a segment known not to contain it; equality removes only a redundant endpoint value.

**Trace a minimum hidden between equal values**

For `[10,1,10,10,10]`, midpoint and right values are repeatedly equal, so right shrinks until an informative comparison exposes `1`. The algorithm never assumes the equal `10` region is wholly on one rotation side.

**Equal values permit only a cautious one-step reduction**

The strict comparisons retain the minimum for the same reason as in the distinct-value problem: a middle value above the right endpoint places the pivot to the right, while a smaller middle value places it at or to the left of `mid`.

When `nums[mid] = nums[right]`, the comparison cannot identify a side. Discarding only `right` is nevertheless safe: if that endpoint holds the minimum, the equal value at `mid` remains in the interval as another occurrence. Every iteration therefore preserves at least one global-minimum occurrence, and the final single index must hold that value.

## Complexity detail
Most comparisons halve the interval, but equal values can force removing only one endpoint, so the worst case is $O(n)$ time. Boundary indices use $O(1)$ space.

## Alternatives and edge cases
- **Linear `min`:** has the same worst-case bound but discards the logarithmic behavior available when comparisons are informative.
- **Apply distinct-value binary search unchanged:** can discard the wrong side when both endpoints equal the middle.
- **Remove all duplicates first:** costs extra space or mutation and still requires a scan.
- All values may be equal. The minimum can be surrounded by duplicates, occur at either endpoint, or appear more than once across the rotation boundary.
- Worst-case $O(n)$ is inherent to comparison ambiguity, but informative inputs still obtain binary-search behavior.
