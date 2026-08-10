## General

**View imbalance as gaps between neighboring sorted values**

For one subarray, sort its values. Its imbalance is the number of adjacent sorted pairs whose difference is greater than one. The exact solution fixes a left endpoint `i` and expands the right endpoint `j` one position at a time. It maintains:

- `sl`, a `SortedList` containing the values in `nums[i:j + 1]`;
- `cnt`, the imbalance of exactly that current multiset;
- `ans`, the sum of `cnt` over every subarray seen so far.

Re-sorting every expanded subarray would repeat almost all earlier work. The important observation is that inserting one new value changes only the sorted adjacencies immediately around that value.

**What an insertion can change**

Before inserting `x = nums[j]`, the code computes `k = sl.bisect_left(x)`. This is the first position whose existing value is at least `x`. Position `h = k - 1`, when it exists, is the predecessor immediately to the left. Position `k`, when it exists, is the successor immediately to the right.

Before insertion, predecessor and successor are adjacent to each other if both exist. After insertion, that one old adjacency is replaced by up to two new adjacencies:

$$
\text{predecessor} \longrightarrow x
\qquad\text{and}\qquad
x \longrightarrow \text{successor}.
$$

No other sorted pair changes. Therefore the imbalance can be updated in constant many comparisons rather than recalculated across the whole sorted list.

**Apply the local gap accounting**

The code performs three adjustments before adding `x`:

1. If a predecessor exists and `x - sl[h] > 1`, the new left gap contributes one, so increment `cnt`.
2. If a successor exists and `sl[k] - x > 1`, the new right gap contributes one, so increment `cnt`.
3. If both neighbors exist and their old gap `sl[k] - sl[h] > 1`, that old adjacency is being broken, so decrement `cnt`.

This is a remove-old-contribution, add-new-contributions calculation. The code happens to add the new contributions first and subtract the old one afterward, but addition order does not change the result.

For example, suppose `sl` currently contains `[1, 5]`. Its one gap contributes one. Inserting 3 creates gaps `1 -> 3` and `3 -> 5`, both greater than one. The updates add two and subtract the old one, changing `cnt` from one to two. That matches the new sorted list `[1, 3, 5]`.

If instead 2 is inserted, the left gap `1 -> 2` contributes zero, the right gap `2 -> 5` contributes one, and the old `1 -> 5` contribution is removed. The imbalance stays one.

**Duplicates are handled without a special case**

`SortedList` stores duplicates. Because `bisect_left` chooses the first value at least `x`, an existing equal value becomes the successor. Then `sl[k] - x` is zero, so no new right gap is added.

If a predecessor has a large gap to that equal successor, the calculation adds the same large gap from predecessor to the new `x` and subtracts the old predecessor-to-successor gap. The net change is zero. This is correct: inserting a duplicate creates a zero gap beside its equal value but does not change which distinct-value gaps exceed one.

Duplicates still matter as positions because each expanded `[i, j]` is a different subarray. The multiset preserves them while the local arithmetic ensures they do not create false imbalance.

**Enumerating all subarrays**

The outer loop chooses every possible left endpoint `i`. It creates a fresh empty `SortedList` and resets `cnt` to zero. The inner loop then visits every right endpoint `j >= i`. After updating the local gaps and inserting `nums[j]`, `cnt` is exactly the imbalance of `nums[i:j + 1]`, so `ans += cnt` adds that subarray's contribution.

Every non-empty subarray has one unique pair of endpoints. The nested loops visit each such pair exactly once, which ensures no subarray is omitted or counted twice.

**Why the maintained count remains exact**

Initially the empty multiset has no adjacent pairs and `cnt = 0`. Assume `cnt` correctly counts all large adjacent gaps before an insertion. Only the predecessor-successor adjacency can disappear, and only predecessor-to-new and new-to-successor adjacencies can appear. The three conditions subtract and add precisely those contributions. Every unaffected adjacency keeps the same status. Therefore `cnt` remains the exact imbalance after insertion. By induction through the inner loop and enumeration of all left endpoints, `ans` becomes the requested sum.

**The manifest omits the ordered-insertion factor**

The branch manifest reports `O(n^2)` time and summarizes a set-based update. The exact code uses `SortedList` and performs an ordered insertion for every one of the quadratic endpoint pairs. Its gap arithmetic is constant work per subarray, but maintaining sorted order is not constant-time in the standard ordered-multiset model. The documentation therefore states the actual logarithmic factor rather than describing a different set implementation.

## Complexity detail

There are

$$
\frac{n(n+1)}{2} = O(n^2)
$$

subarrays and therefore the same number of inner-loop iterations. Each iteration performs a binary search and inserts into `SortedList`. Treating it as a balanced ordered multiset, those operations cost `O(log n)`, while the neighbor comparisons and answer update cost `O(1)`. The exact implementation is thus `O(n^2 log n)` time under the conventional abstraction, not the manifest's stated `O(n^2)`.

The concrete `sortedcontainers.SortedList` library uses a blocked-list implementation with implementation-specific amortized costs, but ordered insertion is still not a guaranteed constant-time operation. `O(n^2 log n)` is the clear algorithm-level bound intended when reasoning about the code as an ordered multiset.

For one fixed left endpoint, `sl` grows to at most `n` entries, so auxiliary space is `O(n)`. It is discarded and rebuilt for the next left endpoint rather than retaining all subarrays simultaneously. Scalars use `O(1)` additional space, and the input is not modified.

## Alternatives and edge cases

- **Bounded-value presence set:** Since the constraints give `1 <= nums[i] <= n`, a carefully derived contribution method can achieve `O(n^2)` with an array or set and constant-time neighbor-value checks. That would match the manifest but is not the exact implementation.
- **Sort every subarray independently:** This is easy to understand but can cost `O(n^3 log n)` or worse when array copying is included, because nearly identical prefixes are repeatedly sorted.
- **Recompute all gaps after each insertion:** Keeping a sorted list but scanning every adjacent pair would add another linear factor. The predecessor-successor update is what avoids that.
- **One-element subarray:** There are no adjacent sorted positions, so its imbalance is zero.
- **Duplicate insertion:** A zero gap is created, and the add/subtract arithmetic leaves the distinct-value imbalance unchanged.
- **Insert a new minimum:** There is no predecessor, so only the gap to the old minimum can be added.
- **Insert a new maximum:** There is no successor, so only the gap from the old maximum can be added.
- **Insert between consecutive values:** The old gap is at most one, and neither new gap can exceed it in a way that creates an incorrect count.
- **Insert inside one large gap:** The old contribution is removed; zero, one, or two replacement gaps are then counted according to their actual sizes.
- **All values equal:** Every gap is zero, every `cnt` remains zero, and the total is zero.
- **Strict threshold for a gap:** Only a difference greater than one contributes. A difference exactly one is balanced and is never counted.
- **Large accumulated answer:** Python's arbitrary-precision integers safely hold the sum across all subarrays.
