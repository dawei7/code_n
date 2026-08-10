## General

The forbidden regions are closed disks: the path may neither enter nor touch any circle. Trying to construct a curve explicitly is difficult because there are infinitely many possible paths. The solution instead asks when the union of the disks forms a continuous barrier across the rectangle. This turns geometry into connectivity among circles and rectangle sides.

Name the start corner bottom-left and the destination top-right. Group the left and top sides together, and group the right and bottom sides together. A connected forbidden component that touches at least one side in the first group and at least one side in the second group separates the two corners. The possible contacts include left-to-right, top-to-bottom, left-to-bottom, and top-to-right barriers. Conversely, if neither corner is covered and no relevant disk component connects those opposing boundary groups, there remains a route through the rectangle's free region.

**Reject a covered endpoint first.** The helper `in_circle` compares the squared center-to-point distance with `r ** 2`. It is called for both `(0, 0)` and `(xCorner, yCorner)`. The comparison uses `<=` because touching a circle is forbidden. If either endpoint lies on or inside any disk, no legal path can even begin or end, so the method immediately returns `False`.

Squared distances avoid square roots and preserve exact integer comparisons:

$$
(x-c_x)^2+(y-c_y)^2\le r^2.
$$

Python integers also avoid overflow despite coordinates and radii as large as $10^9$.

**Classify contacts with the two boundary groups.** The helper `cross_left_top` returns true when a disk reaches the left side within the rectangle's vertical span or reaches the top side within its horizontal span. Reaching the left line means `abs(cx) <= r`, and `0 <= cy <= yCorner` ensures that the perpendicular contact is aligned with the finite side rather than an extension of its line. The top-side test is analogous.

The helper `cross_right_bottom` performs the matching tests for the right and bottom sides. Equal distance counts as contact because the path is not allowed to touch a circle. Although centers are guaranteed positive, the absolute-value expressions make the intended distance-to-line checks explicit.

**Connect disks only when their overlap matters inside the rectangle.** Two disks geometrically meet or overlap when their center distance is at most the sum of their radii:

$$
(x_1-x_2)^2+(y_1-y_2)^2\le(r_1+r_2)^2.
$$

That condition alone is not sufficient. Two large circles could overlap only outside the rectangle, and treating them as connected would invent a barrier that the path inside the rectangle never encounters.

The source applies two additional weighted inequalities:

`x1 * r2 + x2 * r1 < (r1 + r2) * xCorner`

and the analogous expression for `yCorner`. Dividing the first by `r1 + r2` reveals the weighted point

$$
P=\frac{r_2C_1+r_1C_2}{r_1+r_2}.
$$

This point lies on the segment between the centers. If the center distance is at most `r1 + r2`, its distance to `C1` is at most `r1` and its distance to `C2` is at most `r2`, so it belongs to both disks. The strict coordinate inequalities require this shared point to lie below the rectangle's top and left of its right side. Its coordinates are positive because all circle centers have positive coordinates. Thus the accepted connection has shared forbidden material in the rectangle's relevant interior instead of only beyond the upper or right boundary.

This relevance filter is a particularly important part of the exact solution. Omitting it and unioning every pair of intersecting disks in the entire plane can produce false “blocked” answers when the intersection that joins their components is outside the rectangle.

**Depth-first search through a forbidden component.** The Boolean list `vis` records circles already reached. The outer loop considers every circle. After the endpoint checks, an unvisited circle that touches the left/top group becomes a DFS starting point.

Inside `dfs(i)`, the current disk is first checked against the right/bottom group. Reaching it means a complete barrier has been found, so the search returns true immediately. Otherwise the disk is marked visited, and the code examines every circle `j`. It skips an already visited circle and any circle whose disk does not overlap the current one. For an overlapping pair, it applies both weighted interior-relevance inequalities before recursively exploring `j`. If any recursive branch reaches the opposing boundary group, true propagates to the outer loop, which returns `False` for the reachability question.

If a DFS exhausts its entire component without touching right or bottom, that component cannot be the required separator. Its circles remain visited, so the outer loop never searches the same component again. Components that do not touch left or top are not DFS roots because they cannot connect the two designated boundary groups, although they may still be examined from a relevant component if connected to one.

If all circles are processed without covering a corner or discovering a left/top-to-right/bottom forbidden component, the method returns `True`.

**Why the boundary test decides reachability.** The circles and their contacts form closed obstacles in a closed rectangle. A legal curve between diagonally opposite corners fails exactly when a connected closed obstacle separates them. Such a separator must join the two grouped portions of the rectangle boundary: left or top on one side, right or bottom on the other. Pairwise relevant overlaps build precisely the connected components of the obstacle union that matter within the rectangle. The DFS tests whether any such component has contacts in both groups. Therefore a found component is sufficient to block every path, and the absence of all such components, together with free endpoints, is sufficient for a route.

The code is graph search without explicitly building an adjacency matrix. Each circle is a vertex. Relevant disk overlap supplies an edge, and side contacts supply connections to two conceptual boundary vertices. Calculating edges on demand saves an $O(n^2)$ Boolean matrix while preserving the same graph.

## Complexity detail

Let $n$ be the number of circles. A visited circle scans all $n$ circles in its DFS loop. Each circle is visited at most once, so there are at most $n^2$ pair examinations. The outer endpoint and boundary checks add only $O(n)$ work. Every geometric test uses a constant number of integer operations, giving $O(n^2)$ time.

The `vis` array uses $O(n)$ auxiliary space. The recursive DFS call stack can also contain $O(n)$ circles in a chain, so total auxiliary space is $O(n)$. No $O(n^2)$ adjacency structure is stored.

There is an implementation-level concern in Python: a chain near the maximum of one thousand circles can approach or exceed the interpreter's default recursion limit. The algorithmic space bound remains $O(n)$, but an iterative stack would be safer for adversarial deep components. The exact source does not raise the recursion limit.

Coordinate arithmetic can create values on the order of $10^{18}$ in squared distances and weighted products. Python evaluates them exactly; a fixed-width language needs signed 64-bit arithmetic, with care that intermediate sums also remain representable.

## Alternatives and edge cases

- **Disjoint-set union:** Create two conceptual boundary nodes and union every relevant overlapping circle pair plus each circle's boundary contacts. Testing whether the boundary nodes become connected gives the same $O(n^2)$ time and $O(n)$ space, avoids recursion depth, and often makes the connectivity interpretation explicit.
- **Explicit adjacency lists:** Precomputing all relevant edges and then running BFS or DFS is straightforward, but it can store $O(n^2)$ edges. The source recomputes pair relations while scanning and needs only `vis`.
- **Union every intersecting pair in the plane:** This simpler test is unsafe. An overlap outside the rectangle must not connect two obstacles for a path constrained to the rectangle; the weighted coordinate filter prevents that false connection.
- **Grid search:** Rasterizing the rectangle loses exactness and is impossible when coordinates reach $10^9$. Narrow passages can also disappear or appear depending on grid resolution.
- **Attempt a straight segment only:** A blocked diagonal does not imply that every curved path is blocked. Reachability depends on topological separation by obstacle components, not on visibility along one line.
- **A circle touching the start or destination:** The immediate `in_circle` checks return false reachability, including exact tangency, because the path is forbidden from touching a disk.
- **Tangent circles:** The disk-overlap comparison uses `<=`, so externally tangent disks are connected. There is no positive-width gap between closed forbidden regions, and a path may not pass through their touching point.
- **A circle entirely outside the rectangle:** It has no relevant boundary contact and normally no accepted interior connection, so it does not affect the result. Example four is of this form.
- **One disk touches only left and top:** Both contacts belong to the same boundary group, so they do not alone prove separation. A connection to right or bottom is still required.
- **One disk touches left and bottom:** Those sides belong to opposite groups, so DFS begins from its left contact and immediately succeeds through its bottom contact. The component traps the starting corner's side of the rectangle even if the corner itself is outside the disk.
- **Strict weighted upper-bound tests:** The source uses `<` rather than `<=` for the weighted point's right/top coordinates. This is part of its definition of an overlap relevant to the rectangle interior; changing the comparisons without a fresh geometric proof can alter boundary-only configurations.
- **Long chains of circles:** Connectivity is transitive. No single circle needs to touch both boundary groups; DFS correctly detects a chain in which neighboring disks overlap and only the two end disks touch the respective sides.
- **Deep recursion:** With up to one thousand vertices, an iterative DFS or DSU is operationally safer in Python. The recursive source may encounter a `RecursionError` on a sufficiently deep overlap chain even though its geometric reasoning and asymptotic bounds are otherwise sound.
