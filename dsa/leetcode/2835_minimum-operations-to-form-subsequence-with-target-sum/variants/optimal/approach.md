## General

**Represent every power by its bit position**

Splitting never changes the total sum. Consequently, if `sum(nums) < target`, no sequence of operations can succeed. Conversely, because every available value is a power of two and can ultimately be split into ones, a total sum at least as large as `target` guarantees that some construction exists.

For each $i$ from $0$ through $30$, let `counts[i]` record how many available pieces have value $2^i$. Build these counts in one pass through `nums`, then satisfy `target` from its least significant bit upward.

**Resolve low bits before high bits**

When processing bit $i$, all lower target bits have already been satisfied. Any unused lower pieces have also been grouped conceptually: each pair of $2^{i-1}$ pieces contributes one unit of capacity at $2^i$. This grouping costs no operation because a subsequence may select both existing pieces; it is bookkeeping, not a modification of the array.

If bit $i$ of `target` is set and `counts[i]` is positive, consume one $2^i$ piece. This is free and cannot hurt a higher bit: two smaller pieces can replace one larger unit of value, whereas an unused exact piece is already the cheapest way to satisfy the current bit.

**Split the nearest available larger power**

Suppose target bit $i$ is set but no $2^i$ capacity is available. Search upward for the smallest $j>i$ with `counts[j] > 0`. Split one $2^j$ into two $2^{j-1}$ pieces, then split one descendant again, continuing until a $2^i$ piece exists. This costs exactly $j-i$ operations. The unused sibling created at each level remains in `counts`, so later target bits can use it.

This choice is minimal. Every power below $2^j$ is absent after all free lower-bit grouping, while obtaining a $2^i$ piece from a power $2^k$ necessarily requires at least $k-i$ splits. The nearest available $j$ therefore has the smallest possible cost. Processing from low to high also prevents a later decision from invalidating this choice: higher-value demand can use accumulated pairs, but a missing low bit can only be supplied by splitting downward.

After the optional consumption at bit $i$, add `counts[i] // 2` to `counts[i + 1]`. This carries every unused pair into the next bit's capacity. The invariant then holds for bit $i+1$, and the accumulated split count is optimal for every target bit processed so far. Once all $31$ possible target bits are handled, that count is the global minimum.

## Complexity detail

Let $n$ be the length of `nums`. Counting the input takes $O(n)$ time. The remaining work ranges over the fixed $31$ relevant bit positions; upward searches and split chains are bounded by that same constant-size universe. The total time is therefore $O(n)$ under the stated constraints, and the fixed 32-entry count array uses $O(1)$ auxiliary space.

The benchmark uses $n$ as `size`, holds the target fixed, and supplies a scrambled repeating permutation of powers from $2^0$ through $2^{19}$. The optimal implementation only counts them. A correct calibration implementation sorts the complete input before applying the same greedy logic, so it completes every tier but fails with $O(n\log n)$ scaling.

## Alternatives and edge cases

- **Sort before greedy processing:** Sorting the powers and then applying equivalent bit accounting is correct but adds unnecessary $O(n\log n)$ work and may use extra memory.
- **Priority queue of powers:** A heap can repeatedly expose a usable or splittable value, but it complicates preservation of surplus siblings and introduces logarithmic overhead.
- **Explicitly simulate the array:** Appending both halves after every split matches the operation literally, but the array can grow dramatically and obscures the bit-level invariant.
- **Insufficient total sum:** Since a split preserves total value, `sum(nums) < target` must return $-1$ immediately.
- **Already representable target:** Existing pieces and free pair grouping may satisfy every target bit, producing zero operations.
- **One large power:** Reaching a low target bit from $2^j$ can require a complete split chain; the siblings created along that chain may jointly satisfy the other target bits.
- **Maximum target:** The 32-entry array includes index $31$ for carried capacity even though input exponents stop at $30$ and `target` is below $2^{31}$.
