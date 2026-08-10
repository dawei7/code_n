## General

A qualifying black pixel at `(r, c)` must satisfy two coupled rules:

- its row and column each contain exactly `target` black pixels;
- every row containing a black pixel in column `c` must be identical to row `r`.

The solution groups black pixels by column, counts black pixels per row, and then validates one whole column group at a time.

Array `rows` has one entry per picture row. Dictionary `g` maps a column index to the list of row indices where that column contains `"B"`.

**Collect row counts and black-row membership per column.** During the first complete matrix scan, every black cell `(i, j)` performs two updates:

- `rows[i] += 1` records one more black pixel in row `i`;
- `g[j].append(i)` records that row `i` has a black pixel in column `j`.

Afterward, `rows[i]` is the black count of row `i`, and `len(g[j])` is the black count of column `j`. The list `g[j]` also identifies exactly which full rows must be compared for the second rule.

Columns with no black cells do not appear in `g`. They cannot contribute qualifying black pixels, so skipping them is correct.

**Use one representative row.** For each black-containing column `j`, the solution chooses `i1 = g[j][0]`, the first row having a black pixel there. If this column can qualify, every black row in it must be identical, so any one of them can serve as the representative.

The first filter is:

`if rows[i1] != target: continue`.

If the representative row does not contain exactly `target` black pixels, its pixel in column `j` cannot satisfy the row-count rule. Under the identical-row requirement, no other black row in that column could rescue the column as a qualifying group, so it is safe to skip.

**Check the column count and row-pattern rule together.** The condition:

`len(g[j]) == rows[i1]`

compares the column's black count with the representative row count. Because the earlier filter established `rows[i1] == target`, this equality is equivalent to requiring exactly `target` black pixels in the column.

The second part:

`all(picture[i2] == picture[i1] for i2 in g[j])`

compares every row containing a black pixel in column `j` with the representative row. Python list equality checks the complete sequence of `"B"` and `"W"` cells, so this enforces exact row identity, not merely equal black counts.

Only when both checks pass does column `j` satisfy the full rule.

**Why the answer increases by `target`.** A valid column has exactly `target` black pixels, one at each row index in `g[j]`. All those rows are identical to the representative and each has exactly `target` black pixels. Therefore every black pixel in this column qualifies, contributing `target` coordinates at once.

The code uses `ans += target` rather than revisiting each black cell individually.

In the example, the first three rows are identical and each contains three black pixels. Columns one and three contain black pixels exactly in those three rows, so each column contributes three qualifying pixels. Column four also has an additional black pixel in a different fourth row, so its column count and identical-row condition fail. The result is six.

For `[["W","W","B"], ["W","W","B"], ["W","W","B"]]` with `target = 1`, each row has one black pixel, but the black column contains three pixels. `len(g[j])` is three while `rows[i1]` is one, so the column contributes zero.

**Why validating by column does not double-count.** Each pixel belongs to exactly one column. When a column qualifies, the method counts each of its `target` black coordinates once. A row may contribute qualifying pixels in multiple columns, which is correct because those are different coordinates.

**Why every counted pixel satisfies both rules.** A contributing column has `target` black positions. Every corresponding row equals the representative, whose row count is `target`. Thus the selected coordinate's row and column counts are correct, and all black-containing rows in its column are identical.

**Why every qualifying pixel is found.** Take a qualifying pixel in column `c`. Its row appears in `g[c]`. Every row in that list is identical and has row count `target`, so the representative passes the first filter. The column has exactly `target` black pixels, making the length equality true, and all row comparisons succeed. The method adds the whole column group, including the chosen pixel.

The matrix is read-only. Row objects can be compared directly because the input is rectangular and each row contains the complete pattern.

## Complexity detail

Let $R$ and $C$ be the matrix dimensions, and let $B$ be the number of black pixels. Building `rows` and `g` takes $O(RC)$ time and stores $B$ row indices, using $O(R+B)=O(RC)$ space.

The manifest states $O(RC)$ time, but the exact Python code may spend more in its validation phase: each `picture[i2] == picture[i1]` list comparison can inspect $C$ cells, and such comparisons occur across black-row memberships for each considered column. A tight worst-case upper bound is $O(RC+BC)$, which becomes $O(RC^2)$ when $B=RC$. Early count failures and early list mismatches often reduce actual work, but they do not change this exact worst-case distinction.

The retained auxiliary-space bound is $O(RC)$, matching the manifest.

## Alternatives and edge cases

- **Count identical row patterns with tuples:** Hash each qualifying row pattern and combine its frequency with column counts. It can make the intended $O(RC)$ time bound explicit while using $O(RC)$ space for patterns.
- **Check every black pixel independently:** Recounting its row, column, and peer rows repeats substantial work.
- **Columns with no black pixels:** They are absent from `g` and cannot contribute.
- **Representative row has wrong count:** The column is skipped immediately.
- **Column has wrong black count:** `len(g[j]) == rows[i1]` fails after the representative count is known to equal `target`.
- **Rows have equal counts but different patterns:** Full list equality rejects them.
- **One qualifying column:** It contributes exactly `target` pixels, not one.
- **One row or one column:** The same count and equality rules apply without special branches.
- **Repeated identical rows:** They are permitted and are exactly what the second rule may require.
- **Several qualifying columns in the same rows:** Each column contributes its distinct set of coordinates.
- **Rectangular guarantee:** Direct whole-row equality compares patterns of the same length.
