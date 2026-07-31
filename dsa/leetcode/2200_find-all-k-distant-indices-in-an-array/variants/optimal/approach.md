## General

**Each key occurrence covers an interval**

If `nums[j] == key`, then exactly the indices in `[j - k, j + k]`, clipped to the array bounds, qualify because of that occurrence. Key positions are encountered from left to right, so these intervals also appear in nondecreasing order of both endpoints.

Maintain `next_uncovered`, the smallest index not already appended. For each key position `j`, start at the larger of `next_uncovered` and `j - k`, stop at the smaller of `n - 1` and `j + k`, and append that range. Move `next_uncovered` just beyond the emitted endpoint. Overlapping intervals therefore add only their new suffix, while separated intervals naturally leave gaps.

Every emitted index lies inside a key occurrence's clipped interval, so it satisfies the distance condition. Conversely, every qualifying index belongs to at least one such interval. When that interval is processed, the index is either emitted then or is smaller than `next_uncovered`, which means an earlier interval already emitted it. Thus every qualifying index appears exactly once. Processing intervals and their uncovered suffixes from left to right also makes the result increasing without a final sort.

## Complexity detail

The input scan visits $n$ positions. Each output index is appended at most once, and there can be at most $n$ of them, so total time is $O(n)$.

The returned list can contain all $n$ indices, giving $O(n)$ output space; only $O(1)$ auxiliary state is used beyond it.

## Alternatives and edge cases

- **Test every pair of indices:** For each candidate index, scanning every key position directly is correct but can require $O(n^2)$ time.
- **Boolean coverage array:** Marking each interval in a difference array and taking a prefix sum is linear, but uses another $O(n)$ array.
- **Overlapping intervals:** The next-uncovered boundary prevents duplicate indices where two key neighborhoods overlap.
- **Clipped boundaries:** A key near either array end must not produce negative indices or indices at least $n$.
- **Large distance:** When `k` reaches or exceeds every distance to a key occurrence, the answer contains the whole index range.
