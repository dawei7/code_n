## General
**Summarizing the left condition**

For each day, record how many consecutive non-increasing transitions end there. If `security[day - 1] >= security[day]`, extend the previous count by one; otherwise reset it to zero. A day has the required left window exactly when this count is at least `time`.

**Summarizing the right condition**

Scan from right to left and similarly record how many consecutive non-decreasing transitions begin at each day. If `security[day] <= security[day + 1]`, extend the count from the next day. This count reaches `time` exactly when the required right window is valid.

**Combining both windows**

Only indices from `time` through `n - time - 1` have enough surrounding days. Return those whose left and right counts are both at least `time`.

Each recorded count describes the entire required monotonic chain through its endpoint, not merely one comparison. Therefore a selected index satisfies every inequality on both sides. Conversely, any good day has `time` consecutive valid transitions in each direction, so both counts reach the threshold and the scan includes it.

## Complexity detail
The forward scan, backward scan, and final filtering scan each process $n$ positions once, giving $O(n)$ time. The two run-length arrays use $O(n)$ space, and the output can also contain $O(n)$ indices.

## Alternatives and edge cases
- **Direct window checks:** Test all `time` comparisons on both sides of every candidate. This is straightforward but costs $O(n \cdot \texttt{time})$ in the worst case.
- **Prefix counts of violations:** Mark each increasing transition for the left rule and each decreasing transition for the right rule, then use prefix sums to test whether a window contains a violation. This also runs in $O(n)$ time and space.
- **Constant-extra-space streaming:** With carefully maintained windows, the auxiliary arrays can be reduced, but the two directional summaries are simpler and less error-prone.
- When `time = 0`, every day is good, including both endpoints.
- If $2 \cdot \texttt{time} + 1 > n$, no day has enough positions on both sides.
- Equality satisfies both non-increasing and non-decreasing requirements, so flat plateaus may yield several adjacent good days.
- A globally increasing array can fail every positive-time left window, while a globally decreasing array can fail every positive-time right window.
