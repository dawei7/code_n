## General

**Classify the possible final top**

For a removed value to be restored on the last move, it must come from among the first `k - 1` pile positions: reaching a deeper element already requires more than `k - 1` removals. Conversely, any value in that prefix can be removed and restored on move `k`, with remaining moves arranged using the other accessible pile elements.

There is one other possibility. If the first `k` moves are all removals and `k < n`, the untouched value `nums[k]` becomes the top. Therefore, for an ordinary pile with at least two elements, the answer is the maximum of `nums[k]` when it exists and every value in `nums[:k - 1]`, clipped to the array length.

**Handle the degenerate move patterns**

When `k == 0`, no state changes and `nums[0]` is the answer. A one-element pile behaves differently because moves are forced to alternate between removing and restoring its sole value. It is empty after every odd move and contains its original value after every even move.

The candidate classification is exhaustive: the final top is either an element never removed, which can only be the element exposed by exactly `k` removals, or an element that was removed and later restored, which must have been reachable before the final move. Each listed candidate is attainable, so selecting their maximum is optimal.

## Complexity detail

At most the first $\min(n,k-1)$ values are inspected once, plus the single exposed candidate when it exists. The time complexity is $O(\min(n,k))$.

Only scalar bookkeeping is needed. Excluding the input and return value, auxiliary space is $O(1)$.

## Alternatives and edge cases

- **State-space simulation:** Exploring every legal remove-or-restore sequence is correct for tiny inputs but grows exponentially with the move count.
- **Repeated prefix maxima:** Recomputing the best restorable value for every reachable depth is unnecessary and can take quadratic time.
- **Zero moves:** The original top remains unchanged.
- **One-element pile:** Odd `k` forces an empty final pile, while even `k` returns the only value.
- **Exactly one move:** With at least two elements, the original top must be removed and `nums[1]` becomes the answer.
- **More moves than elements:** For a pile with at least two elements, moves can be spent removing and restoring accessible values; the best reachable restorable value remains valid.
