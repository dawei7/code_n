# Guided Example: Minimum Number of Visited Cells in a Grid

## 1. The instance and what has to be counted

We start at the top-left cell of

| row `i` | `grid[i][0]` | `grid[i][1]` | `grid[i][2]` | `grid[i][3]` |
|---|---|---|---|---|
| 0 | 3 | 4 | 2 | 1 |
| 1 | 4 | 2 | 1 | 1 |
| 2 | 2 | 1 | 1 | 0 |
| 3 | 3 | 4 | 1 | 0 |

so $m = n = 4$ and the destination is $(3, 3)$. A cell `(i, j)` allows two kinds of move: rightward to `(i, k)` with $j < k \le \text{grid}[i][j] + j$, or downward to `(k, j)` with $i < k \le \text{grid}[i][j] + i$. The task is the *number of cells visited* on a shortest route, start and destination included, or `-1` when the destination cannot be reached at all. In this instance the answer is $3$: the route $(0,0) \to (3,0) \to (3,3)$ uses two jumps and therefore three visited cells. The same matrix also admits the four-cell route $(0,0) \to (0,3) \to (1,3) \to \dots$ style wanderings, which is exactly the kind of longer candidate the method must price and discard.

The declared limits are $m, n \ge 1$ with $m \cdot n \le 10^{5}$, $0 \le \text{grid}[i][j] < m \cdot n$, and the guarantee $\text{grid}[m-1][n-1] = 0$. That last guarantee is important: the destination may hold $0$, which is a legal dead-end value, because the journey stops there and no outgoing move is ever needed from it.

## 2. Moves form a DAG, so row-major order is a topological order

Write $r(i,j) = \text{grid}[i][j] + j$ for the furthest column reachable from $(i,j)$ in one rightward move, and $d(i,j) = \text{grid}[i][j] + i$ for the furthest row reachable downward. Then

$$
(i, c) \to (i, j) \text{ is legal} \iff c < j \le r(i,c), \qquad (k, j) \to (i, j) \text{ is legal} \iff k < i \le d(k,j).
$$

Two structural facts follow immediately.

- **No cycles.** Every legal move strictly increases either $j$ (rightward) or $i$ (downward), never both decreasing. Hence the move graph is acyclic and $i + j$ strictly increases along any route.
- **Row-major order topologizes it.** Visiting cells with $i$ ascending and, within a row, $j$ ascending, places every possible predecessor of a cell strictly before it. Left neighbours share the row and come earlier in it; upper neighbours live in earlier rows. Nothing that could jump *into* `(i, j)` is still unprocessed.

The rightward-only and downward-only rules also mean a cell's entire predecessor set is "one row to the left, one column above" — no move ever arrives from the right or from below.

| predecessor family | who can jump into `(i, j)` | condition |
|---|---|---|
| same row, to the left | `(i, c)` for $0 \le c < j$ | $j \le \text{grid}[i][c] + c$ |
| same column, above | `(k, j)` for $0 \le k < i$ | $i \le \text{grid}[k][j] + k$ |
| same row, to the right | nobody | rightward moves only, so `(i, c)` with $c > j$ is impossible |
| same column, below | nobody | downward moves only, so `(k, j)` with $k > i$ is impossible |

## 3. The recurrence: price each cell by its last move

Let `dist[i][j]` be the minimum number of visited cells on a route from `(0,0)` to `(i, j)`, and let it be $\infty$ when no route exists. Any route to `(i, j)` with $i + j > 0$ has a final move, and that move comes from a left or upper neighbour, so

$$
\text{dist}[i][j] = 1 + \min\Big(\ \min_{\substack{c < j \\ r(i,c) \ge j}} \text{dist}[i][c],\ \min_{\substack{k < i \\ d(k,j) \ge i}} \text{dist}[k][j]\ \Big),
$$

with the base case $\text{dist}[0][0] = 1$ — the starting cell is itself one visited cell, not zero. If both minima are over empty sets the cell is unreachable.

The recurrence is being read in the right order: because row-major order is a topological order, both minima only reference cells that are already final, so each cell needs exactly one evaluation.

## 4. Executing the sweep over all sixteen cells

The two frontiers are shown for the winning candidate only; a dash means no neighbour in that family can reach the cell.

| cell `(i, j)` | value | best left neighbour `(i, c)` with its `dist` | best upper neighbour `(k, j)` with its `dist` | `dist[i][j]` |
|---|---|---|---|---|
| `(0, 0)` | 3 | — | — | 1 (start) |
| `(0, 1)` | 4 | `(0, 0)`, $r = 3 \ge 1$, dist 1 | — | 2 |
| `(0, 2)` | 2 | `(0, 0)`, $r = 3 \ge 2$, dist 1 | — | 2 |
| `(0, 3)` | 1 | `(0, 0)`, $r = 3 \ge 3$, dist 1 | — | 2 |
| `(1, 0)` | 4 | — | `(0, 0)`, $d = 3 \ge 1$, dist 1 | 2 |
| `(1, 1)` | 2 | `(1, 0)`, $r = 4 \ge 1$, dist 2 | `(0, 1)`, $d = 4 \ge 1$, dist 2 | 3 |
| `(1, 2)` | 1 | `(1, 0)`, $r = 4 \ge 2$, dist 2 | `(0, 2)`, $d = 2 \ge 1$, dist 2 | 3 |
| `(1, 3)` | 1 | `(1, 0)`, $r = 4 \ge 3$, dist 2 | `(0, 3)`, $d = 1 \ge 1$, dist 2 | 3 |
| `(2, 0)` | 2 | — | `(0, 0)`, $d = 3 \ge 2$, dist 1 | 2 |
| `(2, 1)` | 1 | `(2, 0)`, $r = 2 \ge 1$, dist 2 | `(0, 1)`, $d = 4 \ge 2$, dist 2 | 3 |
| `(2, 2)` | 1 | `(2, 0)`, $r = 2 \ge 2$, dist 2 | `(0, 2)`, $d = 2 \ge 2$, dist 2 | 3 |
| `(2, 3)` | 0 | `(2, 2)`, $r = 3 \ge 3$, dist 3 | `(1, 3)`, $d = 2 \ge 2$, dist 3 | 4 |
| `(3, 0)` | 3 | — | `(0, 0)`, $d = 3 \ge 3$, dist 1 | 2 |
| `(3, 1)` | 4 | `(3, 0)`, $r = 3 \ge 1$, dist 2 | `(0, 1)`, $d = 4 \ge 3$, dist 2 | 3 |
| `(3, 2)` | 1 | `(3, 0)`, $r = 3 \ge 2$, dist 2 | `(2, 2)`, $d = 3 \ge 3$, dist 3 | 3 |
| `(3, 3)` | 0 | `(3, 0)`, $r = 3 \ge 3$, dist 2 | — | 3 |

The resulting distance matrix is

| `i` \ `j` | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 0 | 1 | 2 | 2 | 2 |
| 1 | 2 | 3 | 3 | 3 |
| 2 | 2 | 3 | 3 | 4 |
| 3 | 2 | 3 | 3 | **3** |

and the bottom-right entry is the answer, $3$. Two cells in this trace deserve attention. Cell `(3, 2)` is the first place where the row and column families disagree ($2$ versus $3$), showing that the two minima are genuinely independent. Cell `(2, 3)` is priced $4$ even though row $2$ contains a distance-$2$ cell, because that cell cannot reach column $3$ — reachability, not magnitude alone, decides.

## 5. Invariant and correctness

**Invariant.** When the sweep reaches `(i, j)`, every value `dist[a][b]` with `(a, b)` earlier in row-major order already equals the true minimum number of visited cells from `(0,0)` to `(a, b)`.

*Base.* `(0,0)` is first and `dist[0][0] = 1`, the correct count for a route consisting of the start alone.

*Inductive step.* Assume the invariant holds for all earlier cells and consider `(i, j)` with $i + j > 0$. Every legal route to `(i, j)` ends with one move from a predecessor `(i, c)` or `(k, j)`. Both live earlier in row-major order, so their stored values are already optimal, and the recurrence takes the minimum over exactly the predecessors whose frontier covers the cell. Therefore:

- **Soundness (no underestimate).** Every candidate value used is `dist[pred] + 1` for a predecessor that can legally reach `(i, j)`, so it is realised by the concrete route "optimal route to `pred`, then one move". The computed number of visited cells is achievable.
- **Completeness (no overestimate).** Take a genuinely optimal route to `(i, j)`. Its last move starts at some predecessor `p` in one of the two families, and the prefix of that route is a route to `p` with at least `dist[p]` cells. Hence the optimum is at least `dist[p] + 1`, which the minimum over predecessors already attains.

*Failure detection.* A cell is left at $\infty$ exactly when both families are empty of frontier-covering predecessors, which by the same argument means no route exists — so the destination being $\infty$ is precisely the `-1` case, and the guide's sample with a blocked start is handled without a special branch.

## 6. Why the row and column minima can be maintained incrementally

Scanning all $c < j$ and all $k < i$ for every cell is the naive version and is far too slow at $m \cdot n = 10^{5}$ when one dimension is large. The saving comes from a monotonicity observation about frontiers. Inside row $i$, a left neighbour `(i, c)` is usable for column $j$ exactly while $j \le r(i,c)$. Since $j$ only grows during the sweep, **an entry that has expired can never be revived**: once $j > r(i,c)$, that cell is dead for this row forever. The same holds down a column with $i$ versus $d(k,j)$.

So each row and each column can keep its still-usable candidates in a structure that returns the smallest distance quickly, and can permanently discard candidates the moment their frontier falls behind the current position.

| row-2 candidate | frontier $r(2,c) = \text{grid}[2][c] + c$ | usable when $j = 3$? | stored dist |
|---|---|---|---|
| `(2, 0)` | $0 + 2 = 2$ | no, $2 < 3$ | 2 |
| `(2, 1)` | $1 + 1 = 2$ | no, $2 < 3$ | 3 |
| `(2, 2)` | $2 + 1 = 3$ | yes, $3 \ge 3$ | 3 |

Only the last row remains live, so the row minimum at `(2, 3)` is $3$ and not $2$ — the incrementally maintained minimum agrees with the explicit enumeration in the trace above. Column $3$ behaves the same way at $i = 3$: the frontiers of `(0, 3)`, `(1, 3)` and `(2, 3)` are $1$, $2$ and $2$, all below $3$, so no column candidate survives and `(3, 3)` is priced from the row side alone.

The invariant of this bookkeeping is: *after discarding every candidate whose frontier is below the current position, the smallest distance in row $i$'s structure equals the first minimum of the recurrence, and likewise for column $j$'s structure.* Discarding only ever removes entries that the recurrence's reach condition already excluded, and expired entries are removed permanently, so no live candidate is ever lost. Each cell is inserted into its row structure and its column structure once, and removed at most once from each, giving constant amortised structural work per cell beyond the ordered insertion itself.

## 7. Traps this instance exposes

| trap | what it looks like here | correct handling |
|---|---|---|
| Counting moves instead of cells | The optimum is two moves but the required answer is $3$ | Initialise the start at $1$ and add $1$ per move |
| Greedy "always jump as far as possible" | From `(0,0)` the farthest landing is `(0,3)`, whose value $1$ then forces a crawl, while the shorter jump to `(3,0)` reaches the destination immediately | Compare the *prices* of all predecessors, not the length of the jump |
| Taking the smallest distance in the row without checking the frontier | Row $2$ holds a distance-$2$ cell that cannot reach column $3$; using it would price `(2, 3)` as $3$ instead of $4$ | Apply the reach condition $j \le \text{grid}[i][c] + c$ before comparing |
| Reading `0` as "no information" | `(2, 3)` and `(3, 3)` hold $0$, and the guarantee `grid[m-1][n-1] = 0` makes the destination value zero by design | Treat $0$ as "no outgoing moves"; it is fatal only for a cell that must move on |
| Assuming the destination is always priced from a jump | `(2, 3)` is priced by a *move from* `(2, 2)`, whereas `(3, 3)` inherits from `(3, 0)` two columns away | Both families must be consulted for every cell |
| Lower-case/upper-bound confusion in moves | A move from `(i, c)` requires $k > j$ strictly: no zero-length move exists | The predecessor must be strictly left or strictly above |
| Start already at the destination | With $m = n = 1$ and a single `0`, the route visits one cell | Answer $1$, not $0$ and not `-1` |
| Jump ranges past the border | `(0, 1)` has $r = 5$, beyond the last column $3$ | Clamp landings to existing cells; oversized reach is harmless |
| Blocked start | A grid such as `[[0, 1], [1, 0]]` cannot leave `(0, 0)` at all | The destination stays $\infty$ and the answer is `-1` |
| Acyclic but weighted-looking graph | Every move costs exactly the same one unit, and the ordering is a topological one | No priority queue over distances is needed; the sweep itself finalises each cell |

## 8. Complexity

**Time.** The sweep performs one constant-time evaluation per cell after obtaining the two structure minima. Each cell is inserted into one row structure and one column structure and removed from each at most once, and the ordered structures hold at most $n$ entries per row and $m$ per column. The total is therefore

$$
O\!\left(m n \log(m n)\right)
$$

with $m \cdot n \le 10^{5}$, that is roughly $2 \times 10^{5}$ insertions and at most the same number of removals, each costing about $\log_2(10^{5}) \approx 17$ comparisons — on the order of a few million elementary operations. The naive recurrence, which rescans every left and upper neighbour, costs $O\!\left(m n (m + n)\right)$ because a single-cell-wide grid with $n = 10^{5}$ makes each cell scan up to $10^{5}$ predecessors, producing about $5 \times 10^{9}$ candidate checks.

**Auxiliary space.** The distance matrix itself is $O(m n)$ entries, which is the dominant term and is needed because a cell's value is read by later columns of its row and later rows of its column. The ordered structures add at most $O(m n)$ stored entries in total (each cell contributes one row entry and one column entry), so the space bound is $O(m n)$, and it is never worse than the input grid by more than a constant factor.