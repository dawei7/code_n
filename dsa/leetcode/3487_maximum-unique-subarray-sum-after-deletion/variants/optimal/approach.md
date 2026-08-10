## General

**Arbitrary deletions turn the choice into a distinct-value subsequence.** After deleting any number of elements, the elements kept between the chosen subarray's endpoints become contiguous in the remaining array. Therefore, any nonempty subsequence of the original order can be realized as the selected subarray: delete everything else, then select the entire remaining sequence.

The original-order condition does not restrict the sum because addition is order-independent. The task becomes choosing a nonempty set of occurrences whose values are distinct and whose sum is maximum.

**When a positive value exists, keep one copy of every positive value.** Every positive distinct value strictly increases the sum, so excluding one cannot be optimal. Multiple copies of the same positive value cannot both appear because the selected subarray must have unique elements, but keeping any one occurrence gives the same contribution.

Negative values strictly decrease the sum and should be deleted. Zero neither increases nor decreases it, so including or excluding one zero does not affect the optimum once a positive sum exists.

The source first computes `mx = max(nums)`. If `mx > 0`, at least one positive exists and the main loop applies this greedy rule. Set `s` records values already retained. A value is skipped if `x < 0` or `x in s`. Otherwise, it is added to `ans` and inserted into the set.

Because the condition skips only values below zero, the source may keep one zero. Adding it changes nothing, and storing it prevents duplicate zeros. The resulting sum still equals the sum of all distinct positive values.

For `nums = [1,2,-1,-2,1,0,-1]`, the loop adds $1$, $2$, and one zero, skips negative values and the duplicate $1$, and returns $3$. Deleting unwanted positions can leave a sequence such as `[1,2,0]`; it is unique and has the same maximum sum. The example's `[2,1]` is another equally valued realization.

**When no positive value exists, the nonempty rule changes the answer.** If every value is zero or negative, deleting all elements would yield sum zero but is forbidden. A unique subarray containing a single occurrence is always legal, so the best possible sum is the largest array value `mx`.

If zero appears, `mx=0` and one zero is optimal. If all values are negative, choosing more than one can only make the sum smaller, so the least negative single value is optimal. The early branch `if mx <= 0: return mx` handles both.

For `[1,1,0,1,1]`, a positive value exists. The set keeps one $1$ and possibly zero, yielding sum one. For an input such as `[-5,-2,-2]`, the early return gives $-2$, realized by retaining one copy.

**Why contiguity after deletion causes no hidden obstacle.** Choose one occurrence of every retained distinct value in their original relative order. Delete all other elements. The retained occurrences then form the whole remaining array and hence a contiguous subarray. This construction proves every value set used by the greedy sum is feasible.

**Why the greedy sum is optimal.** In the positive case, any feasible result contains each value at most once. Removing a negative selected value improves its sum; adding a missing positive value at one chosen occurrence improves its sum and preserves uniqueness. Repeating these exchanges converts any optimum into exactly one copy of every positive distinct value, with optional zero. The source computes that sum.

In the nonpositive case, every additional selected value is at most zero. A single maximum value is at least as good as any nonempty combination and satisfies uniqueness. Thus the early return is exact.

The method returns only the maximum sum, so it does not need to remember which occurrence of a duplicate positive value was retained.

## Complexity detail

Computing `max(nums)` scans $n$ elements. In the positive case, the loop scans them once more. Set membership and insertion take expected $O(1)$ time, so total expected time is $O(n)$.

The set contains at most one value from $0$ through $100$ because negatives are never inserted and input values lie in $[-100,100]$. Its maximum size is therefore $101$, a fixed constant independent of $n$. Under the problem's bounded value domain, auxiliary space is $O(1)$, matching the manifest.

For an unbounded-value generalization, the same implementation would use $O(u)$ space for $u$ distinct nonnegative values, up to $O(n)$. The local editorial reports that generic bound; the manifest uses the tighter constraint-aware bound.

## Alternatives and edge cases

- **Maximum-unique sliding window:** Sliding windows solve the no-deletion version, but arbitrary deletions let nonadjacent positive values be joined, making a window unnecessary.
- **Dynamic programming over subsequences:** Positivity and uniqueness reduce the choice to one copy per positive value, so DP adds no value.
- **Keep duplicate positives:** That violates the unique-elements rule even though duplicates would increase the numeric sum.
- **Keep negative values between positives:** They can be deleted, after which the positive occurrences become adjacent in the remaining array.
- **Include zero:** One zero is harmless in the positive case and optimal by itself when no positive exists but zero is present.
- **All negative:** Returning zero would violate the nonempty requirement; the largest single element is correct.
- **Repeated maximum negative:** Only one occurrence is needed to form the optimal one-element subarray.
- **All positive and distinct:** Every element is kept and the answer is their total sum.
- **All positive and equal:** Exactly one copy contributes because values must be unique.
- **Original-order preservation:** Chosen occurrences remain in order after deletion, but their sum and distinctness do not depend on that order.
- **Bounded value range:** It justifies the manifest's constant-space claim for the set.
- **Input preservation:** The array is scanned without mutation; deletions are a conceptual feasibility argument rather than operations performed by the code.
