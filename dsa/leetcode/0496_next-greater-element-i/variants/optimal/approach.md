## General

For each queried value, the answer is not merely any larger value to its right. It must be the first larger value encountered when moving rightward through `nums2`. Searching separately for every value in `nums1` repeats the same suffix scans. The solution preprocesses all useful answers in one right-to-left pass with a monotonic stack, then answers each query by dictionary lookup.

Scanning from right to left has a natural advantage: when processing value `x`, every possible answer to its right has already been seen. The stack keeps only right-side values that are still capable of being the next greater element for some value farther left.

**What the stack represents.** From bottom to top, `stk` is strictly decreasing under the distinct-value constraint. Equivalently, values become larger as one moves from the top downward. The top is the nearest surviving candidate in the compressed suffix.

When a new `x` arrives, the loop

`while stk and stk[-1] < x: stk.pop()`

removes every top value smaller than `x`. Such a value cannot answer the query for `x` because it is not greater. It also no longer needs to sit between `x` and farther candidates for future processing: `x` is both larger and farther left, so for any future value that the popped element could exceed, `x` is a closer or stronger candidate in the maintained suffix structure.

After all smaller values are removed, one of two situations remains.

If the stack is empty, there is no greater value to the right of `x`. The source simply stores no dictionary entry for `x`.

If the stack is nonempty, `stk[-1]` is greater than `x`. It is also the first greater value to the right. Any closer suffix values that were not suitable have already been popped while processing the suffix or during the current comparison. A closer value greater than `x` would still survive above farther candidates and would therefore be at the top.

The code records `d[x] = stk[-1]` in this second case, then pushes `x`. Pushing after the lookup is important: an element cannot be its own next greater value.

Consider `nums2 = [1, 3, 4, 2]`. The reverse pass sees `2` first; its stack has no greater candidate. Processing `4` pops `2` and also gets no answer. Processing `3` finds `4` on top and stores `3 -> 4`. Processing `1` finds `3` on top and stores `1 -> 3`. Values `4` and `2` are absent from the map, so queries for them receive `-1`.

**Why a popped value is safe to forget.** Suppose `y < x` is popped while processing `x`, and later a value `z` farther left is considered. If `z < y`, then both `y` and `x` are greater than `z`, but `x` occurs to the left of `y` and is therefore encountered first when moving right from `z`; `y` cannot be the next greater answer. If `z >= y`, then `y` is not greater than `z` at all. In neither case can `y` be needed after `x` appears, proving the monotonic-stack pruning.

The distinctness guarantee simplifies comparisons and dictionary keys. Because no values repeat, a value uniquely identifies its position in `nums2` and its next-greater answer. The source pops with `<` rather than `<=`; equality cannot occur under the contract. If duplicates were allowed, positions rather than values would be needed to distinguish queries and “greater” would still exclude equal values.

**Answer only requested values.** After preprocessing `nums2`, the list comprehension iterates through `nums1` in its original order. `d.get(x, -1)` returns the stored greater value when one exists and `-1` otherwise. The subset guarantee ensures every queried `x` appears in `nums2`, so an absent key means “no greater suffix value,” not “query value missing from the reference array.”

Correctness follows from the stack invariant. Before processing `x`, the stack is a compressed representation of the suffix that preserves its next-greater candidates. Removing smaller values cannot remove a valid answer for `x` or for any later processed value, by the dominance argument above. The remaining top, if present, is the closest greater suffix value, so the dictionary entry is correct. Induction over the reverse scan establishes every stored mapping, and the final lookups return exactly those answers.

## Complexity detail

Let $n$ be `len(nums2)` and $m$ be `len(nums1)`. Every value of `nums2` is pushed once and can be popped at most once. Although one loop iteration may pop many values, the total number of pops across the entire scan is at most $n$. Preprocessing is therefore $O(n)$, and the $m$ expected constant-time dictionary lookups add $O(m)$, for $O(n+m)$ total time.

The stack can hold $O(n)$ values, such as when `nums2` is increasing from left to right and therefore decreasing in the reverse scan. The dictionary can also hold $O(n)$ mappings. Total auxiliary space is $O(n)$. The returned list uses $O(m)$ required output space.

## Alternatives and edge cases

- **Scan rightward for every query:** Locate each `nums1` value and search its suffix. This can cost $O(mn)$ time.
- **Left-to-right monotonic stack:** Keep unresolved values; when a larger value arrives, pop them and map each popped value to the current one. It has the same $O(n+m)$ bounds and is the editorial's common direction.
- **Precompute indices only:** A value-to-index map avoids locating queries but still leaves a linear suffix scan per query, so worst-case time remains quadratic.
- **No greater element:** The reverse scan stores no mapping, and `get(x, -1)` supplies the required sentinel.
- **Strictly increasing `nums2`:** Every value except the last maps to its immediate right neighbor.
- **Strictly decreasing `nums2`:** Every reverse-processed value pops the smaller suffix candidates, and no queried value has a greater element to its right.
- **Distinctness:** Dictionary keys are values because each value occurs once. Duplicate arrays would require index-aware handling.
- **Strict comparison:** Equal values would not qualify as greater. The source's `<` pop is sufficient because equality is impossible here.
- **Query order:** Preprocessing order does not affect output order; the final comprehension follows `nums1` exactly.
