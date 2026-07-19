## General
**Compare shortest arrival times at the target**

Grid movement without obstacles has Manhattan distance $\left\lvert x1 - x2 \right\rvert + \left\lvert y1 - y2 \right\rvert$. Your fastest arrival time is the distance from `(0, 0)` to `target`. Compute each ghost's Manhattan distance to the same target; if any ghost needs no more moves than you, it can wait there and prevent escape.

**Why an earlier interception adds no new condition**

Suppose a ghost could meet you at some point after `t` moves along one of your shortest routes of total length `D`. By the triangle inequality, that ghost could then reach the target in at most $t + (D - t) = D$ moves. Such a ghost already fails the target-distance test. Therefore, when every ghost is farther from the target than you are, following a shortest route cannot be intercepted in time.

The condition is both necessary and sufficient: a ghost with target distance at most yours wins by heading to the target, while strictly larger target distances rule out both waiting at the destination and interception of a shortest path.

## Complexity detail
The algorithm computes one constant-time Manhattan distance for each of the `g` ghosts, taking $O(g)$ time. It stores only the player's distance and current ghost coordinates, for $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Minimum ghost distance list:** Build all ghost-to-target distances and compare their minimum with the player's distance; this is also $O(g)$ but uses $O(g)$ space.
- **Sort ghost distances:** Sorting before inspecting the nearest ghost is unnecessary and takes $O(g \log g)$ time.
- **Simulate grid movement:** Searching positions turn by turn ignores the direct distance characterization and has an unbounded state space.
- **Tied arrival:** A ghost arriving at the same time blocks escape, so the comparison must be strict.
- **Target at the origin:** Your distance is zero, and any ghost not already there is too late.
- **Negative coordinates:** Manhattan distance handles every quadrant without special cases.
- **One dangerous ghost:** A single ghost at least as close to the target is enough to return false.
