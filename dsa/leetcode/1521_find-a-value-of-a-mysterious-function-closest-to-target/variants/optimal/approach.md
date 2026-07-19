## General
**Keep only distinct ANDs ending at the previous position**

Suppose `previous` contains every distinct AND value of a subarray ending immediately before the current element. A subarray ending at the current position either starts there, producing the element itself, or extends one of those earlier subarrays, producing `candidate & value`. These two sources construct every possible ending-here value.

Deduplicate them in a set. For every resulting value, update the smallest absolute difference from `target`; if the difference reaches zero, return immediately because no better answer exists.

**Why the state remains small**

Extending a subarray with bitwise AND can only clear set bits; it can never restore one. Along the sequence of distinct AND values for progressively earlier starting positions, every strict change removes at least one bit. An integer no larger than $M$ has $O(\log M)$ bits, so at most $O(\log M)$ distinct values survive for one ending position.

Replacing `previous` after each element is safe because future subarrays care only about distinct AND values, not which starting indices produced them. The recurrence covers every interval exactly through its right endpoint, so scanning all endpoints considers the global optimum.

## Complexity detail
For each of $n$ elements, at most $O(\log M)$ distinct prior values are extended and tested. Total time is $O(n\log M)$.

The current and previous sets each hold $O(\log M)$ integers, giving $O(\log M)$ auxiliary space. Under the source bound $M \leq 10^6$, each set has only a small constant number of bit-clearing states.

## Alternatives and edge cases
- **Enumerate every subarray:** carrying a running AND for each left endpoint is correct but takes $O(n^2)$ time.
- **Segment tree plus binary search:** range-AND queries can locate value transitions, but the structure and proof are more involved than endpoint-state compression.
- **Sparse table:** constant-time range AND still leaves too many ranges unless combined with transition jumping.
- **Single element:** the answer is simply that value's distance from the target.
- **Exact target:** return zero as soon as any ending-state AND equals `target`.
- **Target above every array value:** AND cannot increase a value, but all endpoint states must still be considered to find the largest reachable result.
- **Repeated values:** deduplication collapses identical AND states immediately.
- **Rapid collapse to zero:** once zero occurs in an ending-state set, extending that state keeps it zero.
