## General
**Process known futures from front to back**

Scan indices from right to left. At that point, collision times for every car ahead are already known. Maintain a stack of indices that can still be the first relevant target for a car farther back. The top is the nearest surviving candidate.

**Discard candidates that cannot be reached as themselves**

For current car $i$ and candidate $j$, a collision is impossible while both keep their present speeds if `speed_i <= speed_j`; candidate $j$ can be removed. Otherwise their direct meeting time is

$$
t = \frac{\text{position}_j-\text{position}_i}
         {\text{speed}_i-\text{speed}_j}.
$$

If $j$ never collides, this meeting is valid. If $j$ does collide, the meeting is valid only when $t$ is no later than $j$'s own collision time. When $t$ is later, $j$ will already have joined a slower fleet, so it cannot be car $i$'s first target in its current form; remove it and test the next stack candidate.

**Why the first survivor gives the answer**

Every popped candidate is unusable: it is either not slower or disappears into a fleet before the current car could reach it. The first candidate not satisfying either rejection condition remains present until the computed meeting time, so the current car really collides then. If no candidate survives, the car never collides. Pushing the current index preserves exactly the candidates needed by cars farther back.

## Complexity detail
Each index is pushed once and popped at most once. Although one iteration may pop several candidates, the total number of stack operations is $O(n)$, giving $O(n)$ time. The answer and stack arrays each use $O(n)$ space.

## Alternatives and edge cases
- **Quadratic forward search:** For each car, examine every car ahead and use already-computed collision times to find the first valid target. It follows the same collision condition but takes $O(n^2)$ time.
- **Event priority queue:** Schedule adjacent fleet collisions and update neighboring events after every merge. This can achieve $O(n\log n)$ time but requires careful stale-event handling.
- Equal speeds never produce a future collision unless the cars are already together, which strict initial positions exclude.
- Several cars can collide at exactly the same time; the comparison must allow `t == collision_times[j]`.
- A candidate that collides earlier than the current car could reach it must be skipped even if its current speed is lower.
- The frontmost car always has answer `-1.0`.
