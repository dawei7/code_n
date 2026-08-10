## General

A vertical line crosses a brick in a row unless it lands on an internal boundary between two bricks. Therefore the best line is the internal horizontal position shared by the largest number of rows.

The solution counts internal boundary positions using prefix sums of brick widths.

For one row, variable `s` begins at zero. As each brick width `x` is processed, adding it gives the horizontal coordinate of that brick's right edge.

The loop deliberately uses `row[:-1]`, excluding the final brick. The final right edge is the outside edge of the wall, and the problem forbids drawing the line there. The left outside edge is also never counted because prefix sum zero is not inserted.

For every internal coordinate `s`, `cnt[s]` records how many rows have a brick edge there.

Brick widths may differ, but coordinates with the same numeric prefix sum align vertically. No geometric grid proportional to wall width is needed, which is important because widths may be very large.

**Convert aligned edges into crossed bricks.** Suppose an internal position appears in `g` rows. In those rows, the line follows an edge and crosses no brick. In every other row, it passes through the interior of exactly one brick.

With `R = len(wall)` rows, crossed bricks equal:

$$
R-g.
$$

To minimize crossings, maximize `g`. The return statement computes:

`len(wall) - max(cnt.values(), default=0)`.

For the example wall, the most common internal edge occurs in four of six rows, so the line crosses the remaining two bricks.

For `[[1],[1],[1]]`, every row contains one brick and has no internal edge. Counter `cnt` remains empty. The default maximum zero produces three crossed bricks, which is unavoidable because outside edges are forbidden.

**Why counting each row boundary once is sufficient.** Brick widths are positive, so prefix sums within a row strictly increase. The same coordinate cannot occur twice in one row. Each counter increment therefore corresponds to one distinct row that the line can avoid crossing.

**Why an optimal line can be chosen at a counted edge.** Between two consecutive edge coordinates across the whole wall, moving the line does not change which brick it crosses in any row. Such an interior region crosses every row lacking an edge there—indeed no row has an edge at an unrecorded coordinate. Moving onto a recorded internal edge can only reduce crossings. Thus some optimal position is among the counted coordinates unless no internal edge exists.

**Why row totals need not be used explicitly.** Equal total width guarantees all prefix coordinates share one common wall coordinate system. The algorithm trusts that source guarantee and only counts internal sums.

The Counter stores positions, not brick indices. Two edges after different numbers of bricks can still align if their accumulated widths match.

The input wall is not modified. Row slicing creates the view-like copied prefix list in Python, while the widths themselves remain unchanged.

Consider two rows `[2, 1, 3]` and `[1, 2, 3]`. Their first edges differ, at coordinates two and one, but both have a second internal edge at coordinate three. Counter key three receives two increments even though the boundary follows a different brick index history in each row. A line there crosses neither row. This example shows why cumulative position, rather than brick number or individual width, is the correct grouping key.

Conversely, equal brick widths do not imply aligned edges. A width-two brick beginning at coordinate one ends at three, while another width-two brick beginning at coordinate four ends at six. Only their prefix sums decide whether one vertical line can use both edges.

## Complexity detail

Let $B$ be the total number of bricks across all rows. Every brick except the final brick of each row is processed once. Time is $O(B)$.

There can be at most $B$ distinct internal edge coordinates, so the Counter uses $O(B)$ space, matching the manifest. Scalar prefix sums use constant additional storage.

Integer prefix coordinates may exceed a single brick width; Python integers safely represent their sums.

The slice `row[:-1]` allocates a temporary list per row in this exact Python implementation. Across rows, the total number of copied references is still $O(B)$, and only one row slice is live during its loop, so it does not change the stated asymptotic bounds.

## Alternatives and edge cases

- **Test every possible coordinate against every row:** This repeats row scans and can become quadratic in the number of bricks.
- **Use physical-width buckets:** Wall width may be enormous, so allocating one slot per coordinate is unsafe.
- **Count the final edge:** It would always appear in every row and incorrectly return zero, despite the forbidden outside boundary.
- **Count the left edge:** Coordinate zero is also forbidden and intentionally absent.
- **One brick per row:** No internal edge exists, so every row is crossed.
- **All rows share an internal edge:** The answer is zero because that position is legal.
- **Different brick counts:** Only accumulated widths determine alignment.
- **Large widths:** Hashing prefix coordinates avoids dependence on total wall width.
- **Several equally common edges:** Any gives the same minimum; only the count is returned.
- **Positive widths:** They ensure strictly increasing boundaries within each row.
