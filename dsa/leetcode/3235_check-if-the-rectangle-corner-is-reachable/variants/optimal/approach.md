## General

**Reduce the path question to an obstacle barrier.** Combine the rectangle's top and left sides into one virtual boundary component, and combine its bottom and right sides into another. A connected closed obstacle joining these two boundary groups separates the bottom-left corner from the top-right corner. If no such component exists, the open free region contains a path between the corners.

Use disjoint-set union for all circles plus these two virtual nodes. A circle may join a virtual node only when its disk intersects the corresponding finite boundary segment. Compute this with squared distance to the segment, not merely distance to its infinite supporting line. This distinction is essential for circles outside the rectangle: a circle near the extension of the top edge may never touch the actual top segment.

**Connect relevant circle overlaps.** Two disks can belong to the same interior obstacle component when their center distance is at most the sum of their radii. The radius-weighted point on the center segment,

$$
P=\frac{r_2C_1+r_1C_2}{r_1+r_2},
$$

lies in both disks whenever they overlap. Requiring both coordinates of $P$ to be below the rectangle's upper bounds keeps an overlap connection that is relevant inside the rectangle; overlaps wholly beyond the top or right are not allowed to create a false barrier. Connections already meeting a rectangle side are represented through the appropriate virtual boundary.

Process every circle pair, union every relevant overlap, and return `False` as soon as the two virtual boundary roots match. Exact squared integer comparisons handle tangency without floating-point error.

A circle containing either endpoint necessarily intersects both sides adjacent to that corner, so it immediately joins the opposing virtual groups and correctly blocks the path.

## Complexity detail

Let $n=\lvert\texttt{circles}\rvert$. Every unordered circle pair is tested once, taking $O(n^2)$ time. The disjoint-set structure and circle data use $O(n)$ auxiliary space; path compression makes each union/find operation amortized nearly constant.

## Alternatives and edge cases

- **Use infinite boundary lines:** This falsely treats circles beyond a segment endpoint as touching the rectangle.
- **Union every overlapping pair globally:** An overlap that exists only outside the rectangle can create a false blocking chain.
- **Rasterize the rectangle:** Coordinate bounds reach $10^9$, so a grid search is neither exact nor feasible.
- A circle that contains or touches either endpoint makes the destination unreachable.
- Circle-circle and circle-boundary tangency count as blocked because the path may not touch an obstacle.
- A circle wholly outside the rectangle has no effect.
- One circle touching only one boundary group does not by itself form a barrier.
- A chain of several circles can block even when no individual circle reaches both groups.
- Squared integer distances avoid square roots and precision loss at maximum coordinates.
