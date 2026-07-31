## General

After processing a prefix of `b`, let `best[j]` be the maximum score obtainable by selecting exactly $j$ positions and pairing them, in order, with `a[0]` through `a[j - 1]`. The empty choice has value zero, while every positive choice count begins unreachable.

For each value from `b`, either skip it or use it as the next selected position. If $j$ positions had already been chosen, taking the current value creates the candidate `best[j] + a[j] * value` for state $j+1$. Process $j$ from 3 down to 0 so the current value cannot be selected more than once during the same iteration.

Every legal selection appears through these transitions when its four indices are encountered. Conversely, each transition appends the current index to an earlier valid selection, so index order remains strict. Keeping only the maximum for each choice count therefore preserves an optimal prefix for every possible continuation. The final state `best[4]` is exactly the requested maximum score.

## Complexity detail

Let $n$ be the length of `b`. Each value performs four constant-time transitions, giving $O(n)$ time. The five dynamic-programming states have fixed size because `a` always contains four elements, so the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Two-dimensional dynamic programming:** Storing a state for every prefix of `b` and every choice count is correct in $O(n)$ time but uses unnecessary $O(n)$ space.
- **Enumerating index quadruples:** Testing all choices directly takes $O(n^4)$ time and is infeasible at the maximum input length.
- **Negative products:** Reachable states must begin at negative infinity rather than zero; otherwise an invalid partial selection could dominate a valid negative score.
- **Exactly four values in `b`:** All positions must be selected, and the same transitions naturally produce their single possible score.
- **Large magnitude result:** Four products can exceed 32-bit range, so implementations in fixed-width languages need a 64-bit integer type.
