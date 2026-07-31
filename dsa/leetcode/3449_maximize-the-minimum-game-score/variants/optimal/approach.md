## General

For a proposed minimum score $x$, index $i$ must be visited at least

$$
q_i = \left\lceil \frac{x}{\texttt{points[i]}} \right\rceil
$$

times. Feasibility is monotone: if the board can reach $x$, it can also reach every smaller target. This permits a binary search from zero through $m \cdot \min(\texttt{points})$.

**Why a left-to-right greedy check is forced.** Before leaving an index for good, any missing visits there must be supplied by bouncing across the edge to its right and back. Suppose the walk has already used `moves` moves and the current index has received `incoming` visits from the preceding construction. If it still needs `bounces = max(0, q_i - incoming)` visits, exactly that many right-left bounces are necessary; using more cannot help an earlier position and only spends moves. Those bounces cost two moves each. The final rightward move advances the construction, costs one more move, and gives the next index `bounces + 1` visits. Thus the greedy state needs only `moves` and `incoming` rather than an array of visit counts.

**Handling the final edge.** At the penultimate index there are two possible optimal endings. The walk may make the required bounces, move right once, and then bounce on the final edge until the last index has enough visits. Alternatively, it may finish on the penultimate side after enough complete bounces to satisfy both remaining indices. Computing both move totals and taking their minimum covers the only two possible ending sides. Therefore the check accepts exactly when some legal walk reaches the target within `m` moves.

Binary search keeps the feasible half after each check. When it terminates, `high` is the greatest feasible target and hence the maximum possible minimum game score.

## Complexity detail

Let $n$ be the length of `points`, let $p = \min(\texttt{points})$, and let $U = mp$. Each feasibility check scans the board once in $O(n)$ time and keeps constant state. Binary search performs $O(\log(U+1))$ checks, so the total time is $O(n \log(U+1))$ and the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Move-by-move simulation:** Expanding every required bounce can take $O(m)$ work for a single feasibility check and is too slow when `m` is as large as $10^9$.
- **Dynamic programming over moves:** Tracking board states for each move introduces at least an $m$ factor and is infeasible under the input limits.
- **Fewer moves than cells:** Some index remains unvisited, so the answer is zero; the feasibility check naturally rejects every positive target.
- **No stay operation:** Repeated visits must alternate across an adjacent edge. Treating a move as permission to remain at one index changes the problem and overestimates the answer.
- **Final position:** A legal walk may end at either endpoint of the last processed edge, which is why both final-edge formulas are necessary.
