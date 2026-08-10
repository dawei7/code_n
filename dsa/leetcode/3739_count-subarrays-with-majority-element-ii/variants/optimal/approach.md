## General

**Convert majority into a positive transformed sum**

Replace each target occurrence conceptually with `+1` and every other value with `-1`. For a subarray with `f` target occurrences and length `L`, its transformed sum is

$$
f-(L-f)=2f-L.
$$

This is positive exactly when `2f>L`, the strict-majority condition.

Let `P[t]` be the transformed prefix sum before position `t`. The transformed sum of `nums[l:r]` is `P[r+1]-P[l]`, so it is positive exactly when

$$
P[l]<P[r+1].
$$

For every current prefix, the algorithm must count earlier prefix sums that are strictly smaller.

**Shift prefix balances into positive Fenwick indices**

Each transformed step is plus or minus one, so all prefix sums lie from `-n` through `n`. The source uses an offset: `s=n+1` represents mathematical prefix sum zero. This keeps every possible Fenwick index positive.

Before scanning elements, it inserts this empty prefix once. For each value, `s` rises by one for a target match or falls by one otherwise.

`tree.query(s-1)` returns the number of earlier shifted balances strictly below `s`. Every such prefix boundary creates one subarray ending at the current position whose transformed sum is positive. The count is added to `ans`, and then the current prefix is inserted for future endpoints.

Querying before insertion prevents a zero-length subarray from being paired with itself. Querying `s-1` rather than `s` enforces strict positivity; equal prefix sums correspond to transformed sum zero and exactly half target values.

**How the Fenwick tree performs prefix counts**

The tree array stores partial frequency sums. `update(x,1)` adds one to the current prefix-balance coordinate and to Fenwick ancestors by repeatedly adding the lowest set bit `x & -x`.

`query(x)` accumulates frequencies from coordinates one through `x`. It repeatedly removes the lowest set bit, visiting $O(\log n)$ tree nodes.

The tree size `2n+1` covers the shifted range. Starting at `n+1`, after at most `n` negative steps the index is at least one, and after `n` positive steps it is at most `2n+1`.

**Why every valid subarray is counted once**

Every subarray has a unique pair of prefix boundaries `(l,r+1)`. When the scan reaches its right boundary, the left prefix has already been inserted. It contributes exactly when its balance is smaller than the current one, which is equivalent to target majority. It is counted at no other iteration because its right boundary is unique.

Conversely, every frequency returned by the query is an earlier prefix with smaller balance, so the corresponding nonempty interval has positive transformed sum and a strict target majority.

For all-target input, balances increase at every step. Every previous prefix is smaller, so the successive query counts are one, two, through `n` and sum to `n(n+1)/2`. If target is absent, balances decrease and no earlier balance is smaller, so the answer stays zero.

**The exact source differs from the editorial and manifest summary**

The editorial describes an $O(1)$ incremental counting-array update, and the manifest claims $O(n)$ time. The protected Optimal source actually defines and uses a `BinaryIndexedTree`. Each query and update takes $O(\log n)$, so the true source complexity is $O(n\log n)$.

The method is still fully correct for `n=10^5`, but its explanation and bound must follow the code that executes rather than a different intended implementation.

## Complexity detail

There are `n` iterations. Each performs one Fenwick query and one update, both $O(\log n)$, so actual time complexity is $O(n\log n)$. Tree initialization costs $O(n)$.

The tree array has `2n+2` entries, giving $O(n)$ auxiliary space. This matches the manifest's space bound but not its time bound.

The answer can reach `n(n+1)/2` and may exceed 32-bit signed range. Python integers are safe; fixed-width implementations need 64-bit storage.

## Alternatives and edge cases

- **Nested endpoint enumeration:** Incremental target counts give $O(n^2)$ time and work for the smaller version, but not for `n=10^5`.
- **Editorial unit-step counter:** Because balances move only by one, a carefully maintained count of smaller prior balances can achieve $O(n)$ time. That is not the exact source documented here.
- **Merge sort counting:** Counting ordered prefix pairs with smaller left values can also take $O(n\log n)$, but a Fenwick tree naturally respects time order online.
- **Query `s` instead of `s-1`:** This would include equal balances and count subarrays where target is exactly half, violating strict majority.
- **Insert before querying:** It would count the empty current-to-current interval.
- **Target absent:** Every step is negative and the answer is zero.
- **Every element target:** Every nonempty subarray is counted.
- **Single element:** A target match yields one; a non-match yields zero.
- **Large element values:** Only equality to `target` matters, so values do not require coordinate compression.
- **Offset boundaries:** The `n+1` shift guarantees valid positive Fenwick indices across the entire possible balance range.
- **Manifest mismatch:** Runtime claims must include the logarithmic tree operations actually present.
