## General

**Keep the target inside one inclusive candidate interval**

The array was non-decreasing before one rotation, so it consists of at most two non-decreasing runs joined at the rotation boundary. The algorithm maintains an inclusive interval `[l, r]` that contains the target if the target exists anywhere not already discarded.

At each step, `mid` is the lower middle. Comparing `nums[mid]` with `nums[r]` reveals which side is certainly ordered unless equal duplicates hide that information. The method never needs to locate the pivot explicitly.

Unlike a distinct-value rotated search, equality between boundary values can make it impossible to know which copy lies on which side of the rotation. The third branch handles exactly that ambiguity.

**When the midpoint is greater than the right endpoint**

If `nums[mid] > nums[r]`, a rotation boundary must occur somewhere after `mid`. The interval from `l` through `mid` is therefore non-decreasing and belongs to the higher-valued run.

The test `nums[l] <= target <= nums[mid]` asks whether the target value lies within that sorted half's closed value range. If it does, `r = mid` retains the midpoint because it might equal the target. If it does not, no value in that ordered half can match, so `l = mid + 1` discards it.

Keeping `mid` in the first branch matters because there is no separate equality check before the branch. If `target == nums[mid]`, the range test is true and the candidate remains for the final comparison.

**When the midpoint is less than the right endpoint**

If `nums[mid] < nums[r]`, the interval from `mid` through `r` is certainly non-decreasing and belongs to the lower or unrotated run.

The condition `nums[mid] < target <= nums[r]` uses a strict lower bound because choosing the right side performs `l = mid + 1` and discards `mid`. Equality with `nums[mid]` must not enter that branch. When the condition is true, the target can lie only to the right of `mid`. Otherwise, `r = mid` keeps the midpoint and searches the other side.

The different inclusivity in the two ordered-half tests is coupled to the boundary assignments. It is not a cosmetic detail.

**When duplicates make the halves indistinguishable**

If `nums[mid] == nums[r]`, the comparison cannot reveal whether `mid` and `r` belong to the same sorted run or straddle the rotation. Halving the interval based on order would be unsafe.

The source instead performs `r -= 1`. Discarding that endpoint cannot remove the only possible target occurrence. If `nums[r]` is not the target, it is irrelevant. If it is the target, then `nums[mid]` has the same value and remains in the interval because `mid < r` while the loop is active. Thus one duplicate can be removed without losing membership information.

This step may shrink the search by only one position. It is the reason duplicates worsen the worst-case time from logarithmic to linear.

**Trace the ambiguity case**

Consider an interval whose midpoint and right endpoint are both 1 while the target is 2. Equality provides no evidence about which side is sorted. Decreasing `r` removes one redundant 1 and repeats the analysis. In an array of all ones with absent target 2, this happens for nearly every element, producing linear work.

In contrast, for `[2,5,6,0,0,1,2]` with target 0, comparisons eventually identify an ordered half whose value range contains zero and retain it. The interval converges to an occurrence of zero, and the final comparison returns true.

**An invariant and termination proof**

Initially `[l, r]` is the complete nonempty array, so it contains every possible occurrence. In the greater and lesser branches, the identified half is sorted, and its endpoint comparisons safely determine whether the target can lie there. The selected update retains every possible target occurrence. In the equality branch, either the discarded right value is not the target or an equal retained midpoint is another occurrence.

Every update strictly shortens the interval: `l` rises above `mid`, `r` becomes `mid`, or `r` decreases by one. Eventually `l == r`. The invariant then says that if the target existed, this sole candidate has its value. Returning `nums[l] == target` is therefore true exactly for membership.

The source depends on the contract's nonempty-array guarantee. With an empty list, the final indexed comparison would be invalid.

## Complexity detail

When comparisons identify an ordered half, the interval is roughly halved, giving logarithmic behavior. With many duplicates, `nums[mid] == nums[r]` can force one-at-a-time right-boundary reductions. The worst-case time is therefore $O(n)$, matching the manifest; the favorable distinct-value case is $O(\log n)$.

Only boundaries and a midpoint are stored. The search is iterative and allocates no collection, so auxiliary space is $O(1)$, also matching the manifest.

## Alternatives and edge cases

- **Compare with the left endpoint:** An equivalent rotated binary search can classify halves using `nums[mid]` versus `nums[left]` and skip ambiguous left duplicates.
- **Trim both equal endpoints:** When left, middle, and right values are equal and not the target, increment left and decrement right. It may improve constants but retains linear worst-case behavior.
- **Linear scan:** It is simpler and has the same worst-case asymptotic bound, but gives up logarithmic behavior on informative inputs.
- **Find a rotation pivot first:** Duplicate values make pivot finding itself potentially linear, so it does not improve the worst case.
- **One element:** The loop is skipped and final equality returns membership directly.
- **All elements equal, target present:** Convergence may be linear, but the final remaining value matches.
- **All elements equal, target absent:** Right shrinks one position at a time, demonstrating the $O(n)$ lower-information case.
- **Target equals midpoint:** Inclusive boundary logic keeps `mid` even without an early equality return.
- **Target equals discarded right duplicate:** An equal midpoint remains, so membership is preserved.
- **No rotation:** One side is repeatedly recognized as sorted, behaving like ordinary binary search unless duplicates cause ambiguity.
- **Negative values:** Only order and equality matter.
- **Nonempty contract:** The direct final access assumes at least one element.
- **Input preservation:** The method changes only indices, never array values.
