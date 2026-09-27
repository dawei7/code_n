# Guided Example: Minimum Time to Visit a Cell In a Grid

## 1. The movement model

We stand on cell `(0,0)` of an $m \times n$ grid at time $0$. Cell `(row, col)` carries a release time $\text{grid}[row][col]$, and it may be entered only at a time greater than or equal to that value. Every second exactly one move is made to a cell sharing an edge with the current one, so the time of arrival is always the number of moves made so far, and **standing still is not an option**: the walk must keep moving for its whole duration. The task is the earliest time at which the bottom-right cell can be entered, or `-1` if it can never be entered.

Because the cost of each step is one second and the release times never decrease along a walk, the arrival time at a cell is the natural state, and the answer is a shortest-path question with a scheduling rule attached.

## 2. The parity invariant of a grid walk

Number the rows and columns from `0`. Every move changes exactly one coordinate by one, so it flips the parity of $row + col$. The grid graph is therefore bipartite, and a walk that starts at `(0,0)` with $0 + 0 = 0$ reaches `(row, col)` only after a number of moves whose parity is fixed:

$$\text{arrival time at } (row, col) \equiv row + col \pmod 2 .$$

This is an invariant of every walk, not a property of the best one: two walks to the same cell may have different lengths, but those lengths always differ by an even number, because each detour adds a back-and-forth pair of steps. The practical consequence is that a cell admits only half of all possible times, and a release time with the wrong parity cannot be met exactly — the earliest legal time is then one second later.

Applying this to the worked instance shows where the waiting will be forced. Each entry below lists the release time and the parity of every arrival time at that cell:

| $\text{grid}$ | col 0 | col 1 | col 2 | col 3 |
|---|---|---|---|---|
| row 0 | `0`, even | `1`, odd | `3`, even | `2`, odd |
| row 1 | `5`, odd | `1`, even | `2`, odd | `5`, even |
| row 2 | `4`, even | `3`, odd | `8`, even | `6`, odd |

Three cells in this instance have a release time of the wrong parity: `(0,2)` requires `3` but only even times arrive there, `(1,3)` requires `5` but only even times arrive there, and the destination `(2,3)` requires `6` but only odd times arrive there. Each of them will cost one extra second.

## 3. The arrival rule for one step

Suppose the walk is on a cell at time $t$, and the move considered enters a neighbour $v$ with release time $g = \text{grid}[v]$. Without any waiting the arrival would be $t + 1$, which is already of the parity that $v$ admits. Two cases remain:

| Situation | Earliest legal arrival at $v$ | Reason |
|---|---|---|
| $t + 1 \ge g$ | $t + 1$ | the natural arrival already satisfies the release time |
| $t + 1 < g$ and $g \equiv t+1 \pmod 2$ | $g$ | wait $g - t - 1$ seconds, an even number |
| $t + 1 < g$ and $g \not\equiv t+1 \pmod 2$ | $g + 1$ | a delay of $g - t - 1$ is odd, so one more second is needed |

In one expression, the arrival time is

$$\text{arrive}(t, v) = \begin{cases} t + 1, & t + 1 \ge g \\ g + \big( (g - t - 1) \bmod 2 \big), & t + 1 < g \end{cases}$$

and the delay it adds is always an even number of seconds, which is exactly what a walk can absorb: from a cell already reached, step to a neighbour and immediately back, and two seconds have passed while all release times stay satisfied, because every cell involved was already enterable earlier and times only grow.

## 4. The worked instance

- Input: $\text{grid} = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]$
- Required output: `7`

Dijkstra's algorithm runs on the cells, with the label of a cell being the earliest time at which the walk can be standing there. The source `(0,0)` starts at $0$, and the smallest label in the queue is finalized at each step.

| Pop | Cell finalized | Time $t$ | Neighbours examined, in the order of the arrival rule | Labels written or rejected |
|---|---|---|---|---|
| 1 | `(0,0)` | 0 | `(0,1)` needs 1, `(1,0)` needs 5 | $d(0,1) = 1$, $d(1,0) = 5$ |
| 2 | `(0,1)` | 1 | `(0,0)` stale, `(0,2)` needs 4, `(1,1)` needs 2 | $d(0,2) = 4$, $d(1,1) = 2$ |
| 3 | `(1,1)` | 2 | `(1,0)` needs 5, no gain, `(1,2)` needs 3, `(2,1)` needs 3 | $d(1,2) = 3$, $d(2,1) = 3$ |
| 4 | `(1,2)` | 3 | `(0,2)` needs 4, no gain, `(1,3)` needs 6, `(2,2)` needs 8 | $d(1,3) = 6$, $d(2,2) = 8$ |
| 5 | `(2,1)` | 3 | `(2,0)` needs 4, `(2,2)` needs 8, no gain | $d(2,0) = 4$ |
| 6 | `(0,2)` | 4 | `(0,3)` needs 5 | $d(0,3) = 5$ |
| 7 | `(2,0)` | 4 | `(1,0)` needs 5, no gain | none |
| 8 | `(1,0)` | 5 | `(1,1)`, `(2,0)` both stale | none |
| 9 | `(0,3)` | 5 | `(1,3)` needs 6, no gain | none |
| 10 | `(1,3)` | 6 | `(2,3)` needs 7 | $d(2,3) = 7$ |
| 11 | `(2,3)` | 7 | destination finalized | answer is 7 |

Every label in that table has the parity that section 2 predicts for its cell: $1$ and $5$ odd for the odd cells, $2$, $4$, $6$, $8$ even for the even cells, and $7$ odd for the destination. Three of the arrivals are later than $t+1$ precisely because the release time had the wrong parity: `(0,2)` is reached at $4$ rather than $2$, `(1,3)` at $6$ rather than $4$, and the destination at $7$ rather than $6$.

The same answer is realized by an explicit walk, which is the route the label chain describes: the two extra seconds before entering `(1,3)` are spent oscillating between two already-visited cells.

| Time $t$ | Cell | Release time | Legal because | Remark |
|---|---|---|---|---|
| 0 | `(0,0)` | 0 | start | the origin is always enterable since its release time is 0 |
| 1 | `(0,1)` | 1 | $1 \ge 1$ | first move is available, so the walk can start |
| 2 | `(1,1)` | 1 | $2 \ge 1$ | downward move |
| 3 | `(1,2)` | 2 | $3 \ge 2$ | on the shortest route |
| 4 | `(1,1)` | 1 | $4 \ge 1$ | oscillation, first second |
| 5 | `(1,2)` | 2 | $5 \ge 2$ | oscillation, second second |
| 6 | `(1,3)` | 5 | $6 \ge 5$ | release time satisfied after the two-second delay |
| 7 | `(2,3)` | 6 | $7 \ge 6$ | destination reached |

The walk has length $7$ and its parity is odd, matching $2 + 3 = 5$; the two oscillation steps in the middle add an even amount to the shortest route of length $5$, which is the only kind of delay a walk can produce.

## 5. Why earliest-arrival labels are correct here

Dijkstra's algorithm is justified on this grid by two facts.

**Monotonicity on each parity class.** Fix a cell $u$ and a neighbour $v$. All arrivals at $u$ share the parity of $row(u) + col(u)$, so any two of them differ by an even number of seconds. Restricted to that parity class, $\text{arrive}(t,v)$ never decreases: while the release time $g$ still dominates, the formula returns $g$ or $g+1$ according to a parity that does not change when $t$ grows by two, and once $t+1 \ge g$ the arrival is $t+1$, which grows with $t$. Arriving at $u$ one second later is impossible for a walk, and arriving two seconds later never helps. This is what makes the earliest arrival at $u$ the right prefix for every continuation.

**Optimal substructure.** Consider the earliest arrival at any cell $v$, and let $u$ be the cell occupied one second earlier. The prefix of that walk arriving at $u$ is itself an earliest arrival, because any earlier arrival at $u$ of the correct parity would produce an arrival at $v$ no later than the one claimed. Dijkstra's relaxation therefore discovers the true earliest arrival at every cell by induction on the finalized label order, and the labels only ever decrease to their final values.

Two boundary facts complete the model. The origin has release time $0$ by the constraints, so it never needs waiting and the walk always starts at $t = 0$. And whenever a move is possible at all, delays of any even size are available, so the only obstruction to reaching the destination is the failure of the very first move.

## 6. The unreachable case and material traps

If both neighbours of the origin require more than one second, the walk cannot make its first move: at $t = 1$ neither `(0,1)` nor `(1,0)` may be entered, no other cell is adjacent to the origin, and standing still is forbidden, so the walk is stuck at the origin forever and the answer is `-1`. The constraints guarantee $m \ge 2$ and $n \ge 2$, so both neighbours exist and this test is always well defined. The second official instance is exactly this case: $\text{grid} = [[0,2,4],[3,2,1],[1,0,4]]$ has $\text{grid}[0][1] = 2 > 1$ and $\text{grid}[1][0] = 3 > 1$, and although the destination has release time $4$ and the grid is full of reachable-looking cells, the walk never leaves `(0,0)`.

| Trap | Symptom on this problem | Correct treatment |
|---|---|---|
| Ignoring parity when waiting | taking $\max(t+1, g)$ reaches `(1,3)` at time `5` and the destination at `6`, one second too early and impossible | wait until the smallest time at or beyond $g$ whose parity matches the cell, so the destination is `7` |
| Waiting before the first move | computing an arrival at `(1,0)` at time `5` directly from the origin | the delay must be spent on an edge that has already been traversed; the label `5` is realized by the detour `(0,1)`, `(1,1)`, oscillation, `(1,0)` |
| Treating a cell as consumable | marking visited cells and refusing to re-enter them | revisiting is essential: the walk enters `(1,1)` and `(1,2)` twice to consume time |
| Testing only the destination's release time | assuming the grid is always traversable unless the goal is blocked | the whole route matters: a neighbour with release time above 1 can make the grid unreachable at the start |
| Using a plain breadth-first search | the first time the destination is dequeued is `5`, which is not legal there | distances must be finalized by earliest arrival, and arrivals can jump by more than one second |
| Assuming the answer is the Manhattan distance | here the Manhattan distance to the destination is `5` while the answer is `7` | release times and parity both add to the length of the route |

| Input | Expected output | Reading of the reasoning |
|---|---|---|
| $\text{grid} = [[0,1],[1,2]]$ | `2` | both first moves open at $1$; the destination needs an even time and release time $2$ is even |
| $\text{grid} = [[0,2],[1,3]]$ | `4` | only the downward move is legal at $t = 1$; the destination has even parity and release time $3$ odd, so `4` |
| $\text{grid} = [[0,2],[2,0]]$ | `-1` | both neighbours require at least $2$ seconds, so no first move exists |
| $\text{grid} = [[0,1,100],[1,2,7]]$ | `7` | the release time `7` already has the odd parity of `(1,2)`, so no extra second is charged |
| $\text{grid} = [[0,1,100],[1,2,6]]$ | `7` | the release time `6` has the wrong parity for `(1,2)`, so exactly one extra second is charged |
| $\text{grid} = [[0,1],[100000,100000]]$ | `100000` | the destination has even parity and the maximum release time is even, so it is met exactly |
| $\text{grid} = [[0,2,4],[0,5,5],[5,4,3]]$ | `6` | the route through `(1,0)`, `(0,1)`, `(0,2)`, `(1,2)` respects every release time and reaches `(2,2)` at `6` |
| $\text{grid} = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]$ | `7` | the full trace above |

## 7. Time and auxiliary space

Let $V = m \cdot n$ be the number of cells. Every cell has at most four edges, so the graph has $O(V)$ edges, and the constraints give $V \le 10^5$.

- **Time.** Dijkstra's algorithm with a binary heap finalizes each cell once and performs one relaxation per directed edge, so it takes $O(V \log V)$ time. The constant work per relaxation is a comparison, a parity test, and possibly one heap insertion, and every arrival time stays below roughly $10^5 + 1$, so no expensive arithmetic is involved. The unreachability test runs in constant time before the search.
- **Space.** The distance table holds $V$ labels and the heap holds up to $O(V)$ entries, so the auxiliary space is $O(V) = O(mn)$. No visited matrix is required, because a cell whose label is already finalized can never be improved by a later, larger label; relaxing into it and finding no improvement is enough.
- **Alternative eliminated.** Breadth-first search by time layers is tempting because every move costs exactly one second, but it is wrong here: the time at which a cell becomes enterable depends on the release times and on parity, so the frontier would have to be advanced one second at a time, and the correct answer can be far beyond the layer in which the destination is first dequeued. Weighted shortest path with earliest-arrival labels is the right model, and the parity rule keeps it a single Dijkstra pass rather than a search over pairs of states.
