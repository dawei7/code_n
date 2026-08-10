## General

A black pixel at coordinate `(i, j)` is lonely only when three conditions all hold:

- the cell itself is `"B"`;
- row `i` contains exactly one black pixel;
- column `j` contains exactly one black pixel.

The solution separates counting from classification. The first pass learns every row and column total. The second pass uses those totals to decide which black cells are lonely.

Let `R = len(picture)` and `C = len(picture[0])`. Array `rows` has one counter per row, and `cols` has one counter per column. Both begin filled with zeroes.

**First pass: count black pixels along both dimensions.** The outer loop uses `enumerate(picture)` to obtain row index `i` and the row itself. The inner loop uses `enumerate(row)` to obtain column index `j` and cell value `x`.

Whenever `x == "B"`:

`rows[i] += 1`

records one more black pixel in that row, and:

`cols[j] += 1`

records the same pixel in its column.

Each black cell contributes once to exactly one row counter and once to exactly one column counter. White cells contribute nothing. After the pass, `rows[i]` is the exact number of black cells in row `i`, and `cols[j]` is the exact number in column `j`.

For picture:

`[["W", "W", "B"], ["W", "B", "W"], ["B", "W", "W"]]`,

every row count is one and every column count is one. This does not yet count answers; it establishes the facts needed to classify each black coordinate.

**Second pass: require all three conditions.** The code scans the matrix again. At `(i, j)`, it increments `ans` only if:

`x == "B" and rows[i] == 1 and cols[j] == 1`.

Checking the cell itself matters. A white cell can lie at the intersection of a row containing one black pixel elsewhere and a column containing one black pixel elsewhere. Such an intersection is not a black lonely pixel and must not be counted.

If the current black pixel's row count is one, there is no other black pixel to its left or right in that row. If its column count is one, there is no other black pixel above or below it in that column. Together with `x == "B"`, these statements exactly match the definition.

In the diagonal three-by-three example, all three black cells pass and `ans` becomes three.

In a dense block of black pixels, row and column counts exceed one. Every black cell fails at least one uniqueness condition, so the result stays zero.

Consider:

`[["B", "W"], ["W", "B"], ["W", "B"]]`.

The black pixel at row zero, column zero has row count one and column count one, so it is lonely. The two black pixels in column one each have a row count of one but share a column count of two, so neither is lonely. This illustrates why row uniqueness alone is insufficient.

**Why two passes are natural.** When the first cell of a row is encountered, the algorithm does not yet know whether a later cell in that row or column will also be black. Counting first ensures every classification uses complete totals. It avoids rescanning an entire row and column separately for every black pixel.

**Why every increment is correct.** The condition proves the current coordinate is black and is the sole black coordinate in both its row and column. Therefore every counted pixel is lonely.

**Why every lonely pixel is incremented.** A genuinely lonely black pixel contributes one to its row total and one to its column total during the first pass, with no other black contributions in either dimension. During the second pass, its cell is `"B"` and both stored counts equal one, so the condition succeeds exactly once.

No pixel can be counted twice because the second traversal visits each coordinate once. The answer is a count of coordinates, not of distinct row or column labels.

The method reads but does not modify `picture`. This is useful because the input remains available in its original form during both passes, and the count arrays clearly separate metadata from cell contents.

The nonempty rectangular-matrix guarantee makes `picture[0]` safe and ensures every row has the same number of columns addressed by `cols`.

## Complexity detail

Let $R$ be the number of rows and $C$ the number of columns. Each pass visits all $RC$ cells and performs constant work per cell. Two such passes still give $O(RC)$ time.

The row counter array uses $O(R)$ integers and the column counter array uses $O(C)$, for $O(R+C)$ auxiliary space, matching the manifest. The scalar answer and loop variables use $O(1)$ additional space.

The returned count needs at most $RC$, which is safely represented by Python's integer type.

## Alternatives and edge cases

- **Scan a row and column for every black pixel:** It uses constant extra storage but can take $O(RC(R+C))$ time in a dense picture.
- **Store black coordinates:** Counting only recorded coordinates can avoid a second full matrix scan, but the coordinate list may use $O(RC)$ space.
- **Modify the first row and column as counters:** It can reduce auxiliary space to $O(1)$ but complicates boundary handling and mutates the input.
- **Single black pixel:** Its row and column counts are both one, so the result is one.
- **All white pixels:** Every counter remains zero and no second-pass cell satisfies `x == "B"`.
- **One row:** A black pixel is lonely only if that row contains exactly one black pixel; its column then automatically contains one.
- **One column:** The symmetric rule applies using the column total and individual row totals.
- **White intersection of unique counts:** The explicit black-cell test prevents a false positive.
- **Two black pixels in one row:** Both fail the row-count condition even if their columns are otherwise empty.
- **Two black pixels in one column:** Both fail the column-count condition.
- **Several isolated diagonal pixels:** Each may be counted because loneliness is based on shared rows and columns, not diagonal adjacency.
- **Rectangular shape:** Separate row and column array lengths support non-square pictures directly.
