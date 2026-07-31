## General

View each segment as a constant, nonnegative coin density on its integer coordinates. While a length-$k$ window shifts through a region where neither boundary crosses a segment endpoint, the amount entering and leaving per step stays constant. The window total is therefore linear there, so a maximum occurs at a boundary event. It is sufficient to consider windows whose left edge equals some $l_i$ or whose right edge equals some $r_i$.

First evaluate every left-aligned candidate. Sort the segments by `left`, store their starts, and build a prefix sum in which each complete segment contributes

$$
(r_i-l_i+1)c_i.
$$

For the window starting at $l_i$, its right endpoint is `l_i + k - 1`. Binary search finds the last segment whose left endpoint does not exceed that boundary. Every segment from $i$ through the one before `last` lies completely inside the window and is obtained from the prefix sums. The last segment contributes only the overlap from its left endpoint through the smaller of its right endpoint and the window boundary.

The remaining candidates are right-aligned. Reflect every coordinate through zero, transforming `[left, right, value]` into `[-right, -left, value]`. A window ending at an original right endpoint becomes a window starting at a reflected left endpoint, so the same helper evaluates the entire second candidate family. Taking the larger helper result covers every possible optimum.

For each candidate, the prefix difference counts exactly the fully covered segments and the explicit overlap counts exactly the sole possible partial segment on the right. Earlier sorted segments end before the candidate's left boundary because the input segments do not overlap. Hence each helper computes its candidates exactly, and the boundary argument proves that one of the two orientations contains an optimal window.

## Complexity detail

Each orientation sorts $n$ segments in $O(n\log n)$ time, builds a prefix array in $O(n)$, and performs $n$ binary searches in $O(n\log n)$. The total time is $O(n\log n)$. The sorted copies, reflected intervals, starts, and prefix sums use $O(n)$ space.

The benchmark defines `size` as the number of segments $n$ and uses 32, 128, and 256 non-overlapping singleton ranges, spanning 8x. The accepted sort-and-query method is $O(n\log n)$. A correct baseline that evaluates both boundary-aligned candidates for every segment by scanning every interval takes $O(n^2)$ time and must fail only the scaling verdict.

## Alternatives and edge cases

- **Scan all segments for every boundary candidate:** This is correct but evaluates $O(n)$ overlaps for each of $O(n)$ windows, taking $O(n^2)$ time.
- **Expand every coordinate:** Coordinates reach $10^9$, so a per-bag array or one-step sliding window is infeasible.
- **Only left-aligned windows:** This misses optima whose right boundary, rather than left boundary, touches a segment endpoint.
- **Partial final segment:** Clamp its overlap to the candidate's right endpoint and ignore it when the computed length is nonpositive.
- **Unsorted input:** Both helpers sort their own interval lists before building prefix sums.
- **Large gaps:** Empty coordinates contribute zero and require no explicit representation.
- **Window wider than all occupied coordinates:** The candidate sum may include every segment, and the prefix logic handles that directly.
