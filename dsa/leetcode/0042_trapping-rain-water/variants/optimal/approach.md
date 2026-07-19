## General
**Water at one bar is fixed by the lower side maximum**

For position `i`, trapped water is `min(max_left[i], max_right[i]) - height[i]`. Precomputing both maximum arrays works, but the same information can be finalized from the ends with two pointers.

Track `left_max` and `right_max` while pointers bound the unprocessed interval. When `height[left] <= height[right]`, the current right bar is a known opposite boundary at least as tall as the current left bar. The history of pointer choices also ensures that if `left_max` is taller than that right boundary, the right side would have been processed instead before this state could make the left calculation unsafe. Thus the left position's limiting side is known, and `left_max - height[left]` is final after updating `left_max`. Process right symmetrically when its current bar is lower.

**Once a side is selected, future interior bars cannot change its water**

Before each iteration, all positions outside `[left, right]` have their final water counted exactly once; `left_max` and `right_max` are the greatest bars seen from their respective ends. Selecting the lower current boundary proves an adequate wall exists on the opposite side. Any future bar inside the interval can raise that opposite maximum but cannot lower it, so it cannot reduce or otherwise revise the selected position's water.

Updating the selected side's maximum before adding water also prevents negative contributions: a new record-height bar traps zero above itself.

**Trace a basin whose right wall is already sufficient**

For `[4, 2, 0, 3, 2, 5]`, the left boundary 4 is lower than right boundary 5. Moving inward under left maximum 4 adds 2 above height 2, 4 above height 0, 1 above height 3, and 2 above height 2, totaling 9.

**The lower boundary makes one side's water final**

When the left boundary is no higher than the right boundary, some wall on the right is already tall enough not to be the limiting side for the current left position. The trapped level there is determined entirely by the best left wall seen so far, so `left_max - height`—clamped at zero—is final. Future interior bars cannot lower that established opposite boundary.

The symmetric argument applies when the right boundary is lower. Advancing exactly the decided pointer processes every interior position once, and each contribution uses the smaller of its true left and right maxima, yielding the exact total water.

## Complexity detail
Exactly one pointer advances on every iteration, so every bar is processed once and time is $O(n)$. Two pointers, two maxima, and the accumulated volume use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Precompute left and right maxima:** runs in linear time but uses $O(n)$ extra arrays.
- **Monotonic stack:** also runs in $O(n)$ and computes water by bounded horizontal layers, using $O(n)$ space.
- **Scan both sides for every bar:** directly applies the formula but requires $O(n^2)$ time.
- Empty arrays and arrays shorter than three bars trap no water; the pointer loop naturally returns zero.
- Equal boundary heights may process either side. Plateaus and zero-height bars require no special cases.
