## General

**A rectangle is determined by two rows and two columns**

An axis-aligned corner rectangle exists when some pair of columns contains a one in both of two different rows. The cells inside the rectangle do not matter.

The exact solution processes rows from top to bottom. For every row, it enumerates every pair of columns `(i, j)` whose two cells are one. The counter `cnt[(i, j)]` records how many earlier rows also had ones in both of those columns.

**Why the counter directly gives new rectangles**

Suppose the current row has ones at columns `i` and `j`, and `cnt[(i, j)] = r`. Each of those `r` earlier rows can be paired with the current row:

- The earlier row supplies the two upper corners.
- The current row supplies the two lower corners.
- Columns `i` and `j` are distinct because the inner loop uses `j > i`.
- The rows are distinct because only earlier rows are counted.

Therefore the current column pair creates exactly `r` new rectangles. The solution adds that count to `ans` and then increments the counter so the current row can serve as an earlier row for future rectangles.

**Enumerate only pairs that are actually present**

For each row, the outer column loop proceeds only when `c1` is one. The inner loop checks later columns and acts only when `row[j]` is also one.

If a row has `q` ones, it contributes `q(q - 1) / 2` useful column pairs. A row with fewer than two ones contributes none.

**Why every rectangle is counted exactly once**

Take any valid rectangle. It has a unique lower row and a unique ordered pair of left and right columns. When the algorithm processes that lower row, its upper row has already incremented the matching column-pair counter, so the rectangle is added.

It cannot be counted at an earlier row because its lower row was not yet processed, and it cannot be counted again later because a later lower row would define a different rectangle. The restriction `i < j` also prevents reversing the same columns.

**Trace a full three-by-three grid**

Every row has ones in all three columns, so each row contains column pairs `(0, 1)`, `(0, 2)`, and `(1, 2)`.

- The first row sees counter zero for every pair and adds no rectangles.
- The second row sees one earlier row for each of three pairs and adds three.
- The third row sees two earlier rows for each pair and adds six.

The total is nine, matching three choices of two rows times three choices of two columns.

**Why interior values do not enter the algorithm**

Only the four corners are constrained. There is no requirement for horizontal or vertical edges to contain ones and no requirement about cells inside the rectangle. Recording only shared one-column pairs between rows captures exactly the definition.

This also means rectangles of different widths and heights need no separate handling. A column pair determines the width, and combining its current occurrence with each earlier occurrence chooses every possible height automatically.

**The maintained invariant**

Before processing a row, `cnt[(i, j)]` equals the number of previously processed rows with ones in both columns. Adding it counts every rectangle whose bottom corners are the current pair. Incrementing afterward restores the invariant for the next row.

The invariant begins true because the counter defaults to zero before any row. Induction across rows proves the final total is exact.

## Complexity detail

Let `m` be the number of rows and `n` the number of columns. The exact source potentially examines every ordered pair `i < j` in every row, so its worst-case time is `O(mn^2)`.

The counter can contain every pair of columns, requiring `O(n^2)` space.

A common symmetric optimization transposes or changes orientation so pairs are formed along the smaller dimension, yielding `O(mn min(m, n))` time and `O(min(m, n)^2)` space. That optimization is not present in this exact row/column implementation, which always pairs columns.

## Alternatives and edge cases

- **Transpose when rows are fewer than columns:** Pair row indices while scanning columns, reducing the squared dimension and achieving the tighter symmetric bound.

- **Choose row pairs first:** Count shared one-columns for each row pair, then add `q(q - 1) / 2`. This is equivalent but may square the larger dimension.

- **Enumerate four corners directly:** Four nested index loops are straightforward but cost `O(m^2n^2)`.

- **Count only adjacent columns or rows:** Rectangles may have any positive width and height; adjacency is not required.

- **One row or one column:** No four distinct corners exist, and the counter logic returns zero.

- **Dense grid:** The algorithm counts combinatorial choices without constructing rectangle objects.

- **Repeated column pair across many rows:** If it has appeared `r` times, the next occurrence creates `r` new choices of upper row.

- **Interior zeroes:** They are irrelevant because only corner cells must equal one.
