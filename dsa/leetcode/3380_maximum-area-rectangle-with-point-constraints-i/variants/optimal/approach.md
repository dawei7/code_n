## General

Two opposite corners of a nondegenerate axis-parallel rectangle must have different $x$- and $y$-coordinates. For every such pair $(x_1,y_1)$ and $(x_2,y_2)$, the other corners are forced to be $(x_1,y_2)$ and $(x_2,y_1)$. Store all input points in a set so those two corner checks are constant time.

When all four corners exist, form their closed bounding box. Scan every input point and reject the candidate if a point inside that box or on its boundary is not one of the four selected corners. Otherwise, its area is

$$
\lvert x_1-x_2\rvert\,\lvert y_1-y_2\rvert.
$$

Every axis-parallel rectangle has two diagonal pairs, so the enumeration necessarily considers every possible candidate. The corner-set check accepts exactly the four-corner shapes, and the closed-box scan enforces both the interior and border exclusions. Taking the greatest area among the surviving candidates therefore gives the required answer.

## Complexity detail

There are $O(n^2)$ point pairs. A pair with all required corners may scan all $n$ points, giving $O(n^3)$ worst-case time. The point set and temporary corner set use $O(n)$ total space.

The benchmark defines `size` as $n^3$, the reference's candidate pair and containment-inspection budget, across legal inputs with four, seven, and ten points. A correct slower baseline enumerates $\binom{n}{4}$ corner subsets and scans all $n$ points for each rectangular subset, growing as $O(n^5)$ and therefore failing scaling while preserving every answer.

## Alternatives and edge cases

- **Enumerate every four-point subset:** It is direct and correct but examines $O(n^4)$ subsets before containment scans.
- **Coordinate compression with range queries:** Fenwick or segment trees become useful in the large-input sequel, but are unnecessary for $n\leq10$.
- **Check only the interior:** A fifth point on any of the four edges also invalidates the candidate, so the bounding comparisons must be inclusive.
- **Exclude no points from the scan:** The four required corners lie on the boundary by definition and must not invalidate their own rectangle.
- **Missing corner:** Two diagonal-looking points do not define a candidate unless both cross-coordinate corners exist.
- **Degenerate pair:** Equal $x$ or equal $y$ produces zero width or height and is not a rectangle.
- **Multiple candidates:** A blocked large rectangle does not preclude a smaller empty rectangle using some of the same points.
- **No valid rectangle:** Preserve the initial sentinel and return `-1`.
- **Maximum coordinates:** A $100$ by $100$ rectangle has area $10{,}000$, which fits comfortably in ordinary integer types.
