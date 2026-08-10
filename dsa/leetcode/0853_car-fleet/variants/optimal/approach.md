## General

**Arrival time reveals whether a rear car catches the fleet ahead**

If a car could drive alone without obstruction, its time to the target would be:

$$
\frac{\texttt{target}-\texttt{position}}{\texttt{speed}}.
$$

Cars cannot pass. Processing them from closest to the target toward farthest lets us compare each rear car's independent arrival time with the arrival time of the fleet directly ahead.

If the rear car would arrive no later, it must catch that fleet by or at the target and join it. If it would arrive later, it cannot catch up before the target and forms a new fleet.

**Sort by starting position**

`idx` contains car indices sorted by `position[i]` in increasing order. Iterating `idx[::-1]` visits cars from greatest position to smallest: frontmost to rearmost.

Positions are unique, so there is one clear order along the road.

The algorithm sorts indices rather than paired records, preserving access to both original `position` and `speed` arrays.

**Meaning of `pre`**

`pre` is the arrival time of the last distinct fleet formed among cars already processed ahead.

It starts at zero. Every car starts before the positive target and has positive speed, so every independent arrival time `t` is positive. The frontmost car therefore satisfies `t > pre` and creates the first fleet.

**When a car creates a new fleet**

For current rear car, compute:

`t = (target - position[i]) / speed[i]`.

If `t > pre`, this car would arrive later than the nearest fleet ahead. It is not fast enough to catch that fleet before the target. It becomes the leader of a new fleet, so:

- increment `ans`;
- set `pre = t`.

As processing moves backward, new fleet arrival times are strictly increasing.

**When a car joins the fleet ahead**

If `t <= pre`, the rear car would reach the target at or before the fleet ahead if unobstructed. Starting behind, it must catch that fleet somewhere before or exactly at the target.

After catching it, passing is forbidden, so it travels with the slower fleet and arrives at time `pre`. It adds no new fleet, and `pre` stays unchanged.

Equality belongs in this case because catching at the target still counts as joining the same fleet.

**Why comparing only one accumulated time is enough**

Cars already processed may form several fleets ahead, but the relevant obstacle for the current car is the nearest fleet in front. `pre` is the arrival time of the rearmost processed fleet, which is the one current car meets first.

If the car can catch that fleet, it joins it and cannot pass onward. If it cannot catch that fleet, it cannot reach any farther fleet either because the nearer fleet lies between them; it becomes a new rearmost fleet.

Thus, one time value summarizes all necessary information.

**Trace the main example**

For target 12, process positions from right to left:

- Position 10 at speed 2 has time 1. It forms a fleet; `pre=1`.
- Position 8 at speed 4 also has time 1. Equality means it catches at the target and joins; fleet count stays one.
- Position 5 at speed 1 has time 7, greater than 1. It forms a new fleet; `pre=7`.
- Position 3 at speed 3 has time 3, no greater than 7. It catches the position-5 fleet and joins.
- Position 0 at speed 1 has time 12, greater than 7. It forms the third fleet.

The answer is three.

**Why independent arrival time remains the right comparison**

A faster rear car may slow after joining, but this cannot create an extra fleet; it has already merged. A slower rear car with larger time never reaches the fleet ahead before the target.

The fleet ahead's effective arrival time is the maximum independent time among cars merged into it, because the slowest constraint determines its target arrival. The algorithm retains exactly that time as `pre`.

**Why the greedy count is correct**

Processing front to back establishes fleets in unavoidable road order. For each current car, the comparison with the immediate fleet ahead determines uniquely whether they meet by the target.

No decision is being optimized or guessed; the physical no-passing rule forces the outcome. Counting strict increases in arrival time while moving backward therefore counts exactly the final fleets.

## Complexity detail

Let `n` be the number of cars. Sorting indices by position takes `O(n\log n)` time. The reverse scan calculates one arrival time and performs constant work per car, taking `O(n)`. Total time is `O(n\log n)`.

The index list contains `n` integers, so auxiliary space is `O(n)`. Sorting may also use linear implementation workspace, remaining within the same bound.

Arrival times use floating-point division. Only relative comparisons of ratios are needed; the bounded inputs make this conventional implementation suitable. Cross multiplication could avoid floating-point values in another language.

## Alternatives and edge cases

- **Sort paired position/time records:** This is equivalent and may be more direct. The exact source sorts original indices.

- **Simulate positions over time:** Continuous catch-up events make simulation unnecessarily complex and potentially slow.

- **Monotonic stack:** Arrival times in position order can be pushed and merged with stack logic. The scalar `pre` suffices when scanning from front to back.

- **One car:** Its positive time exceeds zero, so one fleet is counted.

- **Equal arrival times:** Cars meet at the target and count as one fleet; strict `t > pre` is essential.

- **Rear car arrives sooner alone:** It catches and joins the fleet ahead.

- **Rear car arrives later alone:** It cannot catch and starts a new fleet.

- **Several cars join one fleet:** `pre` remains the fleet's limiting arrival time through all of them.

- **Unique positions:** No two cars require a same-position starting rule.

- **Target greater than every position:** Every distance and time is positive.

- **No passing:** This rule is what turns catch-up into permanent fleet membership.

- **Input immutability:** Only a sorted index list is created; positions and speeds are not reordered.
