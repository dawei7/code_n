## General

**Turn every possible side into a normalized geometric key.** Enumerate each of the $\binom{n}{2}$ point pairs as a segment. Divide `(dy, dx)` by the greatest common divisor of its absolute components and force one sign convention, so all parallel segments share exactly one slope key. The invariant `dy * x - dx * y` is constant along a line with that normalized direction; combining it with the slope distinguishes parallel supporting lines.

**Count candidate pairs without admitting a degenerate quadrilateral.** For a slope containing $k$ segments, $\binom{k}{2}$ chooses two possible parallel sides. Two segments on the same supporting line cannot be opposite sides of a convex quadrilateral, so subtract $\binom{c}{2}$ for every same-line group of $c$ segments. Segments on different parallel lines cannot share an endpoint, and their four endpoints form a convex trapezoid. Thus the remaining total counts every trapezoid once for each parallel-side pair it has.

**Remove the second count of each parallelogram.** A non-parallelogram trapezoid has exactly one parallel-side pair and is already counted once. A parallelogram has two and is counted twice. Its diagonals have the same midpoint, so group every point-pair by the doubled midpoint `(x1 + x2, y1 + y2)` and choose two diagonals from each group. Equal-midpoint segments with the same slope are collinear and degenerate, so subtract those same-slope pairs. Every remaining diagonal pair identifies one non-degenerate parallelogram, and subtracting this number leaves every qualifying four-point set counted exactly once.

## Complexity detail

Let $n$ be the number of points. There are $\binom{n}{2}=O(n^2)$ segments. Normalizing and inserting each segment into a constant number of hash maps takes expected $O(n^2)$ time, and aggregating their groups takes at most the same order. The maps can contain $O(n^2)$ distinct keys, so auxiliary space is $O(n^2)$.

The benchmark uses $S=n$ points on the parabola $y=x^2$. The accepted pair-grouping method performs $O(S^2)$ work. A correct exhaustive implementation that checks every four-point subset performs $O(S^4)$ work and therefore must fail only the scaling verdict.

## Alternatives and edge cases

- **Enumerate every four-point subset:** Building the convex hull and checking opposite slopes is direct and correct, but it requires $O(n^4)$ candidate selections.
- **Floating-point slopes:** Division can merge distinct rational slopes or split equal ones through rounding; reduced integer pairs are exact.
- **Vertical and negative slopes:** The sign convention must map both orientations of the same segment to one key, including the `dx = 0` case.
- **Four collinear points:** Same-line subtraction excludes degenerate selections even though many segment pairs have equal slopes.
- **Interior points:** Only endpoint sets forming a convex quadrilateral can arise from sides on two distinct parallel lines; a point inside a triangle contributes no trapezoid by itself.
- **Parallelograms:** They satisfy the “at least one pair” definition but must contribute one, not two.
- **Doubled midpoints:** Store coordinate sums instead of dividing by two, preserving exact integer keys for half-integer midpoints.
