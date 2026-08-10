## General

**Why one best cost per city is not enough**

A cheap route to a city may take too long to leave enough time for the destination, while a more expensive route to that same city may arrive much earlier. Therefore the state must remember both the city and the elapsed travel time. Discarding either dimension can discard a route that later becomes optimal.

The solution creates `f` with `maxTime + 1` rows and one column per city. The meaning of

`f[time][city]`

is the minimum passing-fee cost of a walk that starts at city $0$ and reaches `city` in exactly `time` minutes. Unreachable states hold positive infinity. “Exactly” is important: the table does not copy a value from time $i-1$ to time $i$, because waiting in place is not an operation in the problem.

The base state is `f[0][0] = passingFees[0]`. The source city's fee is included before any road is taken, matching the requirement that both source and destination fees count. Every other state at time zero remains unreachable.

**Relax every road at every possible arrival time**

For elapsed time `i` from one through `maxTime`, the code scans every road `[x, y, t]`. A road can finish at time `i` only if `t <= i`. A walk that reaches `y` at exact time `i - t` can traverse the road to `x` and arrive at time `i`. Its new cost is

`f[i - t][y] + passingFees[x]`.

The symmetric update reaches `y` from `x` and adds `passingFees[y]`. Both updates are necessary because every road is bidirectional. Taking the minimum preserves the cheapest walk for that exact time and endpoint.

Road travel times are strictly positive. Thus `i - t < i`, and every transition reads an earlier time row that has already been completely computed. The order of edges within a row cannot create a dependency cycle. Multiple roads between the same cities are also safe: each road supplies its own travel time, and the minimum operation keeps whichever complete route is cheapest.

Adding a fee to `inf` remains `inf` in Python, so an explicit “source state is reachable” condition is unnecessary. An unreachable predecessor simply cannot improve a destination state.

**Why revisiting cities is handled correctly**

The problem describes a journey rather than requiring a simple path. A route can revisit a city, paying that city's fee each time it is entered. The recurrence naturally represents such walks. A state at an earlier time may itself have come from the same city through a cycle; traversing another edge adds the new arrival city's fee again.

Positive travel times bound the number of transitions in any walk that fits `maxTime`, so cycles cannot cause an infinite dependency. Positive passing fees also mean useless cycling never improves cost, but the algorithm does not need to assume a simple path to remain correct.

**Choose any arrival time within the limit**

The destination may be reached in fewer than `maxTime` minutes; the constraint says “or less,” not “exactly.” After filling the table, the solution computes the minimum of `f[i][n - 1]` over every time from zero through `maxTime`. If all those states are infinite, no feasible journey exists and it returns `-1`. Otherwise it returns the cheapest cost among all allowed arrival times.

**Why the dynamic program is correct**

Use induction on exact elapsed time. At time zero, the only possible walk is staying at city zero, and its cost is precisely the source fee, so the base row is correct.

Assume all states at times below $i$ are correct. Any walk arriving at city $x$ at exact time $i$ has a final road from some neighboring city $y$ taking $t$ minutes. Its prefix reaches $y$ at time $i-t$. By the induction hypothesis, `f[i - t][y]` is no more expensive than that prefix, and adding `passingFees[x]` gives the candidate for the complete walk. Since the algorithm examines every road in both directions, it examines this final step. Conversely, every finite candidate produced by a transition extends a real valid walk by a real road, so it cannot invent an invalid route. Taking the minimum therefore gives exactly the cheapest walk to every city at time $i$.

The induction covers every allowed time. The final minimum consequently gives exactly the cheapest destination walk satisfying the time limit.

## Complexity detail

Let $M$ be `maxTime`, $V$ the number of cities, and $E$ the number of road records.

Allocating the table takes $O(MV)$ time to initialize and $O(MV)$ space. The nested loops inspect all $E$ edges for each of the $M$ positive time values. Each inspection performs constant-time checks and at most two relaxations, so the transition work is $O(ME)$. Scanning the destination column adds $O(M)$. With a connected graph $E\ge V-1$, the stated dominant time bound is $O(ME)$, while the fully explicit bound is $O(MV+ME)$.

The table has $(M+1)V$ entries, so auxiliary space is $O(MV)$. No recursion is used. Each entry stores either infinity or an integer cost.

## Alternatives and edge cases

- **Cost-priority search with time states:** A heap can explore states ordered by fee while retaining time information. It may stop early in practice, but careful dominance handling is required because a city can have several useful cost-time tradeoffs.
- **One best cost per city:** This is incorrect because a cheaper arrival may consume too much time, while a costlier earlier arrival may be the only route that reaches the destination before the deadline.
- **One fastest time per city:** This is also insufficient because the fastest arrival can have a much higher fee than another still-feasible arrival.
- **Rolling time rows:** A simple two-row compression does not work because an edge may read `f[i - t]` for many different values of `t`, not only the immediately previous row.
- **Arrival exactly at `maxTime`:** The last table row is included both in transitions and in the final minimum, so such a journey is valid.
- **Arrival earlier than the limit:** Taking a minimum across all time rows ensures an earlier cheap journey is not lost.
- **Source fee:** It is paid once in the base state. Every later re-entry to city zero through a road adds its fee again, as “each time you pass through a city” requires.
- **Destination fee:** It is added by the final road transition into city `n - 1`.
- **Parallel roads:** Every edge record is processed separately, so different travel times between the same pair remain available.
- **Cycles:** Positive times keep the DP acyclic in its time dimension, and repeated visits correctly incur repeated fees.
- **No feasible journey:** All destination states stay infinite and the method returns `-1` rather than infinity.
