## General

The future depends on two facts:

- which individuals are still at the base camp;
- the current environmental stage.

The source treats each pair `(mask,stage)` as a shortest-path state and runs Dijkstra’s algorithm because trip durations are positive but unequal.

**State mask**

Bit `i` is one when person `i` remains at the base. The initial mask has all bits set. Goal mask zero means everyone is at the destination.

Given `remaining` after an outward trip, `full_mask ^ remaining` is the set of people currently at the destination and therefore eligible to return with the boat.

**Immediate impossible case**

If boat capacity is one and more than one person exists, every outward trip leaving people behind requires someone to return. The number at the base can never permanently decrease to zero. The source returns `-1` immediately.

For one person, no return is necessary after the only crossing, so capacity one is valid.

**Precomputing group speed**

Outward group time uses its slowest member, the maximum neutral `time` in the subset.

`maximum_time[mask]` is computed from a mask with its lowest bit removed:

`max(maximum_time[mask without bit], time[person])`.

This supplies group maxima in constant time during transition enumeration.

**Dijkstra distances**

`distances[mask][stage]` is the minimum elapsed real time reaching that state. The start is `(full_mask,0)` at zero.

The heap always pops the smallest known elapsed time. A stale heap entry is ignored unless it equals the current distance table value.

All crossing and return times are positive, so once goal mask zero is popped, no later path can have a smaller elapsed time. Returning then is Dijkstra’s standard finalization rule.

**Choosing an outward group**

Every nonempty submask `group` of the current base mask is enumerated. Only groups with at most `k` people fit the boat.

At current stage `s`:

`crossing_time=maximum_time[group]*mul[s]`.

The next stage advances by floor of that duration modulo `m`. The source computes the floor as:

`int(crossing_time+1e-9)`.

The tiny epsilon is intended to protect values mathematically equal to an integer from floating-point representation just below it. It also encodes a numerical assumption: an actual value within `10^{-9}` below an integer would be rounded across the boundary, although the constrained decimal-style multipliers are expected to make this acceptable.

The new base mask is `mask ^ group` because every chosen bit was set and now moves to the destination.

**Finishing without a return**

If `remaining==0`, everyone has crossed. The boat need not return. The arrival state with mask zero is relaxed in the heap.

The source does not return immediately during relaxation because another already-enqueued route might reach goal sooner. It waits until Dijkstra pops the goal.

**Required return when people remain**

If anyone remains at base, the boat is on the destination side and one person there must return.

`returners=full_mask ^ remaining` includes people transported earlier as well as members of the latest group. Each set bit is tried as the sole returner.

Return duration uses the stage after the outward crossing:

`time[person]*mul[next_stage]`.

Its floor advances the stage again. The returning person’s bit is restored:

`next_mask=remaining | returner_bit`.

This transition fully represents one outward crossing followed, when necessary, by one return, leaving the boat ready at the base for the next outward group.

**Why the state is sufficient**

Travel time for a future group depends only on its members and current stage. The identity of people at each side is completely captured by the base mask. Past route order and elapsed integer/fractional composition do not matter beyond total elapsed time and stage.

Therefore, among all ways to reach the same `(mask,stage)`, only the smallest elapsed time can be useful. Dijkstra’s relaxation safely discards larger ones.

**Completeness**

Every legal strategy alternates an outward group with a return whenever people remain, ending on an outward trip. The transition enumeration tries every allowed group and every eligible returner, with exact stage updates.

Thus every legal strategy corresponds to a path in the state graph, and every graph path describes legal boat movements. The shortest graph path is the required minimum time.

## Complexity detail

There are `m2^n` possible states. Across all masks, enumerating every submask produces `3^n` mask-group pairs. For each accepted outward group, up to `n` destination people may be tried as returners.

Including `m` stages and heap operations, a safe bound is:

$$
O(mn3^n\log(m2^n)).
$$

The source stores `maximum_time` in `O(2^n)` and the distance table plus heap states in `O(m2^n)` space. It does **not** materialize all transitions or all `3^n` group pairs.

Therefore the manifest’s `O(mn3^n)` space is a very loose bound and does not describe the actual persistent structures. A faithful state-storage bound is `O(m2^n)`, plus transient scalar subset enumeration.

## Alternatives and edge cases

- **Dynamic programming without a priority queue:** Unequal stage-dependent edge weights prevent ordinary BFS; a repeated-relaxation DP would need another valid ordering.
- **Ordinary BFS:** It minimizes number of trips, not elapsed weighted time.
- **Precompute all feasible groups:** This can reduce repeated bit counts but stores additional exponential data; the source enumerates submasks directly.
- **Capacity covers everyone:** The algorithm may send the full set immediately, while still comparing other routes whose stage effects could theoretically differ.
- **One person:** One outward trip gives the answer.
- **k equals one with several people:** Immediate impossibility is correct.
- **Returner from an earlier group:** Eligible destination set includes all people not remaining at base, so this possibility is covered.
- **Slowest group member:** Group time uses maximum neutral time, not sum or average.
- **Fractional duration:** Elapsed time keeps the full float; only stage advancement uses floor.
- **Goal relaxation:** No return follows the final crossing.
- **Stage cycle:** Both outbound and return advances apply modulo `m`.
- **Repeated state:** Only its least elapsed time remains relevant.
- **Positive multipliers:** All edges have positive duration, satisfying Dijkstra’s requirement.
- **Floating stale check:** Pushed values come directly from assigned distance values, so exact equality filters their own stale copies; robust production code might prefer a greater-than test.
- **n at maximum twelve:** Exponential enumeration is intentional and bounded by the small constraint.
