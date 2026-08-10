## General

**Track ranks, not occurrences**

The problem asks for the third distinct maximum. Repeated appearances of the same value do not create additional ranks. For example, in `[2,2,3,1]`, the two copies of `2` together occupy only the second-distinct-maximum position.

The solution makes one pass while storing the three largest distinct values seen so far:

- `m1` is the largest;
- `m2` is the second largest; and
- `m3` is the third largest.

All three begin at negative infinity, written `-inf`, meaning that the corresponding rank has not yet been filled. Negative infinity is smaller than every permitted integer, including $-2^{31}$. This distinction matters: using the smallest legal integer as a sentinel would be ambiguous if that exact value appeared in the input.

**Discard duplicates before ranking**

For each `num`, the condition `num in [m1, m2, m3]` checks whether that distinct value already occupies a tracked rank. If so, the iteration continues without changing anything.

This duplicate check must occur before the comparisons. Suppose `m1` is already `5` and another `5` arrives. If it were processed as a new contender, shifting ranks could incorrectly place `5` in both `m1` and `m2`, turning occurrences into ranks. Skipping it preserves strict ordering among all filled slots.

The temporary list contains exactly three items, so membership testing is constant work. Its size does not depend on `nums`.

**Insert a new distinct value into the correct position**

After duplicates have been removed, there are four possible placements.

If `num > m1`, the new value is the largest seen so far. The old largest becomes second, and the old second becomes third. The simultaneous assignment

`m3, m2, m1 = m2, m1, num`

performs that full shift. Python evaluates all right-hand values before assigning the left-hand variables, so the old values are not overwritten prematurely.

If the first condition is false but `num > m2`, then `num` is smaller than `m1` yet larger than the old second maximum. It belongs in `m2`, and the old `m2` moves to `m3`:

`m3, m2 = m2, num`

If both earlier conditions are false but `num > m3`, it lies below the first two ranks and above the current third, so only `m3` changes.

If none succeeds, `num` is smaller than all three tracked maxima. It cannot affect the requested third maximum and is ignored.

Strict `>` comparisons are correct because equality was already handled by the duplicate check. They also maintain the ordering $m1 > m2 > m3$ among real stored values.

**Trace the rank shifts**

For `nums = [2,2,3,1]`:

1. The first `2` exceeds `m1`, so the state becomes `(m1,m2,m3) = (2,-inf,-inf)`.
2. The second `2` matches `m1` and is skipped.
3. `3` exceeds `m1`; shifting produces `(3,2,-inf)`.
4. `1` is below `m1` and `m2` but above `m3`, producing `(3,2,1)`.

Three distinct ranks exist, so the answer is `m3 = 1`.

For `[1,2]`, the final state is `(2,1,-inf)`. Since the third slot was never filled, the required fallback is the overall maximum `m1 = 2`.

**The maintained invariant**

After every processed prefix, the filled variables contain exactly the three largest distinct values in that prefix, in descending order.

The claim is true before processing any values because all ranks are empty. For a duplicate, the set of distinct prefix values does not change, so skipping preserves the claim. For a new value, the ordered conditions insert it at its proper rank and shift only the lower affected ranks. A value below `m3` cannot enter the top three. Therefore every iteration preserves the invariant.

At the end, if `m3` is real, at least three distinct values were seen and the invariant makes it the third largest. If `m3` is still `-inf`, fewer than three distinct values exist; the invariant still makes `m1` the largest, exactly the required fallback.

**Why storing only three values is sufficient**

Once three distinct maxima have been established, any value below the current `m3` cannot influence the answer unless a future operation removes larger values. No values are ever removed from the input history, so that cannot happen. A later large value may enter the top three, but the shift rules update the tracked ranks and evict the now-fourth-largest value. Thus values below the current boundary can be forgotten permanently.

This is why the algorithm achieves the follow-up's linear time without sorting and uses constant extra storage.

## Complexity detail

Let $n$ be the length of `nums`. The loop visits each element exactly once. Duplicate testing checks three slots, and rank insertion uses a constant number of comparisons and assignments. Total time is $O(n)$.

Only `m1`, `m2`, `m3`, the current value, and a temporary three-element list are used. Their total size is independent of $n$, so auxiliary space is $O(1)$.

The temporary list in `num in [m1, m2, m3]` is newly constructed per iteration in Python, but it always contains exactly three references. This adds constant allocation work per element and does not change either asymptotic bound.

## Alternatives and edge cases

- **Sort in descending order:** After sorting, scan past duplicates until the third distinct value is reached. This is straightforward but costs $O(n\log n)$ time and may mutate the input.
- **Convert the whole input to a set:** Distinctness becomes automatic, after which sorting or repeated maximum selection finds the answer. The set can require $O(n)$ extra space, unlike the three-slot solution.
- **Min-heap of at most three values plus a set:** Keep the three largest distinct values and discard the smallest when a larger contender arrives. Because the heap never exceeds size three, time remains $O(n)$, but coordinating heap membership is more machinery than three variables.
- **Use a legal integer as the empty sentinel:** This is unsafe. The minimum allowed value, $-2^{31}$, can genuinely be the third maximum. `-inf` cannot collide with any input integer.
- **One distinct value:** Only `m1` is filled, so the algorithm returns that maximum.
- **Exactly two distinct values:** `m3` remains `-inf`, and the larger value in `m1` is returned.
- **Exactly three distinct values:** All slots fill, and `m3` is returned even if it equals the smallest legal integer.
- **Many duplicates:** Every duplicate of a tracked maximum is skipped, so frequency never affects rank.
- **Strictly decreasing input:** Values fill `m1`, then `m2`, then `m3`; later smaller values are ignored.
- **Strictly increasing input:** Each new value shifts the previous first and second maxima down one rank, leaving the correct last three distinct values.
- **Negative-only input:** Negative infinity remains smaller than every real value, so comparisons and fallback logic work without a special case.
- **Simultaneous assignment semantics:** Performing the shifts as separate assignments in the wrong order could lose an old maximum. Python's tuple assignment preserves all old right-hand values before updating any slot.
