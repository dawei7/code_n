## General

**Represent every piston on one periodic triangular wave**

A piston completes a bottom-to-top-to-bottom cycle in $2h$ seconds, where $h$ is `height`. Assign it a phase in that cycle: an upward piston at position $p$ has phase $p$, while a downward piston has phase $(2h-p)\bmod 2h$. This representation also reflects an outward-pointing endpoint direction immediately into the valid interval.

At time zero, a phase below $h$ has slope $+1$ and is moving upward; a phase at least $h$ has slope $-1$ and is moving downward. Over one period, each piston changes slope exactly twice. Reaching the top changes its contribution from $+1$ per second to $-1$, a slope delta of $-2$. Reaching the bottom changes it from $-1$ to $+1$, a delta of $+2$.

**Sweep changes in the total slope**

For every piston, derive the next top and bottom times within one period and accumulate their slope deltas in an event map. The initial total area is `sum(positions)`, and the initial total slope is the sum of all individual slopes.

Process event times in increasing order. Between consecutive events no piston reverses, so the total area is linear: advance it by `slope * elapsed`, record the resulting endpoint as a maximum candidate, then apply every slope delta at that time. A linear function over an interval reaches its maximum at an endpoint, so no interior second can be better than the values inspected by the sweep.

All pistons share the period $2h$, making the summed area periodic as well. Sweeping one complete period therefore visits a representative of every future state and proves that the recorded maximum is global.

## Complexity detail

Each of the $n$ pistons contributes two events. Building them takes $O(n)$ time, sorting at most $2n$ distinct times takes $O(n\log n)$ time, and the sweep is linear. The event map uses $O(n)$ space.

## Alternatives and edge cases

- **Simulate every second:** One full period is sufficient, but updating all pistons for $2h$ seconds costs $O(nh)$.
- **Store every time value:** A difference array of length $2h$ uses space tied to the height bound; sparse events use space tied only to piston count.
- **Optimize each piston separately:** Individual maximum times may conflict, so summing each piston's maximum does not produce a simultaneously attainable total.
- The initial time must be considered because the total may decrease immediately.
- Multiple pistons can reverse at the same time; their slope deltas must be combined before the next interval.
- A piston initially at `0` next moves upward regardless of an outward `D` marker.
- A piston initially at `height` next moves downward regardless of an outward `U` marker.
- With one piston, the maximum is always `height`.
- The result can be as large as $n \cdot h$, requiring a wide integer type outside Python.
