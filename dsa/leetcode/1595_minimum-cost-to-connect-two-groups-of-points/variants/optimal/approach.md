## General

**Why a bitmask represents the smaller group**

Every point in both groups must receive at least one connection. Let the first group have $M$ points and the second group have $N$ points, with $N\le M$ and $N\le12$.

The solution processes first-group points one by one. A bitmask of $N$ bits records which second-group points have been connected so far. Bit `k` is one exactly when second-group point `k` already has at least one selected edge.

There are only $2^N$ masks, which is feasible because $N$ is at most 12. Using the smaller group for the mask is what keeps the exponential factor controlled.

**The dynamic-programming state**

`f[i][j]` is the minimum cost after processing the first `i` points of the first group such that:

- every one of those `i` first-group points has at least one connection;
- the set of connected second-group points is exactly mask `j`.

The table has `m + 1` rows and `1 << n` columns. Every entry starts at infinity, meaning the state is not yet known to be reachable. `f[0][0] = 0` is the only starting state: before processing any first-group point, no edge has been selected and no second-group point is covered.

States `f[i][0]` for `i > 0` remain impossible because each processed first-group point must connect somewhere.

**Choose an edge incident to the current first-group point**

For row `i`, the current first-group point is index `i - 1` in `cost`. The loops consider every target mask `j` and every second-group point `k` whose bit is present in `j`.

The condition:

`if (j >> k & 1) == 0: continue`

skips absent bits because the recurrence treats edge `(i - 1, k)` as one selected edge responsible for the current state. If `k` were absent from `j`, that edge could not be part of a solution whose exact covered set is `j`.

`c = cost[i - 1][k]` is the price of that edge. The recurrence considers three different predecessor meanings before adding `c`.

**Predecessor one: another edge from the same current point**

`f[i][j ^ (1 << k)] + c`

removes bit `k` from the mask while staying in row `i`. This means the current first-group point has already been connected to at least one other second-group point in the smaller-mask state. Adding edge to `k` gives the same current point an additional connection and newly covers second-group point `k`.

This same-row transition is what allows one first-group point to connect to several second-group points, as may be necessary when $M$ and $N$ differ or when costs favor sharing.

Because bit `k` is known to be one, XOR clears it. The smaller mask is numerically less than `j`, so it has already been processed by the ascending `j` loop.

**Predecessor two: connect the new point to an already covered target**

`f[i - 1][j] + c`

starts from a state where the first `i - 1` first-group points already cover exactly mask `j`, including `k`. Edge `(i - 1, k)` is the first selected edge for the new current point, satisfying its coverage requirement, but `k` was already connected, so the mask remains `j`.

Without this case, the DP would incorrectly require every new first-group point to introduce a previously uncovered second-group point, which is impossible once all second-group points are already covered and still more first-group points remain.

**Predecessor three: connect the new point to a newly covered target**

`f[i - 1][j ^ (1 << k)] + c`

starts before the current first-group point is processed and before second-group point `k` is covered. Adding the edge simultaneously gives the new point its first connection and turns bit `k` on.

This is the ordinary case where one edge introduces both endpoints’ required coverage relative to the predecessor state.

**Combining the transitions**

The source takes the minimum of the three predecessor costs, adds `c`, and then minimizes `f[i][j]` over every possible chosen `k`:

`x = min(...) + c`

`f[i][j] = min(f[i][j], x)`.

Infinity propagates harmlessly from unreachable predecessor states. Costs are non-negative, and Python’s infinity plus a finite cost remains infinity.

**Why the recurrence is complete**

Take any valid set of edges represented by `f[i][j]` and focus on one selected edge incident to the current first-group point, say edge to `k`. Removing that edge yields exactly one of three situations:

- the current point still has another edge, and `k` loses its only coverage, corresponding to the same-row smaller-mask state;
- the current point loses its last edge, but `k` remains covered by an earlier point, corresponding to `f[i - 1][j]`;
- the current point loses its last edge and `k` also becomes uncovered, corresponding to `f[i - 1][j without k]`.

Thus every valid solution can be decomposed through one recurrence case. Conversely, adding the described edge to any finite predecessor preserves all predecessor coverage requirements and produces exactly state `(i,j)`. Taking minimums therefore yields the optimal cost for every state.

The final state is `f[m][(1 << n) - 1]`, written as `f[m][-1]` because the final list entry is the all-ones mask. Row $M$ guarantees every first-group point is connected, and the all-ones mask guarantees every second-group point is connected.

## Complexity detail

Let $M$ and $N$ be the group sizes, with the second group represented by $N$ mask bits.

There are $(M+1)2^N$ table states. For each of the $M2^N$ processed states, the source loops over all $N$ bit positions and performs constant work. Time complexity is $O(MN2^N)$.

The full table stores $(M+1)2^N$ numeric entries, giving $O(M2^N)$ auxiliary space. The input cost matrix is read-only.

Same-row dependencies prevent a naive two-row compression unless the mask iteration and recurrence are preserved carefully, although a designed rolling implementation can still reduce retained row storage.

## Alternatives and edge cases

- **Choose one edge per first-group point:** This may leave second-group points uncovered. The same-row transition permits additional edges from a current point.
- **Enumerate all edge subsets:** There are $MN$ possible edges, leading to $2^{MN}$ subsets. Mask DP uses the small second-group size to reduce the exponential dimension to $2^N$.
- **Minimum-cost matching:** Ordinary bipartite matching requires one-to-one assignments, but this problem allows and sometimes requires one-to-many connections.
- **Recursive memoization:** A recursion over first-group index and covered mask can work if it also accounts for cheaply covering missing second-group points. The tabulated three-transition formulation enforces both sides directly.
- **One point in each group:** The only full-mask state selects their sole edge, so its cost is returned.
- **One second-group point:** Every first-group point must connect to it. The DP repeatedly uses the already-covered-target transition and sums all required edge costs.
- **Zero-cost edges:** They are handled normally. Several connections can be added at no cost, and infinity still distinguishes unreachable states.
- **More first-group than second-group points:** After all mask bits become one, later first-group points connect through `f[i - 1][j]` without changing the mask.
- **Multiple connections for one first-group point:** `f[i][j without k]` allows accumulating them within the same row.
- **Mask zero after processing points:** It remains infinity because no processed first-group point can be left without a connection.
- **All-ones result mask:** `f[m][-1]` uses Python negative indexing to select the last mask, which is exactly `(1 << n) - 1`.
- **Ascending mask order:** Clearing a set bit produces a smaller integer mask, so every same-row dependency is ready before use.
- **Infinity arithmetic:** Unreachable predecessors never create finite candidates because infinity plus a finite edge cost remains infinity.
- **Group-size assumption:** Masking the second group relies on it being no larger than the first and bounded by 12, matching the contract.
