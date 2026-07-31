## General

**Put every possible lower-right endpoint after its partner.** Sort points by increasing $x$ and, when $x$ values tie, by decreasing $y$. For a fixed point $A$ at index `i`, any later point has $x_B\ge x_A$. The descending tie-break is essential: on one vertical line, a higher point appears first and can be the upper endpoint, while the reverse ordered pair is never considered.

**Track the visible lower boundary.** Scan later points from left to right. A point $B$ can be below $A$ only when $y_B\le y_A$. Among such points, keep `highest_lower_y`, the greatest $y$ value already accepted. If $y_B\le\texttt{highest_lower_y}$, the previously accepted point with that height lies inside or on the closed rectangle from $A$ to $B$, so $B$ is blocked. If instead $y_B$ is strictly greater than this boundary, no earlier scanned point lies in the rectangle's vertical interval; count the pair and raise the boundary to $y_B$.

Points above $A$ cannot lie in any candidate rectangle rooted at $A$ and do not change the boundary. Thus the scan counts exactly the endpoints visible from $A$ without inspecting every third point separately. Repeating it for every possible $A$ counts each ordered pair once.

## Complexity detail

Sorting takes $O(N\log N)$ time. The nested scans examine each ordered index pair once, for $O(N^2)$ total time, which dominates sorting. Apart from the sorting workspace used by the language runtime, the algorithm stores a fixed number of counters and coordinates, so its auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Inspect every third point:** Enumerating a pair and then scanning the whole input for a blocker is direct but costs $O(N^3)$ time.
- **Rectangle occupancy grid:** A prefix-sum grid can answer rectangle counts quickly because coordinates are bounded, but it adds grid construction and boundary bookkeeping that the visibility scan avoids.
- **Equal x-coordinates:** The higher point must precede the lower point; descending $y$ tie-breaking preserves the ordered upper-left relation and detects vertical-line blockers.
- **Equal y-coordinates:** Only adjacent visible points along that horizontal level can form an empty line segment; the strict boundary update blocks farther endpoints.
- **Border points:** A third point on any rectangle edge invalidates the pair exactly as an interior point does.
- **Rising diagonal:** When $y$ increases with $x$, no later point is below the fixed upper-left endpoint, so the contribution is zero.
