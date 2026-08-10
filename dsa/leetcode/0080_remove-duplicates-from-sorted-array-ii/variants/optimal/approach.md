## General

**Treat the front of the array as the output buffer**

`k` is both the number of values retained so far and the index where the next retained value should be written. At every point, `nums[:k]` is the correct compacted result for the original values already scanned. Positions at or after `k` are irrelevant to the final contract until they are used as unread input or overwritten with later retained values.

The loop variable `x` visits the input values in their original non-decreasing order. When a value is accepted, the source writes it to `nums[k]` and increments `k`. When it is rejected as an excessive duplicate, `k` stays fixed, so a later acceptable value overwrites that unused output slot.

The physical list length never changes. This matches the custom judge: only the returned length and the prefix before it matter; stale values after that prefix are unspecified.

**Why mutating during `for x in nums` is safe here**

Python's list iterator visits indices from left to right. Overwriting a list during iteration can be dangerous if writes alter unread positions. Here, after `p` original positions have been processed, at most `p` values have been retained, so `k <= p`. The next write is therefore at or behind the current scan position, never ahead of it.

If no value has been skipped, `k` equals the current index and the write is a harmless self-assignment. After skips, `k` is smaller and the write changes a position the iterator has already passed. Future original input values remain intact until they are read. The algorithm does not insert, delete, or change the list length, so iteration indices remain stable.

**Keep the first two retained values unconditionally**

When `k < 2`, fewer than two total values have been retained. No value can yet be a forbidden third occurrence, so the condition accepts it. This also avoids reading `nums[k - 2]` with a negative logical output position.

The array is nonempty by contract, but the same logic would naturally return zero for an empty input because the loop would not run.

**Use the value two retained positions back**

Once the retained prefix has at least two values, the candidate `x` is accepted only when `x != nums[k - 2]`.

Because both the original array and the retained prefix are non-decreasing, equal values occur in one consecutive run. If `x == nums[k - 2]`, then `nums[k - 2]`, `nums[k - 1]`, and the candidate are all equal: the middle retained value cannot be smaller or larger inside this sorted interval. Keeping `x` would create at least three copies, so it must be skipped.

If `x != nums[k - 2]`, there cannot already be two retained copies of `x` at the end of the prefix. If there were, the earlier of those two would be exactly at `k - 2` and would equal `x`. Thus accepting the candidate preserves the at-most-two rule.

This comparison replaces an explicit per-value counter. Sorted grouping makes the last two retained output values all the history the decision needs.

**Trace a run longer than two**

For `[1, 1, 1, 2, 2, 3]`, the first two ones are kept, making `k = 2`. The third one equals `nums[0]`, the value two retained slots back, and is skipped. The first two arrives next; it differs from the retained value two positions back, so it is written at index two. The second two is also accepted. Finally 3 differs from the value two retained slots back and is accepted.

The returned `k` is five and the meaningful prefix is `[1, 1, 2, 2, 3]`. Whatever remains in the sixth physical slot is outside the judged prefix.

**A prefix invariant proves exact retention**

After each scanned input value, `nums[:k]` is the original scanned prefix with every value retained in original order up to two occurrences and every later occurrence removed.

The invariant is initially true for an empty scanned prefix. If fewer than two output values exist, accepting the candidate is necessarily legal. Otherwise, equality with the value two output positions back occurs exactly when two copies of this sorted-run value are already retained, so skipping is necessary. Inequality proves fewer than two retained copies and makes acceptance necessary. Writing at `k` preserves order because candidates are scanned in non-decreasing order.

At loop completion, the invariant applies to the entire original array. Therefore `k` is the required length and `nums[:k]` is exactly the required compacted result.

## Complexity detail

Let $n$ be the original array length. Every original element is read once, and each iteration performs a constant number of comparisons and at most one assignment. Time is $O(n)$, matching the manifest. No costly element deletion or shifting occurs.

The method stores only `k`, the loop value `x`, and constant interpreter state. It allocates no result array or frequency map, so auxiliary space is $O(1)$, also matching the manifest. The input list itself is the output buffer.

## Alternatives and edge cases

- **Explicit run counter:** Track the current value's occurrence count and copy only counts one and two. It is equally linear and constant-space but uses more state.
- **Two-pointer plus previous comparisons:** Scan from index two and compare against the output at `write - 2`; this is the indexed form of the selected method.
- **Delete excessive values:** Removing list elements while scanning can shift a linear suffix for every deletion, producing quadratic time in Python.
- **Frequency dictionary:** It works without sorted input but uses extra space and ignores the key simplifying guarantee.
- **One element:** `k < 2` accepts it and returns one.
- **Exactly two equal elements:** Both are accepted.
- **Three or more equal elements:** Only the first two reach the output prefix.
- **All values distinct:** Every comparison differs and `k` becomes the original length.
- **All values equal:** The returned length is two when the input has at least two entries.
- **Negative values:** Only equality and sorted position matter, so sign is irrelevant.
- **Unspecified suffix:** The algorithm intentionally does not erase values after `k`.
- **No resizing:** Stable list length makes mutation during iteration safe together with the never-write-ahead invariant.
- **Sorted-order dependency:** Without grouping equal values, comparison with `k - 2` would not reliably count occurrences.
