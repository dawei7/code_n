## General

**Testing a required AND mask.** Suppose every selected final value must contain all bits of a candidate mask `mask`. For one original value `value`, let its cost be the smallest nonnegative increment that reaches some `target` satisfying `target & mask == mask`. Costs for different indices are independent, so a size-`m` subset can support the mask exactly when the sum of the `m` smallest individual costs is at most `k`.

**Finding one value's minimum increment.** Compute `missing = mask & ~value`. If it is zero, the value already contains every required bit and its cost is zero. Otherwise, let `bit` be the highest set bit in `missing`. Every required bit above `bit` is already present in `value`. Preserve the prefix above `bit`, turn `bit` on, and set the lower positions to the smallest pattern that still contains the lower required bits:

```
target = ((value >> (bit + 1)) << (bit + 1))
target |= 1 << bit
target |= mask & ((1 << bit) - 1)
```

The preserved higher prefix and the change from `0` to `1` at `bit` guarantee `target > value`, regardless of the reset lower positions. Any smaller integer either leaves that highest missing bit off or violates a required lower bit, so `target - value` is the minimum cost.

**Building the maximum answer.** The largest possible final value is at most $10^9+10^9<2^{31}$, so consider bits 30 through 0. Tentatively add the current bit to the already accepted higher bits. Compute all per-index costs for this candidate, sort them, and test the sum of the smallest `m`.

If the candidate is feasible, retain its bit. Otherwise discard it. A number with the current bit set is larger than every number with the same accepted higher prefix and that bit clear, regardless of lower bits. Moreover, any final AND containing a later refinement must also contain the candidate's accepted bits. The feasibility tests therefore justify each greedy decision, and the completed mask is the maximum achievable AND.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$ and let $B=31$ be the fixed number of relevant bit positions. Each candidate computes $N$ constant-time costs and sorts them in $O(N\log N)$ time. Across all bits, the bound is $O(BN\log N)=O(N\log N)$. The cost array uses $O(N)$ auxiliary space.

## Alternatives and edge cases

- **Heap-select the cheapest indices:** Keeping only the `m` smallest costs can take $O(N\log m)$ per bit and may save work when $m\ll N$, while retaining the same $O(N\log N)$ worst-case bound.
- **Pair or subset enumeration:** Trying index subsets explicitly is exponential in $N$ and cannot handle the $5\cdot10^4$ limit.
- **Binary search on the numeric answer:** Feasibility is not monotone in ordinary numeric order because different integers require unrelated bit sets; greedy prefix construction uses the correct bitwise ordering.
- **Force selected values to be equal:** Equality is unnecessarily restrictive. Values such as `8` and `10` already share bit `8`, so their AND can contain that bit without making the values identical.
- **Carries reset lower bits:** Incrementing across a power-of-two boundary may clear lower bits. The minimum-target construction intentionally rebuilds every required lower bit after setting the highest missing bit.
- **Subset semantics:** The selected indices need not be adjacent, and operations spent on unselected indices cannot improve the result.
- **Unused budget:** Because the limit is at most `k`, an already optimal subset may use fewer operations or none.
- **Single selected value:** When `m = 1`, the bitwise AND is simply that chosen final value; the same feasibility logic still applies.
