## General
**The second value is not another unknown**

A pair search treats both values as choices. Once the current value `x` is fixed, however, its partner is forced to be `target - x`. Call that complement `y`. The problem becomes a membership question: has `y` appeared earlier?

Keep a hash table `seen` from each previously observed value to its position. At position `i`, compute `y = target - x` and look it up. If `y` is present, return its stored position with `i`; otherwise store `seen[x] = i` and continue.

**Look up before inserting**

The operation order enforces the different-elements rule. At the moment of lookup, `seen` contains only positions strictly smaller than `i`, so a match can never reuse the current element.

This also handles duplicates correctly. For `nums = [3, 3]` and `target = 6`, the first `3` finds nothing and is stored. The second `3` then finds the earlier occurrence and returns `[0, 1]`.

For `nums = [2, 7, 11, 15]` and `target = 9`, position zero stores `2`. At position one, the complement of `7` is `2`, which is already mapped to zero, so the answer is `[0, 1]`.

**Why the unique pair must be found**

Let the promised solution use indices $a < b$. By the time the scan reaches $b$, `nums[a]` is in `seen`. Since `nums[a] = target - nums[b]`, the lookup at $b$ succeeds. No false pair can be returned because every successful lookup explicitly verifies the target sum.

## Complexity detail
Let $n$ be the length of `nums`. The scan performs one expected-constant-time hash-table lookup and at most one insertion per element, for $O(n)$ expected time. The table stores at most $n$ values and positions, using $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate every pair:** uses constant auxiliary space but takes $O(n^2)$ time.
- **Sort and use two pointers:** takes $O(n \log n)$ and must retain original indices through the sort.
- **Two-pass hash table:** has the same asymptotic bounds, but needs an explicit check against matching an element with itself.
- **Negative values, zero, and duplicates:** need no special cases; lookup-before-insert handles them uniformly.
- **No-match fallback:** the contract promises exactly one answer, so `return []` is unreachable for legal inputs and only keeps the app-local function total on malformed data.
