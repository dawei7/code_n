## General

Process the array from left to right. Once index $i$ is reached, no future operation can begin to its right and still affect it. Therefore, after accounting for earlier windows, the remaining value at index $i$ uniquely determines how many operations must start there.

**Forced greedy choice**

Maintain `active_decrements`, the total number of previously started operations whose length-$k$ windows still cover the current index. The current value would become `nums[i] - active_decrements`. A negative result means earlier forced operations have already decremented this position too many times, so no solution exists.

If the result is zero, no operation may start at this index: an additional decrement would make it negative. If it is positive, exactly that many operations must start here. Such a start is legal only when the window ending at index $i+k-1$ remains inside the array.

**Expiring window effects**

Use an expiration difference array. When `required` operations start at index $i$, add them to `active_decrements` and record `required` at position $i+k$. Before processing any index, remove the operations recorded to expire there. Each group of operations is therefore added and removed once, without visiting all $k$ affected positions.

Every decision is forced by the leftmost not-yet-cleared position. If the scan accepts a start, every valid solution must make the same start count there; if the scan rejects because of over-decrement or insufficient remaining length, no later operation can repair that position. Reaching the end proves that all positions can be cleared.

## Complexity detail

Let $n$ be the length of `nums`. The algorithm performs constant work at each index, so its time complexity is $O(n)$. The expiration array has $n+1$ entries, giving $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Apply each forced window directly:** Subtracting from all $k$ positions whenever a start is required is correct, but takes $O(nk)$ time in the worst case.
- **Store expirations in the input array:** The same linear scan can reuse `nums` as difference storage and achieve $O(1)$ auxiliary space, but it mutates the caller's input.
- **Queue active starts:** A queue can track when operation groups expire in $O(n)$ time and $O(n)$ worst-case space, but the indexed expiration array is simpler.
- When $k=1$, every position can be cleared independently, including values at the upper constraint.
- When $k=n$, all input values must be equal because every operation affects the entire array.
- An all-zero array succeeds without starting any operation.
- A positive value among the final $k-1$ positions fails if it was not fully covered by earlier windows, because no new length-$k$ window fits.
