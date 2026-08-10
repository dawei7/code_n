## General

**Search for the point where accumulated area reaches half.** Let $A(y)$ be the total square area below horizontal line height $y$. In this version, overlapping square portions are counted once per square, so each square can be handled independently and its contribution added.

For square with bottom coordinate $y_i$ and side length $l_i$, the vertical height below the line is:

- zero when $y\le y_i$;
- $y-y_i$ when $y_i<y<y_i+l_i$;
- $l_i$ when $y\ge y_i+l_i$.

Its below-line area is therefore

$$
l_i\max(0,\min(y-y_i,l_i)).
$$

The helper `check(y1)` implements this. It skips squares whose bottom is not below the line. For the others, `l * min(y1 - y, l)` gives their partial or full area.

The total counted square area is

$$
S=\sum_i l_i^2.
$$

Area above the line equals $S-A(y)$. Equality requires $A(y)=S/2$.

**Use monotonicity.** As $y$ rises, no square's below-line contribution decreases. Hence $A(y)$ is continuous and non-decreasing. `check(y)` asks whether $A(y)\ge S/2$.

The initial lower bound is zero, no greater than any square bottom under the constraints. The upper bound is the greatest square top `max(y + l)`, where every square lies fully below and `check` is certainly true.

At each binary-search step:

- if the midpoint has at least half the area below, the answer is at or below it, so `r = mid`;
- otherwise, the answer is above it, so `l = mid`.

The source returns `r`, the true-side boundary. This is important when many heights split the area equally. For two separated equal squares, $A(y)$ is exactly half throughout the empty vertical gap. The lower edge of that plateau is the minimum valid $y$, and binary search for the first height satisfying `>=` converges to it.

**Why the x-coordinate is irrelevant.** A horizontal cut through one axis-aligned square depends only on its width $l_i$ and vertical overlap height. Since overlaps count multiple times, squares never need to be merged along $x$. The first coordinate is intentionally ignored in the helper.

For square `[0,0,2]` and line height $7/6$, the below height is $7/6$ and contribution is $2\cdot7/6$. A second unit square beginning at $y=1$ contributes $1/6$. Their sum is $2.5$, half the counted total $5$.

**Why the returned height is sufficiently accurate.** Each iteration halves `r-l` until it is at most `1e-5`. The true minimum boundary remains inside the interval because the false lower and true upper invariants are preserved. Returning the upper endpoint differs from the exact boundary by at most the final interval width.

The total area constraint keeps `s / 2` within reliable numeric magnitude for Python floating-point comparisons. Integer square areas are summed exactly before division; partial areas are floating point.
`check` computes exactly the problem's multiply-counted area below its line. The monotone predicate changes from false to true at the minimum equal-area height, possibly remaining exactly half on a plateau. Binary search preserves a bracket around this boundary and returns its true-side endpoint within tolerance. Thus the method produces the required minimum coordinate.

The conditional `if y < y1` also avoids passing a negative height into the partial-area formula.

The manifest labels time as $O(n)$ because the precision and coordinate limits bound the binary-search iteration count by a small constant, roughly $47$. In parameterized analysis, that factor should be shown explicitly.

## Complexity detail

Let $n$ be the number of squares, $U=\max(y_i+l_i)$, and $\varepsilon=10^{-5}$. Summing area and finding $U$ take $O(n)$. Each check costs $O(n)$ and binary search performs

$$
O\!\left(\log\frac{U}{\varepsilon}\right)
$$

iterations. Exact time is $O(n\log(U/\varepsilon))$. Under fixed constraints and fixed tolerance, the iteration count is bounded, yielding the manifest's practical $O(n)$ view.

Only scalar bounds and accumulated area are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Sweep square-edge events:** Sorting bottom/top events and integrating active total width finds the answer exactly within one linear strip, but costs $O(n\log n)$ time and $O(n)$ event space.
- **Union-area sweep:** That is required for version II, but wrong here because overlaps must contribute once for each square.
- **Separated equal areas:** A whole vertical gap may be valid; searching for the first true height returns its lowest boundary.
- **Line through an edge:** Zero-area boundaries do not create ambiguity; the area function is continuous.
- **Complete overlap:** Each square still contributes separately, exactly as the per-square sum does.
- **Large side lengths:** Python integers hold $l^2$ exactly before floating-point partial calculations.
- **All square bottoms above zero:** The lower bound remains false until the first relevant height.
- **Minimum valid value:** Returning the upper binary-search endpoint supports first-true behavior.
- **Tolerance:** Stopping at interval width `1e-5` provides the required coordinate accuracy.
- **Ignored x-coordinate:** This is safe only because overlap multiplicity makes horizontal union irrelevant.
