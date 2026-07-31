
## General

The number of equal-value pairs in a window never decreases when its right boundary moves right. This monotonicity makes a sliding window suitable: once a window is good, every extension ending farther right is also good.

**Updating the pair count**

Maintain the frequency of every value in the current window. If the arriving value already occurs $f$ times, placing one more copy creates exactly $f$ new pairs, one with each existing copy. Add $f$ to the running pair count before increasing its frequency.

**Counting all valid endings**

After extending the right boundary, repeatedly shrink from the left while the window has at least `k` pairs. For the current left boundary, the present right endpoint is the earliest one currently known to make the window good. Every endpoint from `right` through the end of the array remains good, so add `len(nums) - right` to the answer.

When removing the outgoing value, first decrease its frequency. If $f$ copies remain, the removed occurrence participated in exactly $f$ pairs, so subtract $f$ from the pair count. Each successful shrink advances to a new left boundary and counts all of its valid right endpoints exactly once. Boundaries that never form a good window contribute nothing, establishing that the final sum contains every good subarray and no other subarray.

## Complexity detail

Let $n$ be the length of `nums`. The right boundary visits every element once, and the left boundary also advances at most $n$ times, so the total time is $O(n)$. The frequency map stores at most $n$ distinct values and therefore uses $O(n)$ space.

## Alternatives and edge cases

- **Restart a scan at every left boundary:** Incrementally counting pairs for each start is correct but may inspect $O(n^2)$ windows before reaching the threshold or exhausting the suffix.
- **Enumerate pairs explicitly:** Generating equal-index pairs and then attempting to combine their covering ranges creates unnecessary combinatorial work and makes duplicate range counting difficult.
- **No attainable threshold:** If even the full array has fewer than `k` pairs, the window never shrinks and the answer remains zero.
- **Many identical values:** A new copy with frequency $f$ creates $f$, not one, additional pairs; this is essential when three or more copies coexist.
- **Removal order:** Decrease the outgoing value's frequency before subtracting it, because the remaining frequency is exactly the number of pairs destroyed.
- **Large answer:** Up to $n(n+1)/2$ subarrays may qualify, so languages with fixed-width integers need a 64-bit result.
