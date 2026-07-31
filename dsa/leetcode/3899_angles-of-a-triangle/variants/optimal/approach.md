## General

**Reduce triangle validity to one strict comparison**

Sort the lengths as $a \le b \le c$. For positive lengths, the two triangle inequalities involving $c$ on the left are automatic: $a+c>b$ and $b+c>a$. The only condition that can fail is $a+b>c$. Equality would place all three vertices on a line and give zero area, so it must be rejected along with $a+b<c$.

**Recover each angle from its opposite side**

For a valid triangle, the law of cosines gives the angle opposite side $a$ as

$$
\alpha=\arccos\left(\frac{b^2+c^2-a^2}{2bc}\right).
$$

Apply the same formula cyclically for the angles opposite $b$ and $c$, then convert the three radian values to degrees. Floating-point rounding can move a theoretically valid cosine slightly outside $[-1,1]$, so clamp it to that closed interval before calling inverse cosine.

Longer sides face angles that are at least as large as those opposite shorter sides. Because $a$, $b$, and $c$ were sorted, computing their opposite angles in that order already produces the required non-decreasing result.

If the inequality fails, the algorithm returns `[]`, exactly as required. Otherwise, the law of cosines uniquely determines each internal angle from the three side lengths; therefore each computed value is the corresponding triangle angle. Their side-based order proves that the returned valid result is also correctly sorted.

## Complexity detail

The contract fixes the input length at three. Sorting those three values, checking validity, and evaluating three formulas therefore take $O(1)$ time. The fixed three-angle result and all auxiliary values use $O(1)$ space.

The `bounded_domain` certificate replaces runtime scaling because no legal input has more or fewer than three side lengths. Varying the integer magnitudes within $[1,1000]$ changes numeric values but never the amount of algorithmic work, so artificial workload tiers would not test a complexity class.

## Alternatives and edge cases

- **Coordinate reconstruction with `atan2`:** Place one side on the horizontal axis, derive the third vertex, and measure directions. This is also constant time but introduces more coordinate bookkeeping than applying the law of cosines directly.
- **Derive the third angle from $180^\circ$:** Computing two angles and subtracting them from $180^\circ$ saves one inverse-cosine call, but it can concentrate the rounding errors of both earlier values in the last result.
- **Equality in the triangle inequality:** When $a+b=c$, the would-be triangle has zero area and must return `[]`; using a non-strict comparison is essential.
- **Input permutations:** Sorting makes the decision and returned order independent of how the caller arranged the three sides.
- **Very thin valid triangles:** Inputs such as `[1,1000,1000]` contain a small but positive angle and must not be mistaken for a degenerate triangle.
- **Inverse-cosine boundary:** Clamping only compensates for floating-point roundoff near $-1$ or $1$; it does not replace the exact integer triangle-validity check.
