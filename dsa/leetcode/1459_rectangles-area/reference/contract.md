## Function Contract

**Input**

- `Points(id, x_value, y_value)`: uniquely identified integer-coordinate
  points.

Let $P$ be the number of points, and let $R$ be the number of reported
non-degenerate point pairs.

**Return value**

Return columns `p1`, `p2`, and `area`. Represent each unordered pair once with
`p1 < p2`. A pair is valid only when its points differ in both coordinates, and
its area is

$$
\lvert x_1-x_2\rvert\,\lvert y_1-y_2\rvert.
$$

Order the rows by `area DESC, p1 ASC, p2 ASC`.
