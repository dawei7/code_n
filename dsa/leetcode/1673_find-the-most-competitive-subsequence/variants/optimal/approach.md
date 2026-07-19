## General
**View the budget as removable elements.** Exactly $n-k$ values must be discarded. Scan `nums` from left to right while storing the best prefix chosen so far in a stack. A later smaller value should replace larger values at the end of that prefix whenever the remaining removal budget permits it.

**Remove a dominated suffix greedily.** Before appending the current value, repeatedly pop the stack while its top is greater, the stack is nonempty, and removals remain. Replacing the earliest possible larger selected value with the current smaller value makes the candidate lexicographically better. Values deeper in the stack are already fixed before that position, and popping consumes one of the deletions needed to keep the final length at $k$.

**Keep equal values stable.** Use a strict greater-than comparison for popping. Replacing an equal earlier value with a later copy cannot improve the current position and only discards future flexibility, so the earlier equal value remains.

**Spend unused removals on trailing candidates.** Append a scanned value after the beneficial pops only while the stack contains fewer than $k$ values. Once it is full, a current value that could not improve the stack is discarded and consumes one removal. This performs the trailing deletions online and keeps the stored prefix capped at the required output length.

**Why each greedy replacement is safe.** When a larger stack top is popped for a smaller current value, the result first differs from the old candidate at that popped position and is smaller there. The deletion budget proves enough total elements remain to complete length $k$. Any optimal candidate that kept the larger value at that position would therefore be lexicographically worse, so applying all such replacements cannot exclude the optimum.

## Complexity detail
Every input value is considered once, pushed at most once, and popped at most once, so the total stack work is $O(n)$. The stack is capped at the required output length and therefore uses $O(k)$ auxiliary space.

## Alternatives and edge cases
- **Repeated feasible-window minimum:** For each output position, scan the range in which the next choice may occur. This is correct but can inspect $O(nk)$ values.
- **Segment tree range minima:** Repeated minimum-index queries can achieve $O(k\log n)$ time, but the monotonic stack is simpler and asymptotically linear.
- **Sort by value:** Sorting loses the original relative-order requirement and does not produce a valid subsequence in general.
- If $k=n$, no deletion is available and the original array must be returned.
- If $k=1$, the smallest array value is chosen; among equal minima, the earliest is sufficient.
- A descending array spends the deletion budget removing its early large values.
- An ascending array leaves the stack intact and discards only its suffix.
- Equal values are preserved in their original order and may appear multiple times in the answer.
