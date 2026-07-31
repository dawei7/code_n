## General

**Make horizontal order implicit.** Sort the points by increasing $x$, breaking equal-$x$ ties by decreasing $y$. For a point $A$ at index `i`, every later point is at or to its right. The tie-break also puts the higher point first on a vertical line, so only the legal upper-to-lower ordering can be counted.

**Characterize which lower endpoints remain visible.** Fix $A$ and scan later points in sorted order. A candidate $B$ must satisfy $y_B\le y_A$. Keep `highest_lower_y`, the largest $y$ among previously accepted lower-right endpoints. If $y_B\le\texttt{highest_lower_y}`, that earlier visible point lies horizontally between $A$ and $B$ and vertically inside or on their closed fence, so it blocks the pair. When $y_B$ is strictly above the stored boundary but no higher than $A$, no earlier point can occupy the fence; count the pair and raise the boundary.

Points above $A$ are outside every downward fence rooted at $A$ and do not alter the boundary. Because the scan processes non-decreasing $x$, every possible blocker with horizontal coordinate between the endpoints has already been considered when $B$ is reached. The maintained boundary therefore distinguishes exactly the empty fences without a third nested loop.

Each ordered pair appears once under its possible upper-left endpoint. The sort enforces the horizontal condition, the upper bound on `y` enforces the vertical condition, and the strict visibility test rejects precisely those pairs containing a third point. Summing the accepted endpoints is therefore correct.

## Complexity detail

Sorting takes $O(N\log N)$ time, and the nested visibility scans examine $O(N^2)$ ordered index pairs, so total time is $O(N^2)$. Apart from the sorting workspace supplied by the language runtime, the scan stores only counters and one boundary value, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Inspect every third point:** Testing every candidate fence against all other points is correct but costs $O(N^3)$ time, which is too slow for $N=1000$.
- **Coordinate-compressed occupancy queries:** A two-dimensional prefix structure can answer rectangle occupancy after compression, but it adds substantial structure while the sorted visibility frontier already gives the required quadratic bound.
- **Equal x-coordinates:** Decreasing-$y$ tie-breaking is mandatory so vertical-line pairs are considered from upper to lower and intermediate border points block farther endpoints.
- **Equal y-coordinates:** Along a horizontal line, only consecutive visible points can form an empty fence; the strict boundary comparison rejects farther points.
- **Negative coordinates:** The ordering and comparisons depend only on relative positions, so the full signed coordinate range requires no translation.
- **Border blockers:** A third person on any edge invalidates the placement just as an interior person does.
- **Zero-area fences:** Horizontal and vertical lines are explicitly legal when their closed segment contains only Alice and Bob.
