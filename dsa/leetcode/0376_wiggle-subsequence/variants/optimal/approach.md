## General
**Track the best sequence ending in each sign**

Maintain `up`, the longest wiggle subsequence seen so far whose last difference is positive, and `down`, the analogous length for a negative last difference. Both begin at one because any single value can start either future state.

When the current value is greater than the previous value, it can follow the best downward-ending sequence, so set `up = down + 1`. When it is smaller, set `down = up + 1`. Equal adjacent values create no valid difference and leave both states unchanged.

**Why adjacent comparisons are sufficient**

Within a rising run, keeping the latest—and therefore highest—value is never worse than keeping an earlier lower endpoint: it gives at least as much room for the next required drop. Symmetrically, within a falling run, the latest lowest value is the best endpoint for a future rise. Updating only when the sign changes, or replacing an endpoint while the sign stays the same, preserves an optimal subsequence without examining every earlier index.

The `up` and `down` recurrence expresses exactly this exchange. A positive step extends the best sequence that previously needed a rise, and a negative step extends the best sequence that needed a fall. At the end, the larger state is an optimal wiggle length.

**Trace a complete wiggle**

For `[1,7,4,9,2,5]`, every adjacent difference alternates sign. The states extend on every step, reaching length six, so the full array is already an optimal wiggle subsequence.

## Complexity detail
The algorithm scans the `n` values once and performs constant work per adjacent pair, giving $O(n)$ time. It stores only two lengths, using $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Quadratic dynamic programming:** compares every earlier endpoint and uses $O(n^2)$ time plus $O(n)$ storage.
- **Explicitly collect local peaks and valleys:** yields the same greedy result but stores a subsequence when only its length is required.
- **Count raw sign changes without handling equals:** can incorrectly treat zero differences as wiggles.
- A strictly increasing or decreasing array has maximum length two when it has at least two values.
- All-equal values produce length one.
- Equal values between two trends may be skipped without changing the optimum.
- Negative numbers require no special handling because only comparisons matter.
