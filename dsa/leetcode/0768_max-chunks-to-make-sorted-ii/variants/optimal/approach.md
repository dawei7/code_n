## General

**A chunk boundary must respect values across it**

After sorting chunks individually and concatenating them, every value in an earlier chunk must be no greater than every value in a later chunk. If an earlier chunk contains maximum five and a later chunk contains value two, sorting them separately still leaves five before two, so that boundary is impossible.

The exact solution processes values left to right and maintains a monotonic stack. Each stack entry is the maximum value of one tentative chunk.

**Start a new chunk when ordering permits**

If the stack is empty or current value `v` is at least the previous chunk maximum `stk[-1]`, the existing boundary is safe so far. The solution pushes `v` as a new one-element chunk.

Stack maxima therefore remain nondecreasing.

Equal values may start separate chunks because concatenating equal boundary values remains globally sorted.

**Merge when the current value violates a boundary**

If `v < stk[-1]`, the current value cannot remain in a new later chunk. The previous chunk contains a larger value that would still precede `v` after separate sorting.

The algorithm pops that chunk and saves its maximum as `mx`. It then keeps popping while an earlier chunk maximum is also greater than `v`. Every such boundary is invalid for the same reason and must disappear.

Finally it pushes `mx` back as the maximum of the combined chunk.

**Why preserve the first popped maximum**

Before popping, stack maxima are nondecreasing, so the top is at least every earlier popped maximum. Current `v` is smaller. Therefore the first popped value `mx` is the maximum of the entire merged region.

The merged chunk must retain that maximum for future boundary decisions. Pushing `v` instead would forget a large value still present inside the chunk and could allow an invalid later split.

**Why popping stops at `stk[-1] <= v`**

An earlier chunk whose maximum is no greater than `v` can remain separate. Every value in that chunk is at most its maximum, and the merged current chunk contains `v` plus later values. Its eventual minimum may require deeper reasoning, but the stack construction guarantees all intervening violating chunks were absorbed; the remaining boundary is compatible.

Stopping there preserves the greatest possible number of chunks because only boundaries proved invalid are removed.

**Trace `[2,1,3,4,4]`**

Push two as the first chunk maximum. Value one is smaller, so pop two, preserve maximum two, and push it back for merged chunk `[2,1]`.

Values three, four, and four are each at least the current top, so each starts a new chunk. The stack ends with four entries, matching chunks `[2,1]`, `[3]`, `[4]`, and `[4]`.

Sorting each yields the globally sorted array.

**Trace a descending array**

In `[5,4,3,2,1]`, every new value is smaller than all current chunk maxima. Each step collapses the stack back to one entry holding five. Only one chunk can be valid.

**The stack invariant**

After processing a prefix, the stack describes the maximum possible valid chunking of that prefix, and its entries are the chunk maxima in nondecreasing order.

A nonviolating value adds one safe chunk. A violating value forces every popped boundary to merge; retaining `mx` summarizes the merged chunk exactly. Thus the invariant continues.

The algorithm does not need to store chunk start indices or contents because future validity depends only on each chunk’s maximum. The original scan order already determines which consecutive values belong to a merged region.

**Why stack size is maximal**

Whenever the method merges, any valid final chunking must also remove those boundaries because an earlier maximum exceeds a later included value. Whenever it pushes without merging, keeping the boundary is compatible and increases the chunk count.

The algorithm therefore discards only forced boundaries and retains every possible one. At the end, stack length is the maximum number of chunks.

The stack entries are summaries, not the sorted output. Returning their count is sufficient because the problem asks only how many chunks can be formed, not where every boundary lies.

## Complexity detail

Let `n` be the array length. Every value is pushed once. A stack entry can be popped at most once after its creation, so total loop work is `O(n)` amortized.

The stack may hold `n` maxima for an already nondecreasing array, giving `O(n)` auxiliary space.

## Alternatives and edge cases

- **Prefix maximum and suffix minimum arrays:** A boundary after `i` is valid when prefix maximum is no greater than the following suffix minimum. This also gives `O(n)` time and space.

- **Sort and compare prefix multisets:** It is correct but typically costs `O(n log n)`.

- **Use the permutation-only rule `prefix_max == i`:** Duplicates and arbitrary values make that rule invalid for this version.

- **Equal boundary values:** They may remain separate because nondecreasing order permits equality.

- **Descending input:** Every boundary is forced to merge, leaving one chunk.

- **Already sorted input:** Every value pushes a new entry, yielding `n` chunks.

- **Preserve merged maximum:** Forgetting `mx` would make future comparisons unsound.
