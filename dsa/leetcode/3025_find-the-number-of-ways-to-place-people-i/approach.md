## General

**Turn geometry into a visibility scan.** Alice must occupy the upper-left corner $A=(x_A,y_A)$ and Bob the lower-right corner $B=(x_B,y_B)$. Therefore a candidate orientation requires

$$
x_A\le x_B
\quad\text{and}\quad
y_A\ge y_B.
$$

The rectangle, including its boundary, must contain no third point. A direct method could select two points and scan every other point, but that would cost cubic time. The exact solution removes the third scan by ordering points and keeping one vertical boundary.

**Sort by $x$ ascending and $y$ descending.** The call

`points.sort(key=lambda x: (x[0], -x[1]))`

places smaller $x$ first. For equal $x$, it places larger $y$ first. After choosing `points[i]` as Alice, every later point automatically has $x_B\ge x_A$, so only the vertical condition $y_B\le y_A$ needs to be checked explicitly.

The descending tie-break is essential. If several points share Alice's $x$ coordinate, scanning them from high to low matches the upper-left to lower-right direction along a vertical fence. It also ensures that a same-$x$ point lying between Alice and a later Bob is encountered before that Bob and can block it.

**Fix Alice and scan possible Bobs left to right.** For a fixed Alice height `y1`, the source initializes `max_y = -inf`. As later points are visited in sorted order, `max_y` records the greatest $y$ value among previously scanned points that was not above Alice and that formed the current visible lower boundary.

A later point with height `y2` becomes a valid Bob exactly when

`max_y < y2 <= y1`.

The second inequality, `y2 <= y1`, enforces that Bob is no higher than Alice. The strict first inequality says Bob must lie above every previously accepted or blocking point within Alice's downward range.

**Why a candidate at or below `max_y` is blocked.** Suppose `y2 <= max_y`. The earlier point responsible for `max_y` was scanned before this candidate, so its $x$ lies between Alice's $x$ and Bob's $x$ (inclusive in equal-$x$ cases). Its $y$ satisfies

$$
y_B\le \texttt{max\_y}\le y_A.
$$

Thus that point lies inside or on the rectangle from Alice to Bob. It is a third person on the fence or in its interior, so the pair is invalid.

**Why a candidate above `max_y` is clear.** Now suppose `max_y < y2 <= y1`. Any earlier scanned point with $y$ in the vertical interval $[y2,y1]$ would have raised the visible boundary to at least that $y$, contradicting `max_y < y2`. Points above Alice are outside the rectangle, and points below Bob are also outside. Later points have $x$ beyond Bob and cannot lie inside this rectangle. Therefore no third point occupies the rectangle, so the pair is valid.

After counting the pair, the source sets `max_y = y2`. This new Bob becomes the strongest blocker for lower candidates farther to the right. A higher later Bob can still be visible because its rectangle does not extend down far enough to contain the previous lower point.

**Why `max_y` needs updating only on valid candidates.** A point above Alice is irrelevant to all rectangles extending downward from Alice, so it should not change the boundary. A point at or below the current boundary is already hidden behind a previous point and is no stronger than that boundary. Only a candidate strictly between `max_y` and `y1` raises the lower visible frontier.

**Example of the scan.** Suppose Alice has height 10 and the later points, in sorted order, have heights 4, 2, 7, 7, and 9. Starting from negative infinity, height 4 is valid and sets the boundary to 4. Height 2 is blocked. Height 7 is above the boundary and valid, then raises it to 7. The repeated height 7 is blocked because the inequality is strict; the earlier point lies on the later rectangle's horizontal boundary. Height 9 is valid and raises the boundary again. This exactly captures both interior and boundary exclusion.

**Every orientation is considered once.** Sorting ensures that a geometrically possible Alice appears no later than her Bob. The outer loop chooses every point as Alice, and the suffix scan considers every later point once. The vertical test rejects reversed or upward orientations. Hence all permissible ordered placements are examined without counting a pair twice.

## Complexity detail

Let $N$ be the number of points. Sorting costs $O(N\log N)$ time. The nested scans examine

$$
\sum_{i=0}^{N-1}(N-i-1)=\frac{N(N-1)}{2}
$$

candidate pairs, so they cost $O(N^2)$ time and dominate sorting. Total time is $O(N^2)$.

The high-level algorithm needs only `ans`, `max_y`, and loop variables after sorting. However, the exact Python expression `points[i + 1:]` creates a new suffix list on every outer iteration. Across the whole execution that causes $O(N^2)$ cumulative element-reference allocation work, while the largest one suffix uses $O(N)$ memory at a time. Python's in-place sort may also use $O(N)$ temporary workspace. Therefore the exact implementation's peak auxiliary space is $O(N)$, not the $O(1)$ shown in the local manifest.

The source also mutates the input by sorting `points`. The answer itself is one integer.

## Alternatives and edge cases

- **Triple-loop rectangle check:** Select Alice and Bob, then test every other point. It is easy to derive but costs $O(N^3)$ time.
- **Two-dimensional prefix sums:** Coordinate compression plus a grid prefix sum can query rectangle populations, but it uses substantially more machinery and space for this small-$N$ version.
- **Iterate by index without slicing:** Replacing the suffix slice with `for j in range(i + 1, n)` preserves the same $O(N^2)$ algorithm while avoiding the per-iteration lists. That would improve auxiliary space, but it is not the exact protected source.
- **Sort equal $x$ by ascending $y$:** This is incorrect for vertical fences because a lower same-column point could appear before the upper Alice candidate, breaking the one-direction scan and blocker logic.
- **Bob above Alice:** `y2 <= y1` fails, so the orientation is rejected even if the rectangle would otherwise be empty.
- **Alice and Bob on one vertical line:** Equal $x$ is allowed; the fence may have zero area. The descending-$y$ tie order handles it correctly.
- **Alice and Bob on one horizontal line:** Equal $y$ is allowed. Once one point at that height is accepted, another farther right at the same height is blocked by the strict `max_y < y2` test.
- **A point on the rectangle boundary:** It blocks the pair just like an interior point. The non-strict coordinate containment and strict frontier update correctly enforce this.
- **Distinct point coordinates as pairs:** Individual $x$ or $y$ values may repeat even though complete points are distinct, which is why the tie rules matter.
- **Input mutation:** The returned count is independent of original order, but the caller receives `points` rearranged into sorted order.
