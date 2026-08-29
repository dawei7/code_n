## General

The method does not construct a battery-swapping schedule directly. Instead, it asks a yes-or-no question: can all `n` computers run simultaneously for a proposed integer duration `mid`? Once that test is available, the maximum feasible duration can be found by binary search.

**Cap what one battery can contribute**

A battery with capacity `x` has at most `x` minutes of energy. Over a target interval of `mid` minutes, however, one physical battery can contribute at most `mid` useful minutes: it cannot power two computers at the same time, and no single computer needs it beyond the target duration.

Therefore the useful contribution of that battery is

$$
\min(x,\textit{mid}).
$$

A capacity far above `mid` cannot donate its excess simultaneously while it is supporting one computer. Capping is the key detail that a simple total-capacity check would miss.

All `n` computers together require `n \cdot mid` battery-minutes. The exact feasibility condition is

`sum(min(x, mid) for x in batteries) >= n * mid`.

It is necessary because the left side is the most usable energy the batteries can provide within that horizon.

It is also sufficient under the problem’s swapping rules. Batteries may be moved instantaneously at integer times, there are at least `n` batteries, and their capped energy portions can be scheduled across the computers so that no battery powers more than one computer at once. The cap prevents any single battery from being asked to supply more than the entire interval; the total inequality ensures enough aggregate usable energy for all `n` timelines.

For `n = 2` and `batteries = [3,3,3]`, target four yields capped contributions $3+3+3=9$, which covers the required $8$, so four is feasible. Target five still has only nine useful minutes but requires ten, so it is not.

**Use monotonicity**

If duration `T` is feasible, every smaller duration is feasible by stopping earlier. If `T` is infeasible, every larger duration is also infeasible because required energy grows and no battery’s capped contribution can grow faster than one minute per added minute.

Feasible durations therefore form an integer prefix beginning at zero.

**Maintain an inclusive binary search**

The code begins with `l = 0` and `r = sum(batteries)`. Zero is certainly feasible. The total sum is a loose upper search bound; the true answer cannot exceed total energy divided among `n` computers, but using the larger bound remains correct.

While `l < r`, it computes the upper midpoint:

`mid = (l + r + 1) >> 1`.

The right shift divides the nonnegative sum by two. Adding one chooses the ceiling midpoint, which is essential when searching for the greatest feasible integer. If the lower midpoint were used and `l + 1 == r`, setting `l = mid` could make no progress.

If the capped contribution test succeeds, `mid` belongs to the feasible prefix, so `l = mid`. Otherwise, `mid` and everything above it are impossible, so `r = mid - 1`.

The interval shrinks on every iteration. When the bounds meet, that shared value is feasible and no larger candidate remains possible, so the method returns it.

**Why swaps make energy fungible but not unlimited**

Instantaneous replacement lets small batteries take turns powering a computer and lets partially used batteries move between computers. This makes their usable capped portions behave like a shared pool for the feasibility test. The `min` cap still enforces the physical concurrency restriction: one giant battery cannot alone keep two machines alive during the same minute.

## Complexity detail

Let $m$ be the number of batteries and let $S$ be their total capacity. Computing `sum(batteries)` costs $O(m)$ time. The exact code binary-searches the integer interval from $0$ through $S$, requiring $O(\log(S+1))$ iterations. Each iteration scans all $m$ batteries through the generator expression, so total time is $O(m\log S)$.

The manifest gives the tighter conceptual range $O(m\log(S/n))$, which would follow if the upper bound were initialized to `sum(batteries) // n`. The exact source instead uses `sum(batteries)`, so $O(m\log S)$ precisely describes its written search.

The generator passed to `sum` yields one capped value at a time and does not build a list. Apart from scalar bounds, midpoint, and accumulation state, no input-sized storage is created. Auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Tighter binary-search upper bound:** Set `r = sum(batteries) // n`. This preserves correctness and may save iterations, producing the manifest’s stated logarithmic range.
- **Sorting and water filling:** Sort batteries, dedicate the largest `n` as current computer capacities, and distribute all smaller capacity to raise the bottlenecks. This gives $O(m\log m)$ time and is constructive but more involved.
- **Check total energy without caps:** Testing only `sum(batteries) >= n * mid` is wrong because one oversized battery cannot power multiple computers simultaneously.
- **Assign batteries permanently:** This ignores the ability to swap partially used batteries and can underestimate the answer.
- **One computer:** Every battery can be used sequentially, so the answer is the total capacity. The feasibility sum reaches `mid` for every candidate up to that total.
- **Exactly n batteries:** Each computer ultimately depends on one battery, and the smallest capacity limits the duration. The capped condition reproduces that bottleneck.
- **Many small equal batteries:** Their energy can be rotated among machines; only aggregate capped supply matters.
- **One enormous battery plus weak batteries:** The enormous battery contributes at most `mid` in the test, preventing its unusable simultaneous excess from inflating feasibility.
- **Zero lower bound:** Battery capacities are positive, but starting at zero gives a simple guaranteed-feasible invariant.
- **Upper midpoint:** The `+ 1` prevents an infinite loop when only two adjacent candidate values remain.
- **Integer answer:** Battery changes occur at integer moments and capacities are integer minutes, so searching integer durations matches the contract.
- **Large sums:** The total may exceed 32-bit range. Python integers represent `S` and `n * mid` without overflow.
- **Input preservation:** The method scans `batteries` without sorting or modifying it.
