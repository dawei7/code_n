## General

**Check whether every required bit already exists.** The allowed operation only clears bits. Therefore, transformation is possible exactly when every `1` bit in `k` is also `1` in `n`. The expression `n & k` retains precisely their shared set bits, so `n & k == k` states this condition directly.

**Count the forced changes.** Once the subset condition holds, bits set in both numbers remain untouched. Every bit set only in `n` must be cleared, and clearing exactly those bits reaches `k`. The XOR `n ^ k` marks these differing positions; its population count is both necessary and sufficient, hence minimal.

## Complexity detail

The legal values are at most $10^6$ and therefore occupy at most 20 significant bits. On the fixed-width integer model used by the supported runtimes, masking, XOR, and population count perform bounded work, giving $O(1)$ time and $O(1)$ auxiliary space.

The workload width cannot span the runtime benchmark tiers needed for an honest scaling verdict. The package therefore uses a bounded-domain certificate backed by reduced-domain exhaustion and maximum-width property cases.

## Alternatives and edge cases

- **Inspect bits one at a time:** A 20-iteration loop is correct, but the mask and population-count operations express the same proof directly.
- **Count all differing bits without the subset check:** This incorrectly treats forbidden `0`-to-`1` changes as possible.
- Equal inputs require zero changes.
- If `k` has even one set bit absent from `n`, the answer is `-1`.
- Clearing the highest set bit is allowed and may shorten the displayed binary representation.
- Numeric ordering alone is insufficient: `n > k` does not guarantee that the set bits of `k` form a subset.
