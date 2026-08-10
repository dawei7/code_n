## General

**The vertical coordinates do not affect how many rectangles are needed.** A rectangle may start at height zero and choose any nonnegative top height `y2`. After deciding which points belong to one rectangle, its top can simply be placed at the largest of their $y$-coordinates. There is no height limit or height cost.

The only restrictive dimension is horizontal. One rectangle covers points whose $x$-coordinates fit in some inclusive interval `[x1, x2]` with:

$$
x_2-x_1\le w.
$$

The two-dimensional problem therefore reduces to covering all point $x$-coordinates with the minimum number of closed intervals of width at most $w$.

**Sort points from left to right.** `points.sort()` orders each pair lexicographically, primarily by $x$ and secondarily by $y$. Only the primary ordering matters to the greedy argument. Points sharing an $x$-coordinate become adjacent and will always fit in the same horizontal interval.

Variable `x1` is somewhat misleadingly named: after a rectangle is opened, it stores that rectangle's rightmost covered $x$-coordinate, not its left endpoint. It begins at -1. Since every input $x$ is nonnegative, the first point necessarily satisfies `x > x1` and opens the first rectangle.

**Start a maximum-width rectangle at the leftmost uncovered point.** When the scan encounters coordinate `x` beyond the current right boundary, that point is uncovered. The source increments `ans` and sets:

`x1 = x + w`.

This describes a rectangle whose horizontal range is `[x, x + w]`. Its vertical top can be high enough for every point assigned to it.

If a later point has `x <= x1`, it lies on or inside this rectangle's horizontal boundary and needs no new rectangle. The comparison is strict `x > x1` because boundary points count as covered.

**Why placing the left edge at the uncovered point is optimal.** Let $p$ be the smallest uncovered $x$-coordinate. Every valid solution needs some new rectangle covering $p$. Such a rectangle's left edge cannot be greater than $p$. If its left edge is smaller, shift it right until the left edge equals $p$. The shifted rectangle still covers $p$ and extends at least as far right as before, because its permitted width remains $w$.

Therefore, among all rectangles that can cover the required leftmost point, `[p,p+w]` covers the farthest possible future coordinates. Choosing it cannot increase the number of rectangles needed later.

After it covers every point through $p+w$, the next uncovered point creates an identical smaller subproblem. Repeating the exchange argument proves every greedy rectangle is compatible with an optimal solution.

**A trace for the first example.** Sorting the $x$-coordinates yields 1, 1, 1, 2, 3, 4 with `w=1`. The first coordinate opens interval `[1,2]`. All points at 1 and the point at 2 fit. Coordinate 3 lies beyond the boundary and opens `[3,4]`, which also covers 4. Two rectangles are used.

For coordinates 0 through 6 with `w=2`, the greedy intervals begin at 0, 3, and 6. Their ranges are `[0,2]`, `[3,5]`, and `[6,8]`. The answer is three.

**Why duplicate horizontal positions cost nothing extra.** A rectangle's top may be chosen as the maximum $y$ among all points it covers. Any number of distinct points at the same $x$ can therefore share it, even if their heights differ greatly.

**The algorithm constructs enough information without storing rectangles.** `ans` counts the chosen intervals and `x1` stores only the current right boundary. The actual left boundaries are the values of `x` that trigger new rectangles. Heights never need to be recorded because their unconstrained choice proves vertical feasibility.

**A correctness invariant.** Before each scanned point, all earlier points are covered by exactly `ans` greedy rectangles, and `x1` is the right boundary of the last one. If current `x <= x1`, it is already covered and the invariant continues. Otherwise it is the leftmost uncovered point, every solution requires another rectangle, and the greedy maximum-width placement is never worse than another placement. At scan completion, every point is covered and no solution can use fewer rectangles.

## Complexity detail

Sorting $n$ point pairs costs $O(n\log n)$ time. The subsequent scan visits each point once and costs $O(n)$, so total time is $O(n\log n)$.

`points.sort()` mutates the input list. CPython's sorting implementation can use $O(n)$ temporary memory in the worst case, consistent with the manifest's $O(n)$ space bound. The explicit greedy state after sorting is only two integers, or $O(1)$.

No vertical data structure is required. Large coordinates and `x + w` are safe in Python; fixed-width languages should use a type that can represent up to $2\cdot10^9$ here.

## Alternatives and edge cases

- **Sort only the $x$-coordinates:** Extracting them makes the reduction explicit but allocates another $O(n)$ list.
- **Interval dynamic programming:** It can model coverage choices, but the leftmost-uncovered exchange argument makes it unnecessary.
- **Unsorted greedy scan:** It is incorrect because a later unseen point might lie left of the chosen interval.
- **`w = 0`:** One rectangle covers exactly one distinct $x$-coordinate, so the answer is the number of distinct $x$ values.
- **Several points at one $x$:** All can share one rectangle regardless of height.
- **Point on the right boundary:** `x == x1` is covered because rectangle boundaries are inclusive.
- **Large gap:** Any coordinate beyond `x1` must start a new rectangle.
- **One point:** It opens one rectangle.
- **Arbitrary height:** Choose `y2` as the maximum height of assigned points.
- **Nonnegative coordinates:** Initial boundary -1 guarantees that the first point opens a rectangle.
- **Input mutation:** Sorting changes point order but not the pairs themselves.
- **Second-coordinate sorting:** It occurs automatically for tied $x$ values and has no effect on the count.
- **Maximum width:** Using less than `w` at a leftmost uncovered point cannot cover more future points.
- **Overlapping rectangles:** Allowed but never needed by the greedy proof.
- **Return only the count:** Rectangle coordinates need not be materialized.
