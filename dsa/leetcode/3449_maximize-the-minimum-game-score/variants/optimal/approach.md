## General

**Binary-search the minimum score.** If it is possible to make every `gameScore[i]` at least $T$, then every smaller target is also possible. This monotonicity allows a binary search for the largest feasible $T$.

To reach score $T$ at index $i$, that index must be visited at least

$$
q_i=\left\lceil\frac{T}{\texttt{points}[i]}\right\rceil
$$

times. The source computes this with integer ceiling division.

**Understand visits while walking left to right.** The first move is forced from outside index $-1$ to index $0$. It costs one move and visits index zero once, so `moves = 1` and `incoming = 1`.

When processing a non-final index, `incoming` is how many visits that index has already received from movements arriving from its left neighbor. If it still needs

`bounces = max(0, required - incoming)`

additional visits, the cheapest way before advancing is to bounce right and back. Each round trip costs two moves, visits the right neighbor once, and revisits the current index once.

After enough bounces, one final move to the right permanently advances to the next index. Hence the added moves are `2 * bounces + 1`, and the next index has already been visited `bounces + 1` times: once during each bounce plus once during final advancement.

This greedy processing is optimal for interior positions. A score deficit at the current index must be repaired before leaving it permanently, and every extra visit requires at least a two-move round trip. Those round trips also provide useful visits to the next index, summarized by `incoming`.

If the accumulated moves already exceed `m`, no later action can reduce them, so feasibility returns false early.

**Treat the final two indices together.** The ordinary pattern assumes there is a position to the right that can support bouncing. At indices $n-2$ and $n-1$, movement cannot go beyond the array, so the source calculates two possible endings.

Let `need_current` be the additional visits required at index $n-2$, and let `last_required` be total required visits at index $n-1$.

**Ending pattern 1: advance and finish at the last index.** Perform `need_current` round trips between the two final indices, then one final move from $n-2$ to $n-1$. This costs

`2 * need_current + 1`

and gives the last index `need_current + 1` visits. If it still lacks visits, each extra last-index visit needs a round trip from the last index to $n-2$ and back, costing two. This is `continue_moves`.

**Ending pattern 2: finish at the second-last index.** Perform $q$ complete round trips from $n-2$ to $n-1$ and back. Each supplies one additional visit to both final positions. Choosing

$$
q=\max(\texttt{need\_current},\texttt{last\_required})
$$

satisfies both and costs `2 * q` beyond current `moves`. This is `stop_moves`.

The smaller of these two complete legal endings is the minimum move count for the final pair. Feasibility is whether it is at most `m`.

For `points = [2,4]` and target $4$, required visits are two and one. Starting at index zero gives one visit. One final round trip `0 -> 1 -> 0` supplies the missing visit at zero and one visit at one in two more moves, totaling three, so target four is feasible.

**Why the search bounds are safe.** Zero is always feasible. No index can be visited more than $m$ times, so the minimum score cannot exceed `min(points) * m`. This is a loose but valid inclusive upper bound.

Binary search sets `low` above a feasible middle and `high` below an infeasible middle. When the loop ends, `high` is the greatest feasible target.
The interior sweep uses the minimum necessary bounces at each position; extra bounces there could only increase moves and their useful next-index visits are already fully credited. The final pair examines both possible endpoint parities of the walk. Thus `feasible(T)` is true exactly when $T$ can be achieved within the budget. Monotonic binary search then returns the optimal minimum score.

## Complexity detail

Let $n=\lvert\texttt{points}\rvert$ and $P=\min(\texttt{points})\cdot m$. One feasibility test scans $O(n)$ indices with constant arithmetic. Binary search performs $O(\log(P+1))$ tests, for total time $O(n\log(P+1))$.

The check stores only counters and scalar requirements. Binary search also uses constant state, so auxiliary space is $O(1)$, matching the manifest.

## Alternatives and edge cases

- **Simulate the best walk directly:** The objective couples all indices, and locally maximizing one score can starve another. Binary search converts it to a uniform requirement.
- **Ignore visits gained during bounces:** Every trip to the right also scores the neighbor; `incoming` is essential to avoid overcounting required moves.
- **Use the interior formula at the last index:** It would attempt to step outside the array. The final-pair calculation is necessary.
- **Target zero:** It is immediately feasible without interpreting the forced first move.
- **Move budget too small to reach all indices:** Positive targets become infeasible naturally because the required traversal exceeds `m`.
- **Extra moves:** The rule is at most $m$, so a feasible construction need not spend the remainder.
- **Large arithmetic:** Python integers safely hold target products and move expressions.
- **Two indices:** The main loop immediately executes the specialized final-pair branch.
- **Monotonicity:** A walk meeting $T$ also meets every smaller target, justifying binary search.
- **Finish at either final position:** Comparing both ending patterns avoids an unnecessary final move and can change feasibility.
