## General
**Represent only the letters still required**

Count each sticker's letters once. A recursive state is the remaining target letters in sorted order, which canonically represents their multiset. Different sticker orders that leave the same deficits then share one memoized state.

**Every transition consumes one useful sticker**

For the current remainder, count its letters and subtract one sticker's available counts. Build the next canonical remainder from positive deficits. Ignore a sticker when it removes no needed letter, because adding it cannot belong to a minimum solution.

**Require the next sticker to cover one chosen letter**

Choose the first letter of the canonical remainder and try only stickers containing it. Every complete solution must eventually use some sticker covering that letter. Sticker order is irrelevant to the final multiset, so that necessary sticker can be moved to the front without changing the number used. This pruning preserves an optimal solution while removing many symmetric branches.

**Why memoized recursion returns the minimum**

The empty remainder needs zero stickers. For a nonempty state, every tried transition uses one sticker and delegates the exact residual requirement to a smaller state. Taking the minimum of `1 + residual_cost` over all useful necessary-letter stickers considers an optimal first choice. Memoization makes every canonical remainder solve once; if all branches are impossible, the state is impossible and ultimately returns `-1`.

## Complexity detail
Let `T` be target length and `S` the number of stickers. A target-position view has at most $2^{T}$ covered subsets; canonical count states are no more numerous. Each state can examine `S` stickers and rebuild up to `T` remaining letters, for $O(S T 2^T)$ time. Storing canonical strings and cached results uses $O(T 2^T)$ space, with at most `T` recursion depth.

## Alternatives and edge cases
- **Bitmask dynamic programming:** track which target positions are covered and apply every sticker; it has the same exponential state bound and naturally distinguishes duplicate target positions.
- **Breadth-first search over canonical remainders:** reaches the empty state with the fewest stickers and can use the same pruning, but stores a frontier in addition to visited states.
- **Unmemoized backtracking:** tries the same sticker choices but revisits identical remainders through many orders, causing exponential repeated work.
- Stickers are reusable without limit; their input multiplicity does not cap usage.
- Extra sticker letters are harmless and simply remain unused.
- If any target letter appears in no sticker, the answer is `-1`.
