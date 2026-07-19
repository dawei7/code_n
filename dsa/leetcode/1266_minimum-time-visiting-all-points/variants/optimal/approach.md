## General
**Solve one required leg independently**

For consecutive points, let $\Delta_x$ and $\Delta_y$ be the absolute coordinate differences. One second can reduce both remaining differences by one with a diagonal move. Use diagonals while both differences are positive, then finish the larger unmatched difference with horizontal or vertical moves. This constructs a route of length $\max(\Delta_x,\Delta_y)$.

No route can be shorter: a single move changes either coordinate by at most one, so closing the larger coordinate difference requires at least $\max(\Delta_x,\Delta_y)$ seconds. The constructed route meets this lower bound and is therefore optimal for that leg.

**Add the forced legs**

The visit order partitions the journey into the $n-1$ consecutive legs. Reaching an intermediate point is mandatory before the following leg begins, so choices on one leg cannot reduce the minimum displacement required on another. Sum the Chebyshev distance $\max(\lvert x_i-x_{i-1}\rvert,\lvert y_i-y_{i-1}\rvert)$ over all adjacent pairs.

Passing through a later point causes no special case because it does not satisfy that later visit until all preceding points have been visited.

## Complexity detail
The algorithm examines each of the $n-1$ adjacent pairs once and performs constant work per pair, giving $O(n)$ time. It keeps only the running total and coordinate differences, so its auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Simulate every second:** Move diagonally and then along one axis for each leg; it is correct, but its running time depends on the coordinate distances rather than only on $n$.
- **Euclidean distance:** Taking a square root models geometric length, not the number of allowed one-second moves, and produces the wrong objective.
- **Manhattan distance:** Adding both coordinate differences ignores that one diagonal move reduces both simultaneously and can overcount.
- **Single point:** No movement is required, so the total is `0`.
- **Repeated consecutive points:** Both coordinate differences are zero and that leg contributes `0`.
- **Negative coordinates:** Absolute differences make the same formula valid in every quadrant.
