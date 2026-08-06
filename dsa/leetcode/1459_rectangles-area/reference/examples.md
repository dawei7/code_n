## Examples

**Example 1**

- **Input:** `Points = [[1,2,7],[2,4,8],[3,2,10]]`

| id | x_value | y_value |
|---:|---:|---:|
| 1 | 2 | 7 |
| 2 | 4 | 8 |
| 3 | 2 | 10 |

- **Output:** `[[2,3,4],[1,2,2]]`

| p1 | p2 | area |
|---:|---:|---:|
| 2 | 3 | 4 |
| 1 | 2 | 2 |

The source diagram's point and rectangle relationships are reproduced in the
following accessible evaluation table:

| Point pair | Width | Height | Area | Result |
|---|---:|---:|---:|---|
| `(1, 2)` | $\lvert 2-4\rvert=2$ | $\lvert 7-8\rvert=1$ | 2 | included |
| `(1, 3)` | $\lvert 2-2\rvert=0$ | $\lvert 7-10\rvert=3$ | 0 | excluded |
| `(2, 3)` | $\lvert 4-2\rvert=2$ | $\lvert 8-10\rvert=2$ | 4 | included |

- **Explanation:** Points `2` and `3` form a rectangle of area
  $\lvert4-2\rvert\cdot\lvert8-10\rvert=4$. Points `1` and `2` form one of
  area $\lvert2-4\rvert\cdot\lvert7-8\rvert=2$. Points `1` and `3` share an
  $x$-coordinate, so their area is zero and that pair is invalid.
