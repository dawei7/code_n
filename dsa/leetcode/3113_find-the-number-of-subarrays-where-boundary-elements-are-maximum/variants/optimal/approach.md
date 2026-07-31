## General

**Count subarrays by their right boundary.** Fix an index as the right endpoint and call its value `value`. A valid subarray ending there must begin at either the same index or an earlier occurrence of `value`. That earlier occurrence is usable exactly when no element greater than `value` lies between the two endpoints. The task is therefore to count the still-visible equal values for every right endpoint.

Maintain a stack of pairs `(value, count)` whose values are non-increasing from bottom to top. Each count records how many occurrences of that value have appeared since the nearest greater value that would block them from a later equal endpoint. When the current value is larger than the stack top, pop that smaller group: the current element is now a greater blocker, so none of those occurrences can form a valid subarray ending at a future equal value across this position. Every group is pushed once and can be popped only once.

After all smaller groups are removed, an equal top group represents exactly the previous left boundaries that can pair with the current endpoint. Increment its count to include the current position. If the top is greater, or the stack is empty, push a new group with count $1$ because only the singleton subarray currently qualifies at this value. In either case, add the top group's count to the answer: it counts the singleton plus every valid subarray ending here at an earlier equal boundary.

The stack retains a value occurrence precisely while no greater element has appeared after it. Consequently, every counted pair has equal endpoints and no larger interior value, so its subarray is valid. Conversely, the left endpoint of any valid subarray cannot have been popped, because popping requires a greater intervening value; it remains in the equal group and is counted at the right endpoint. Summing these disjoint right-endpoint contributions counts every valid subarray exactly once.

## Complexity detail

Let $n$ be the length of `nums`. Each array value creates at most one stack entry and each entry is popped at most once, so the total time is $O(n)$. A decreasing array can leave all $n$ distinct values on the stack, requiring $O(n)$ auxiliary space. The answer can be as large as $n(n+1)/2$, so implementations in fixed-width languages need a 64-bit integer.

## Alternatives and edge cases

- **Quadratic endpoint expansion:** Extending every left endpoint while maintaining the current maximum is straightforward and correct, but it takes $O(n^2)$ time when all values are equal.
- **Range maximum queries plus occurrence searches:** A segment tree and per-value position lists can test or count candidates in $O(n \log n)$ time, but the monotonic stack removes the logarithmic factor and uses simpler state.
- **Offline disjoint-set processing:** Activating indices from larger values to smaller values can group positions that are not separated by a greater blocker, but it is more elaborate and normally requires sorting.
- **Singletons:** Every element contributes at least one valid subarray, even when all values are distinct.
- **All values equal:** Every subarray is valid, producing the triangular total $n(n+1)/2$.
- **Smaller values between equal endpoints:** They do not invalidate the pair because the equal boundary value remains the subarray maximum.
- **A larger intervening value:** It blocks the equal endpoints and causes their stack group to be popped before a later equal value is processed.
- **Strictly monotone arrays:** No two equal endpoints exist, so only the $n$ singleton subarrays qualify.
- **Large answer:** With $n=10^5$, the result exceeds a signed 32-bit integer even though every input value fits in one.
