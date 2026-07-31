## General

For a proposed time $t$, worker $i$ can remove the greatest integer $x$ satisfying

$$
workerTimes[i]\frac{x(x+1)}{2}\le t.
$$

After dividing by the worker time, solve the triangular inequality with the quadratic formula. Using `isqrt(1 + 8 * budget)` computes the floor exactly, avoiding floating-point rounding. Sum every worker's capacity and stop once it reaches `mountainHeight`. This predicate is monotone: any time that is sufficient remains sufficient at every later time.

Binary-search the first sufficient time. Zero is a valid lower bound. As an upper bound, let the fastest worker remove the whole mountain alone; its time is `min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2`. At termination, the equal search bounds are sufficient while every smaller time has been ruled out, so that value is the minimum possible simultaneous completion time.

## Complexity detail

Let $w$ be the number of workers and let

$$
U=\min(workerTimes)\frac{mountainHeight(mountainHeight+1)}{2}.
$$

Binary search performs $O(\log U)$ feasibility checks, each examining at most $w$ workers, for $O(w\log U)$ time. The calculation stores only counters and search bounds, using $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Priority queue simulation:** Assigning one height unit at a time costs $O(mountainHeight\log w)$ and is much slower for a tall mountain.
- **Floating-point quadratic inversion:** Square-root rounding near a triangular boundary can overcount a worker's capacity; integer square root is exact.
- **One worker:** The upper bound is the only possible schedule and equals the full triangular cost.
- **Many identical workers:** Work is distributed as evenly as possible, which the capacity sum captures without constructing an assignment.
- **Large result:** The answer can exceed 32-bit range, so fixed-width implementations require 64-bit arithmetic.
