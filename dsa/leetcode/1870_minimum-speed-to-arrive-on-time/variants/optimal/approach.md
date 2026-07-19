## General
**Evaluate one candidate speed**

For every ride except the last, add `ceil(dist[i] / speed)`, because the next departure cannot occur before that integer-hour boundary. Compute the ceiling with integer arithmetic as `(dist[i] + speed - 1) // speed`. Add the exact quotient `dist[-1] / speed` for the final ride, then compare the sum with `hour`.

**Use monotonic feasibility**

Increasing the speed never increases any rounded ride duration or the exact final duration. Thus infeasible speeds form a prefix of the positive integers and feasible speeds form a suffix. Binary-search the inclusive range from `1` through $U$, retaining the lower half when its midpoint is feasible and discarding it otherwise.

**Handle impossibility**

The first $N-1$ rides each require at least one integer-hour interval, regardless of speed. If `hour <= N - 1`, positive final travel time makes arrival impossible. After binary search, verify the remaining speed as well; this covers any instance for which even $U$ is insufficient.

## Complexity detail
Each feasibility check scans the $N$ distances in $O(N)$ time. Binary search performs $O(\log U)$ checks, so total time is $O(N\log U)$. The search bounds and elapsed-time accumulator require $O(1)$ auxiliary space; the generator used to sum rounded rides does not materialize another array.

## Alternatives and edge cases
- **Linear speed search:** Testing `1, 2, 3, ...` is correct but may require $O(NU)$ time when the minimum speed is large.
- **Binary search over floating-point speed:** The required answer is integral, so integer bounds avoid termination and rounding complications.
- **Round every ride:** Rounding the final ride upward is wrong because there is no subsequent departure to wait for.
- **Deadline at $N-1$:** It is impossible; the final positive-distance ride still needs nonzero time.
- **Single ride:** No departure waiting occurs, so only its exact travel time matters.
- **Exact integer arrival:** A ride ending at an integer hour adds no extra delay.
- **Answer at $U$:** The upper endpoint must remain searchable and can be the minimum valid speed.
