## General
**Express a target cost as independent distances**

A ball starting at index $j$ needs exactly $\lvert i-j\rvert$ adjacent moves to reach target $i$. Balls do not obstruct one another and may share a box, so the minimum cost for target $i$ is the sum of these distances over all positions containing a ball.

**Accumulate contributions from the left**

Sweep indices from left to right. Before processing index `i`, let `balls` be the number of balls strictly to its left and `moves` their total distance to `i`. Add `moves` to `answer[i]`. After including a possible ball at `i`, advancing the target one position right increases every seen ball's distance by one, so update `moves` by `balls`.

**Add the symmetric right contribution**

Reset the two counters and sweep from right to left. They now describe balls strictly to the right and their distance to the current index. Add this second `moves` value to the existing answer, include the current ball, and again increase the next position's cost by the number of seen balls.

**Preserve the initial configuration**

Neither sweep moves or removes a ball; both read the same original bits. For each target, the first pass supplies every term with $j<i$ and the second supplies every term with $j>i$. A ball already at the target contributes zero. Together the passes produce the full distance sum, which is the independent minimum required by the contract.

## Complexity detail
Each sweep visits all $n$ positions once and performs constant work per position, giving $O(n)$ time. The returned answer array uses $O(n)$ space; aside from that required output, the algorithm maintains only four integer counters and loop indices.

## Alternatives and edge cases
- **Sum distances for every target:** Directly checking every box for each answer is correct but takes $O(n^2)$ time.
- **Store full prefix sums:** Prefix counts and index sums can also answer each target in constant time after linear preprocessing, but two running sweeps use less auxiliary state.
- **No balls:** Both counters remain zero, so every answer is zero.
- **One ball:** The answer is the absolute distance from that ball's initial index.
- **All boxes occupied:** Every index contributes one distance term to every target.
- **Several balls in the destination:** The operation rules allow co-location, so no capacity adjustment is needed.
- **Independent targets:** Computing one answer must not mutate the configuration used for another.
- **Endpoint targets:** A single directional sweep supplies all nonzero contributions at an endpoint.
