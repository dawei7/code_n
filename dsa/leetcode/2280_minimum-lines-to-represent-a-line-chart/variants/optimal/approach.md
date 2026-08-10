## General

**Put chart points into day order**

The line chart connects points in increasing day order, not in the arbitrary input order. `stockPrices.sort()` sorts each two-element record lexicographically, so the distinct day coordinate orders the points correctly.

After sorting, every consecutive pair represents one required chart edge. Because all days are distinct, each horizontal difference `dx1 = x1 - x` is positive. Vertical differences may be positive, zero, or negative as the price rises, stays constant, or falls.

The sort mutates `stockPrices`, so callers observe the reordered points after the method returns.

**A single line can cover a whole run of equal slopes**

Every adjacent pair must be connected, but several consecutive edges can be drawn as one straight line when their slopes are equal. A new line is necessary exactly when the current edge's slope differs from the preceding edge's slope.

Therefore, the answer is the number of maximal consecutive runs of equal edge slopes. The solution scans the edges once and counts the start of each run.

**Compare slopes without floating point**

For one edge, slope is `dy / dx`. For the next edge, it is `dy1 / dx1`. Since both horizontal differences are nonzero, the slopes are equal exactly when

$$
\texttt{dy}\cdot\texttt{dx1}
=
\texttt{dx}\cdot\texttt{dy1}.
$$

The code tests the negation, `dy * dx1 != dx * dy1`, to detect a new line.

Cross multiplication avoids floating-point rounding. Two rational slopes such as one-third and two-sixths compare equal exactly even if their decimal forms cannot be represented precisely. It also avoids reducing fractions by greatest common divisors.

**Use a sentinel slope to count the first edge**

The previous direction begins as `dx = 0, dy = 1`, representing a vertical direction. Every real chart edge has positive `dx1` because days are distinct. On the first comparison,

`dy * dx1` is positive while `dx * dy1` is zero,

so the condition is always true and `ans` becomes one.

This sentinel removes a special branch for the first edge. After the comparison, `dx, dy = dx1, dy1` stores the real current direction for the next iteration.

If there is only one stock point, `pairwise` yields no edge, the sentinel is never compared, and `ans` remains zero. No line segment is needed to connect a single point.

**Why proportional direction vectors are enough**

Two consecutive chart edges lie on the same infinite line when they share the middle point and have equal slopes. Equal slope guarantees their direction vectors are proportional. Sharing the endpoint then guarantees collinearity, so the line used for the first edge can continue through the second.

It is not necessary for the raw differences to be identical. An edge with direction `(1, 2)` and the next with `(3, 6)` belong to the same line because cross products agree.

Negative vertical differences also work: both products retain their signs, distinguishing an upward slope from a downward one.

**Trace the line-run count**

Suppose four sorted points have consecutive direction vectors `(1, -1)`, `(1, -1)`, and `(1, 0)`. The sentinel differs from the first vector, so the answer becomes one. The second vector has the same cross-multiplied slope, so no new line is added. The third is horizontal rather than downward, so the answer becomes two.

The method counts lines, not slope values globally. If a slope appears, changes, and then reappears later, those separated edge runs require different line segments and are counted separately.

**Why the count is minimal**

Whenever adjacent slopes differ, no single straight line can contain both edges, so every representation needs a line boundary there. This gives a lower bound of one line for the first edge plus one for every slope change.

Within each maximal equal-slope run, all connected points are collinear, so one line actually represents the whole run. Constructing one line per run achieves the lower bound. Thus, the counted number is both necessary and sufficient.

## Complexity detail

Let `n` be the number of points. Sorting costs `O(n \log n)` time. `pairwise` produces `n - 1` edges and the scan uses constant arithmetic for each, adding `O(n)`. Total time is `O(n \log n)`.

The slope scan itself uses `O(1)` variables. Python's in-place Timsort can use `O(n)` temporary memory in the worst case, so including sorting workspace gives `O(n)` auxiliary space, matching the manifest.

Coordinate differences and cross-products may exceed 32-bit range. Python integers are safe; fixed-width implementations should use a sufficiently wide type.

## Alternatives and edge cases

- **Floating-point slopes:** They are easy to write but can misclassify mathematically equal rational slopes due to rounding.
- **Reduced fraction pairs:** Dividing `dy` and `dx` by their greatest common divisor gives exact comparable slopes, but cross multiplication is simpler.
- **Store every slope:** Only the immediately previous direction is needed because the goal is consecutive slope runs.
- **Compare all triples after sorting:** It gives the same collinearity test; the stored previous direction is its constant-state form.
- **One point:** There are no adjacent edges, so zero lines are returned.
- **Two points:** The sentinel ensures the only edge contributes one line.
- **Horizontal edges:** `dy = 0` compares correctly.
- **Falling prices:** Negative `dy` values preserve exact slope signs.
- **Different step sizes on one line:** Proportional vectors pass the cross-product equality.
- **A slope reappears later:** A change away and back creates separate line runs and must be counted again.
- **Distinct days:** They guarantee every real `dx` is positive and eliminate vertical chart edges.
- **Large coordinates:** Cross-products require wide arithmetic outside Python.
- **Input order:** Sorting is required before adjacency has chart meaning.
- **Input mutation:** `stockPrices.sort()` changes the caller's list order.
- **Inclusive point connection:** Each line run shares endpoints with its neighboring run, which is allowed in the chart.
