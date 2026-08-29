## General

**Moving an element to the end means deferring it**

While scanning the original array, imagine keeping most encountered values in their relative order and deferring selected values until after all kept values. Each deferred value corresponds to one allowed move to the end.

Positive values never hurt a prefix, so there is no benefit in deferring them. Only negative values need consideration.

The solution maintains `s`, the sum of encountered values that have not been deferred, and a min-heap `h` of encountered negative values still eligible for deferral.

**React only when the retained prefix becomes negative**

For each `x`, the code first adds it to `s`. If $x$ is negative, it also pushes it into the heap.

As long as `s < 0`, at least one encountered negative must be moved behind the current prefix; otherwise this prefix can never become nonnegative.

The heap's smallest numeric value is the most negative value. Popping it and executing `s -= popped` removes its negative contribution from the retained prefix. Because subtracting a negative increases `s`, this repairs the deficit.

Each pop increments `ans` because it represents one element moved to the end.

**Why remove the most negative available value**

When one operation is necessary, every choice costs the same one move. Removing a more negative value increases the retained sum more than removing a less negative value.

For example, if the available negatives are $-8$ and $-3$, deferring $-8$ raises `s` by eight, while deferring $-3$ raises it by only three. The larger repaired balance is never worse for future prefixes and may prevent additional moves.

An exchange argument makes this formal. If an optimal plan at the current prefix defers $-3$ but keeps $-8$, swap their roles. The number of operations stays the same, and every retained prefix from their encounter onward becomes at least five larger. Feasibility cannot be lost. Therefore some optimal plan always defers the most negative value when forced.

**A greedy dominance invariant**

After processing each original position, the algorithm has used the minimum possible number of deferrals needed to make the retained scanned sequence nonnegative. Among all plans using that many deferrals, it maximizes the retained sum by removing the most negative values.

If `s` is nonnegative, using another operation now cannot reduce the count later more efficiently than waiting; the same negative remains available if a future deficit occurs.

If `s` is negative, every feasible plan must add at least one deferral among encountered negatives. Greedy takes the choice that maximizes the repaired sum, so it remains at least as prepared for the future as any equal-count plan. This preserves the invariant by induction.

**Why the heap always contains something when needed**

Before adding the current value, greedy's retained sum was nonnegative. If it becomes negative, the new value must be negative or earlier negative values remain kept. At least one negative contribution exists in the retained prefix and is present in `h`.

Thus `heappop` is safe whenever `s < 0`. In fact one pop is enough immediately after a single new element because removing the current negative would restore the previous nonnegative sum, but the exact `while` loop is robust and clearly enforces the invariant.

**Why appending deferred values stays valid**

The scan validates all prefixes of the kept elements. Afterward, deferred negative values are appended.

Let their total be $D\le0$. The sum before appending them is the original total minus $D$, which is at least $-D$ because the problem's feasibility guarantee implies the original total is nonnegative.

As deferred negatives are appended, the running sum decreases. Its smallest value occurs after all of them, when it equals the original total, still nonnegative. Therefore every appended-tail prefix is also safe, regardless of their order.

**Trace the second sample**

For `[3,-5,-2,6]`:

- after $3$, `s=3`;
- after $-5$, `s=-2` and heap contains $-5$, so defer it and restore `s=3`; operations become one;
- after $-2$, `s=1`, still valid;
- after $6$, `s=7`.

The kept order is `[3,-2,6]` and deferred $-5$ is appended, giving prefix sums $3,1,7,2$. One operation is minimal.

**The algorithm counts operations without building the array**

The heap identifies which negative values conceptually move, but the function does not reconstruct their positions or final order. Only the minimum number is requested, and the proof shows a valid final order exists.

The input `nums` is never modified.

## Complexity detail

Let $n$ be the array length. Each negative value is pushed once and popped at most once. Heap operations cost $O(\log n)$, while the scan is linear, giving $O(n\log n)$ worst-case time.

The heap can store $O(n)$ negative values, so auxiliary space is $O(n)$. Scalar sums and counters use $O(1)$ additional space.

## Alternatives and edge cases

- **Move the current negative:** This can be suboptimal when an earlier, more negative value would repair more balance for the same operation.
- **Sort the entire array:** Arbitrary reordering is not allowed; only selected elements may move to the end while others retain order.
- **Dynamic programming:** It can model retained sums but is unnecessary because the most-negative exchange gives a greedy optimum.
- **No negative prefix:** Heap entries may accumulate, but no pop occurs and the answer is zero.
- **Multiple negative values:** The heap chooses by magnitude rather than recency.
- **Zero values:** They neither hurt the sum nor enter the negative heap.
- **Guaranteed feasibility:** It implies total sum is nonnegative, ensuring the deferred tail can be appended safely.
- **Repeated negatives:** Each occurrence is a separate heap entry and possible operation.
- **Input preservation:** Deferrals are conceptual; the source array is not rearranged.
