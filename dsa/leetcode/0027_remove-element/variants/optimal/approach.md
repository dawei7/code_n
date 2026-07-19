## General
**Write only values that survive the filter**

Set `write = 0` and scan every value. When a value differs from `val`, assign it to `nums[write]` and increment `write`. Matching values cause no write. The app returns `nums[:write]`; the official method returns `write` after the identical in-place compaction.

**The prefix is a stable filter of everything already read**

Before each read step, `nums[:write]` contains exactly the non-target values from the processed original prefix, in their original order. Writing the next retained value extends this prefix; skipping a target leaves it unchanged. Since `write` never exceeds the read index, an in-place assignment cannot overwrite an element that has not yet been inspected.

**Trace a case where reading moves ahead of writing**

For `[3, 2, 2, 3]` with target 3, skip the first value, write the two 2s into positions 0 and 1, then skip the final 3. The retained prefix is `[2, 2]` and its official length is 2.

**The write pointer counts retained values**

Each read position is classified exactly once. A target value leaves the write pointer unchanged; a non-target is copied to that boundary and advances it. Thus the prefix before `write` contains all and only retained values seen so far, in their original order.

When the read scan ends, every source value has been classified. No target can appear in the prefix and no non-target can be missing, so `write` is both the correct new length and the boundary of the required retained multiset.

## Complexity detail
Every array element is read once and every retained value is written at most once, so time is $O(n)$. The two-pointer compaction uses $O(1)$ auxiliary space. The app returns the retained prefix for direct testing; the native LeetCode method instead returns its length.

## Alternatives and edge cases
- **Swap targets with the end:** also uses linear time and constant space and can reduce writes when targets are rare, but does not preserve order.
- **Delete matching array elements:** repeated shifts can require $O(n^2)$ time.
- **Build a separate filtered list:** is simple but uses $O(n)$ auxiliary space; repeated concatenation may also become quadratic.
- An empty array and an array containing only `val` both produce retained count zero. If `val` is absent, every element remains in its original position.
- The official judge permits arbitrary retained order, but stable compaction gives deterministic app output with no complexity penalty.
