## General
**The second value is not another unknown**

A pair search treats both values as choices. Once the current value `x` is fixed, however, its partner is forced to be `target - x`. The problem becomes a membership question: has that complement appeared earlier?

Keep a hash table from each previously seen value to its index. At index `i`, compute the complement and look it up. If present, return its stored index with `i`; otherwise store the current value and continue.

**Look up before inserting**

The order of those two operations enforces the “different elements” rule. At the moment of lookup, the table contains only earlier indices, so a match can never reuse position `i` itself.

This also handles duplicates correctly. For `nums = [3, 3]` and `target = 6`, the first `3` finds nothing and is stored. The second `3` then finds the earlier occurrence and returns `[0, 1]`.

For `nums = [2, 7, 11, 15]` and `target = 9`, index zero stores `2`. At index one, the complement of `7` is `2`, which is already mapped to zero, so the answer is `[0, 1]`.

**Why the unique pair must be found**

Let the promised solution use indices $a < b$. By the time the scan reaches `b`, `nums[a]` is in the table. Since `nums[a] = target - nums[b]`, the lookup at `b` succeeds. No false pair can be returned because every successful lookup explicitly verifies the target sum.

## Complexity detail
The scan performs one expected-constant-time lookup and insertion per element, for $O(n)$ expected time. The hash table stores at most `n` values and indices, using $O(n)$ space.

## Alternatives and edge cases
- **Enumerate every pair:** uses constant auxiliary space but takes $O(n^2)$ time.
- **Sort and use two pointers:** takes $O(n \log n)$ and must retain original indices through the sort.
- **Two-pass hash table:** has the same asymptotic bounds, but needs an explicit check against matching an element with itself.
- Negative values, zero, and duplicate values need no special cases; lookup-before-insert handles them uniformly.
