## General

**Robots partition the line into local shooting regions.** Sort each robot together with its distance. A bullet cannot cross a neighboring robot, so a wall strictly between consecutive robots $i-1$ and $i$ can be reached only by robot $i-1$ firing right, robot $i$ firing left, or both. No farther robot can affect that gap. Similarly, walls left of the first robot depend only on its left shot, and walls right of the last robot depend only on its right shot.

A wall sharing a robot coordinate is always destroyed when that robot fires either direction. Count these co-located walls once at the outset and remove them from the wall list used for interval queries. This also makes all remaining gap intervals free of robot-coordinate endpoint ambiguity.

**Precompute each gap's four possible contributions.** Sort the remaining walls. Binary searches count walls in any closed coordinate interval. For a gap from positions $a$ to $b$, the left robot's right shot covers through $\min(a+d_{\mathrm{left}},b)$, and the right robot's left shot begins at $\max(b-d_{\mathrm{right}},a)$. Count each coverage interval separately. When both shots point inward, add their counts and subtract their intersection so an overlapping wall remains unique.

The contribution of a gap depends only on the two endpoint directions:

- left/left: only the right endpoint shoots into the gap;
- left/right: neither endpoint shoots into the gap;
- right/left: both endpoints shoot inward, using their union count;
- right/right: only the left endpoint shoots into the gap.

**Optimize the binary direction chain.** Maintain two values after processing each robot: the best destroyed-wall count when that robot fires left and when it fires right. To add the next robot, try both previous direction states and add the corresponding gap contribution. Initialize the first left state with its exterior-left coverage. After the last gap, add exterior-right coverage only to the final right state.

Every firing assignment corresponds to exactly one path through these states, and every state transition adds precisely the newly completed gap. Conversely, each DP path specifies one direction per robot. Gap interiors, exterior regions, and co-located walls are disjoint after overlap correction, so the maximum DP total plus the fixed co-located count is the global optimum.

## Complexity detail

Let $R$ be the number of robots and $W$ the number of walls. Sorting paired robots takes $O(R\log R)$ time, sorting non-co-located walls takes $O(W\log W)$, and each of the $R-1$ gaps uses a constant number of $O(\log W)$ binary searches. Total time is $O((R+W)\log(R+W))$.

The sorted arrays, robot-position set, filtered walls, and DP data use $O(R+W)$ space. The two-state DP itself uses $O(1)$ space beyond the sorted input structures.

The benchmark defines $S=R$ and supplies $W=2S$ walls. It spans three legal tiers. The accepted solution sorts once and uses binary searches. A calibrated correct alternative performs the same DP but scans the entire wall array for every interval count, producing quadratic growth while preserving all outputs.

## Alternatives and edge cases

- **Enumerate all direction assignments:** Trying all $2^R$ choices is exact but exponential and unusable at the input limit.
- **Scan every wall for every gap:** This keeps the same DP recurrence but costs $O(RW)$ time instead of binary-search interval counts.
- **One robot:** Compare its left and right exterior coverage; it cannot fire in both directions.
- **Wall at a robot coordinate:** Count it once regardless of the robot's chosen direction.
- **Bullet range beyond a neighbor:** The neighboring robot truncates the shot; walls beyond that robot are unreachable by this bullet.
- **Two inward shots overlap:** Count the union, not the sum, to avoid double-counting shared walls.
- **Unsorted robot input:** Sort `(position, distance)` pairs together so ranges stay attached to their robots.
- **Empty gap coverage:** A direction may reach no wall and still be part of the optimal assignment because it affects the adjacent gap on the other side.
