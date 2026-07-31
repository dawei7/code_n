## General

**Inspect the index rather than the value**

Traverse `nums` together with its 0-based indices. For each index `i`, compute the number of `1` digits in its binary representation using the integer population-count operation `i.bit_count()`. Add `nums[i]` to the running total exactly when that count equals `k`.

This direct filter is correct because the requested sum contains one term for every and only every index satisfying that predicate. Each array position is visited once, so no qualifying value can be missed or counted twice. In particular, index `0` has zero set bits and is included precisely when `k = 0`; the bits of `nums[i]` never affect the decision.

## Complexity detail

Let $n$ be the length of `nums`. Under the problem's bounded index range and Python's integer population-count primitive, each bit count is constant-time, so the full scan takes $O(n)$ time. The running sum uses $O(1)$ auxiliary space.

The benchmark uses $n$ as `size`, with legal lengths up to 960. The population-count solution scans once. A correct manual method repeatedly shifts each index to inspect all $O(\log n)$ binary digits, completes every tier, and exhibits $O(n \log n)$ scaling.

## Alternatives and edge cases

- **Clear the lowest set bit:** Repeatedly apply `i &= i - 1` and count iterations. This avoids string conversion but takes time proportional to the number of set bits for each index.
- **Shift and test:** Examine one binary digit at a time with `i & 1`, then right-shift. It is correct but performs $O(\log n)$ work per index.
- **Dynamic bit-count table:** Use `bits[i] = bits[i >> 1] + (i & 1)` for all indices. This takes $O(n)$ time but allocates $O(n)$ extra space for a one-pass sum.
- **Index zero:** Its set-bit count is zero, so `nums[0]` contributes only for `k = 0`.
- **Unattainable `k`:** If no index has that many set bits, return `0`.
- **Values versus indices:** Count bits in `i`, never in `nums[i]`.
