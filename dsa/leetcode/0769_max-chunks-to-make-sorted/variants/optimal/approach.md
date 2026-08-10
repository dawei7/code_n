## General

**Use the permutation guarantee**

The array contains every integer from zero through `n - 1` exactly once. The completely sorted array is therefore known in advance:

`[0, 1, 2, ..., n - 1]`.

This special structure makes a constant-space boundary test possible.

**What must be true at the end of a chunk**

Suppose a chunk ends at index `i` and all earlier chunks already cover the prefix `0..i`. After sorting this prefix’s chunks, the first `i + 1` output positions must contain exactly values `0..i`.

Because the prefix has `i + 1` distinct permutation values, it contains exactly that set if and only if its maximum is `i`:

- Every value is nonnegative.
- All values are distinct.
- If the maximum is `i`, all `i + 1` values must be the complete set `0..i`.

Therefore index `i` is a valid chunk boundary precisely when the maximum value seen through `i` equals `i`.

**Maintain the prefix maximum**

Variable `mx` stores the greatest value in `arr[0:i + 1]`. At each index:

`mx = max(mx, v)`.

If `mx == i`, the prefix contains exactly the values that belong in the first `i + 1` sorted positions. Sorting the chunks completed so far will produce the correct prefix, so the solution increments `ans`.

**Why a larger maximum forbids a cut**

If `mx > i`, some value belonging to a later sorted position is trapped in the current prefix. Since chunks cannot exchange values, cutting here would leave that large value before at least one smaller value located later. The concatenated result could not be sorted.

Under a permutation, `mx < i` cannot happen after processing `i + 1` distinct nonnegative values from `0..n - 1` without forcing a missing or repeated value among the available smaller range.

**Why taking every valid boundary maximizes chunks**

Whenever `mx == i`, the prefix is self-contained. Cutting it cannot restrict how the untouched suffix is partitioned because no prefix value belongs in the suffix and no suffix value belongs in the prefix.

Skipping a valid boundary would merge two regions and reduce the chunk count without creating new opportunities inside the already scanned prefix. Therefore greedily cutting at every valid index is optimal.

**What happens after a boundary**

Once prefix `0..i` is self-contained, every remaining value is greater than `i` because the array is a permutation and all values `0..i` have already appeared. The suffix can therefore be analyzed independently with the same prefix-maximum scan.

The implementation keeps one global `mx` rather than resetting it. This is safe: later indices grow beyond the previous maximum, and equality at a new index still states that the larger global prefix is self-contained. Consecutive equality points define the individual chunks between them.

**Trace `[1,0,2,3,4]`**

- At index zero, prefix maximum is one, so no cut.
- At index one, maximum is still one and equals the index. Prefix values are exactly `{0,1}`, so one chunk ends.
- At indices two, three, and four, each current value equals the new index and the prefix maximum matches immediately. Each position ends another chunk.

The four chunks are `[1,0]`, `[2]`, `[3]`, and `[4]`.

**Trace the descending permutation**

For `[4,3,2,1,0]`, the prefix maximum becomes four immediately and remains four. It cannot equal indices zero through three. Only at final index four does equality hold, producing one chunk.

**The invariant**

After processing index `i`, `mx` is the exact prefix maximum and `ans` counts every self-contained prefix segment ended so far. Each equality proves the current remaining prefix segment contains precisely its required sorted values.

Because every invalid boundary is skipped and every valid boundary is taken, the invariant yields the maximum partition count.

The count includes the final boundary. At index `n - 1`, the prefix is the whole permutation and its maximum is necessarily `n - 1`, so at least one chunk is always recorded.


Any legal boundary after `i` requires the prefix to contain exactly sorted values `0..i`, which under the permutation guarantee is equivalent to `prefix_max == i`. The algorithm finds all and only these positions.

Each such boundary is independent and safe, so selecting all of them creates a legal chunking with the greatest possible number of cuts. Returning their count is correct.

## Complexity detail

Let `n` be the array length. The method visits each element once and performs constant work, so time is `O(n)`.

It stores only `mx`, `ans`, the index, and current value. Auxiliary space is `O(1)`, and the input is not modified.

## Alternatives and edge cases

- **Sort each candidate prefix:** This repeats work and can cost `O(n^2 log n)`.

- **Prefix sum comparison:** For a permutation, comparing prefix sums with `0 + ... + i` also identifies boundaries, but maximum is simpler and avoids larger arithmetic.

- **General stack method:** It handles duplicates and arbitrary values as in problem 768, but the permutation guarantee permits this smaller state.

- **Single element:** Prefix maximum equals index zero, so one chunk is returned.

- **Already sorted permutation:** Equality holds at every index, producing `n` chunks.

- **Descending permutation:** Equality occurs only at the final index.

- **Why uniqueness matters:** With duplicates, maximum equal to `i` would not prove the prefix contains exactly `0..i`.
