## General

The selected solution uses a set of distinct values that have not yet been consumed and a dictionary of already summarized consecutive suffixes.

For each original array value `x`, it removes the still-unprocessed consecutive values `x, x + 1, x + 2, ...`. When removal reaches a value `y` that is no longer in the set, `d[y]` can represent a consecutive suffix already processed from `y`. The source joins the newly removed block to that suffix.

**Why duplicates disappear from the set**

`s = set(nums)` keeps one copy of each integer. Consecutive-sequence length counts distinct consecutive values, so duplicate input occurrences must not increase a sequence.

The outer loop still visits the original `nums`, including duplicates, but a value can be removed from `s` only once. Later occurrences find it absent and perform no removal loop.

**What the removal loop discovers**

For current `x`, `y` starts at `x`. While `y in s`, the source removes it and increments `y`.

When the loop stops, all still-unprocessed values in the half-open integer interval `[x, y)` have been consumed. Their count is `y - x`.

The stopping value `y` has one of two meanings:

- `y` is not present in the input, so it is a genuine gap and contributes no suffix; or
- `y` was removed earlier as the start of an already summarized consecutive suffix.

`defaultdict(int)` returns zero for the first case. In the second case, `d[y]` supplies the known suffix length.

**Why the stopping point can safely use `d[y]`**

Suppose `y` was removed earlier and is consecutive with the new block. The earlier processing that removed `y` scanned continuously to the right and stored its combined length under the starting value of that scan.

A future block approaching from smaller values meets that earlier scan at its left boundary. It cannot first meet an unrecorded interior value while the earlier boundary lies farther left, because those lower overlapping values would already have been removed and could not form the new block.

Therefore, when a newly removed block reaches a previously processed consecutive component, the meeting value has the suffix summary needed in `d[y]`.

**The summary formula**

The newly removed block has length `y - x`. The already processed suffix beginning at `y` has length `d[y]`. They are adjacent and disjoint, so:

`d[x] = d[y] + y - x`.

If `y` is a gap, the default suffix length is zero and the formula is simply the new block's length.

If `x` was already removed, the loop does not move `y`; then `y == x` and the assignment becomes `d[x] = d[x] + 0`. For a recorded component start, it preserves its value. For an interior duplicate, it records or preserves zero, but the previously found component maximum remains in `ans`.

**Why processing order does not matter**

Consider component `{1, 2, 3, 4}`.

If one is processed first, it removes the whole component and records length four immediately.

If three is processed first, it removes three and four and records `d[3] = 2`. Later one removes one and two, stops at three, and calculates `d[1] = d[3] + 2 = 4`.

The dictionary lets lower fragments attach to suffixes discovered earlier. Because set removal is permanent, the same values are never rescanned as new work.

**Why `ans` remains correct despite later duplicate iterations**

After each summary assignment, `ans` keeps the maximum length ever recorded.

An outer iteration for an already consumed interior value may assign zero to its own dictionary key, but it does not reduce `ans`. More importantly, future left-side merging needs the earlier component's left boundary summary, not an arbitrary interior key.

Thus transient or unused interior dictionary values cannot erase a previously discovered longest length.

**Tracing the first Reference example**

With `[100, 4, 200, 1, 3, 2]`, processing 100 records length one, processing four records one, and processing 200 records one.

Processing one removes one, but stops at two if two is still present? In this input order, three was processed before two: processing three finds three already? More explicitly, after one it removes one only because two remains and is consecutive, so the loop actually continues through two; before that outer position is reached, set membership ignores original position order. It removes one, two, then stops at three if three was already removed with four, and joins `d[3] = 2`. The resulting `d[1]` is four.

The essential point is that the set contains values globally, not only values seen earlier in the array. Array order does not constrain sequence order.

**Empty and signed inputs**

For an empty array, both the set and outer loop are empty, so initial `ans = 0` is returned correctly.

Negative values work because adding one and hash lookup are independent of sign. Python integers also safely handle incrementing the maximum allowed value by one.

**Exact source dependencies**

The annotation requires `List`, and the code requires `defaultdict`; neither is imported. A standalone module needs `from typing import List` and `from collections import defaultdict`.

## Complexity detail

Let $n$ be input length and $u$ the number of distinct values. Set construction is expected $O(n)$ time. The outer loop has $n$ iterations, but every successful `while` iteration removes one distinct value permanently, so all removal loops together run only $u$ times.

With expected $O(1)$ hash operations, total expected time is $O(n)$. Adversarial hash-collision behavior can weaken this theoretical expectation, as with ordinary Python hash-table analyses.

The set stores $O(u)$ values. The dictionary can store keys for original values and stopping gaps, still $O(n)$ total. Auxiliary space is $O(n)$.

The returned integer uses constant output space, and the original list is not modified.

## Alternatives and edge cases

- **Start-only hash-set scan:** Begin a run only when `x - 1` is absent, then count upward. It is the standard and easier-to-prove expected $O(n)$ solution.
- **Boundary-length interval merging:** Store interval lengths at their endpoints and merge neighboring components as values arrive.
- **Sorting:** Sort distinct or original values and scan, handling duplicates. It takes $O(n\log n)$ time and may mutate the input.
- **Union-find:** Connect present neighboring integers. It works but adds more structure than the interval nature requires.
- **Empty input:** Returns zero.
- **Only duplicates:** The set contains one value, so longest length is one.
- **Negative through positive sequence:** Arithmetic adjacency works across zero.
- **Unsorted order:** The set makes array position irrelevant.
- **Previously processed suffix:** `d[y]` joins it to a newly removed lower block.
- **True gap:** Default zero terminates the sequence.
- **Duplicate outer iteration:** Performs no removals and cannot lower `ans`.
- **Hash complexity:** Linear time is expected, based on expected constant-time set and dictionary access.
- **Missing imports:** `List` and `defaultdict` must be supplied.
- **Input preservation:** Only the copied set is destructively reduced.
