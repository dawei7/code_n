## General

Analyze each allowed sorted layout separately, then take the smaller cost. For one chosen target, map every current position to the position where its current value belongs. Because `nums` is a permutation, this position mapping is also a permutation and decomposes into disjoint cycles.

**Cycles containing the empty space.** Let a nontrivial cycle have length $L$ and contain the current position of value `0`. Moving the correct item into the empty position advances the empty space around that cycle. After $L-1$ such moves, every item in the cycle is placed correctly, so its cost is $L-1$.

**Cycles without the empty space.** A misplaced cycle that does not contain `0` cannot begin rotating until one of its items is moved into the external empty position. After the cycle is corrected, one final move restores the empty position outside it. Together with the internal rotation, a length-$L$ cycle costs $L+1$ moves. A fixed point has length one and costs nothing.

For the empty-first target `[0, 1, ..., n - 1]`, value $v$ belongs at position $v$. For the empty-last target `[1, 2, ..., n - 1, 0]`, value `0` belongs at $n-1$ and every positive value $v$ belongs at $v-1$. Traverse every cycle under each mapping, apply the appropriate cost, and return the smaller total.

Every move changes only which position is empty, exactly matching a swap between value `0` and one item. The cycle costs therefore describe legal operation sequences. Conversely, a cycle without `0` necessarily needs both an entry and an exit move, so no sequence can beat the counted costs.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Each target analysis marks every position once, taking $O(n)$ time; evaluating both targets remains $O(n)$.

The visited array contains $n$ booleans. All other state is constant-sized, so auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Position-map simulation:** Maintaining each value's current position lets a direct legal-move simulation reach either target in $O(n)$ time and $O(n)$ space.
- **Repeated linear search simulation:** Searching the array for the needed item on each of $O(n)$ moves is correct but takes $O(n^2)$ time.
- **Only one target:** Computing the cost for `[0, 1, ..., n - 1]` alone is wrong because the empty-last layout may require fewer moves.
- **Already sorted:** Either target can have total cycle cost zero.
- **Fixed points:** Length-one cycles contribute no moves, even when the fixed point contains `0`.
- **External cycles:** Every nontrivial cycle without the empty position pays two additional moves.
- **Empty-space cycle:** Only the single cycle containing the current position of value `0` receives the $L-1$ cost.
- **Permutation guarantee:** Unique values make the current-to-target position mapping bijective, so its components are cycles rather than general directed graphs.
- **Smallest array:** For $n=2$, both possible permutations are already one of the two valid layouts.
