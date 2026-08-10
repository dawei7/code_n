## General

**Turn each row into the bottom of a histogram**

`heights[j]` stores the number of consecutive `"1"` cells in column `j` ending at the current row. When the current matrix cell is `"1"`, the vertical run from the preceding row extends by one, so the source increments the height. When the cell is `"0"`, no all-one rectangle ending at this row can pass through that column, so the height resets to zero.

After updating one complete row, `heights` is a histogram whose bars measure how far an all-one column segment reaches upward from this row. A consecutive interval of histogram bars can support a rectangle whose height is their minimum and whose width is the interval length. That histogram rectangle corresponds directly to an all-one matrix rectangle with its bottom edge at the current row.

The algorithm finds the largest histogram rectangle for every possible bottom row and retains the largest area in `ans`.

**Why considering every bottom row is complete**

Take any all-one rectangle in the matrix. It has some bottom row `r`, spans consecutive columns, and has some height `h`. When row `r` is processed, every spanned column has at least `h` consecutive ones ending there. The row's histogram therefore contains a rectangle over the same columns with height at least `h`, so the histogram solver considers an area at least as large as that matrix rectangle.

Conversely, if a histogram interval has minimum height `h`, each of its columns contains `h` consecutive ones ending at the current row. Those cells form a genuine all-one matrix rectangle. Histogram candidates cannot invent invalid matrix cells.

Thus the maximum across row histograms is exactly the maximum matrix rectangle, not merely an approximation.

**For one histogram, find the nearest strictly lower bars**

For each bar `i`, the helper wants the first position to its left with height strictly smaller than `heights[i]` and the first such position to its right. Between those boundaries, every bar is at least as tall as `heights[i]`, so a rectangle of that height can cover the entire open interval.

The width is `right[i] - left[i] - 1`, and the candidate area is the width times `heights[i]`. Sentinel defaults `-1` and `n` represent no smaller bar before the beginning or after the end.

**Build left boundaries with an increasing stack**

The first stack pass scans left to right. Before index `i` is pushed, it removes every top whose height is greater than or equal to the current height. Those bars cannot be the nearest strictly smaller boundary.

After the pops, the remaining top—if one exists—is lower than the current bar and is the nearest such lower index. Any closer index was popped because it was at least as high. The source writes that top to `left[i]`; otherwise the initialized `-1` remains. Pushing `i` restores strictly increasing stack heights.

Popping equal heights is important to the chosen boundary definition. Equal bars do not block a rectangle from extending across one another, so the boundary must be strictly lower, not merely lower-or-equal.

**Build right boundaries symmetrically**

The source clears the stack and scans indices from right to left. It again pops heights greater than or equal to the current height. The remaining top is now the nearest strictly lower index on the right, so it becomes `right[i]`. If none exists, the bar can extend to the histogram end and keeps sentinel `n`.

Using a fresh reverse pass makes the symmetry easy to verify. For an equal-height plateau such as `[2,2,2]`, equal bars are removed as blockers in both directions, and the plateau can receive boundaries outside the full run.

**Trace the matrix-to-histogram transition**

In the standard example, after processing the row `['1','1','1','1','1']` beneath prior rows, the height state becomes `[3,1,3,2,2]`. The last three columns can support height two across width three, producing area six. Those histogram bars correspond to a two-row by three-column block of ones ending at that matrix row.

A zero in a later row resets its column height and prevents subsequent bottom-row histograms from incorrectly reaching through it. Other columns can retain or extend their vertical runs independently.

**A two-level invariant**

After updating row `r`, each `heights[j]` is exactly the largest number of consecutive ones ending at `(r, j)`. This follows from incrementing on one and resetting on zero.

Within `largestRectangleArea`, each completed boundary is the nearest strictly lower bar in its direction. Therefore every calculated area is a feasible histogram rectangle, and for every possible limiting height there is a bar whose boundary interval captures its maximal width.

Combining these invariants proves that `ans` after row `r` is the largest all-one rectangle whose bottom is at or above `r`. After the final row, it is the global answer.

**Nonempty dimensions are assumed by the exact source**

The function immediately reads `matrix[0]` to size `heights`, and the helper calls `max` over histogram bars. Both are safe under the reference contract, which guarantees at least one row and one column. An empty matrix or empty row outside the contract would require an explicit guard.

## Complexity detail

Let $m$ be the number of rows and $n$ the number of columns. Updating heights costs $O(n)$ per row. Each boundary pass pushes and pops every histogram index at most once, and area evaluation is another linear pass. Therefore each row costs $O(n)$ and total time is $O(mn)$, matching the manifest.

`heights`, `left`, `right`, and the stack each use $O(n)$ storage, with boundary arrays and stack recreated inside one helper call at a time. Peak auxiliary space is $O(n)$, matching the manifest. The matrix is read without modification.

## Alternatives and edge cases

- **One-pass histogram stack:** Finalize bar areas as soon as a lower-or-equal bar appears and flush at a virtual zero. It avoids `left` and `right` arrays but still uses $O(n)$ stack space.
- **Dynamic left/right/height arrays across rows:** Update rectangle boundaries directly for each row. It also achieves $O(mn)$ time and $O(n)$ space but has more coupled state.
- **Upward scan from every cell:** Maintain horizontal widths and scan previous rows, which can take $O(m^2n)$ time.
- **All zeroes:** Every height remains zero and all candidate areas are zero.
- **All ones:** Heights increase each row, and the final full-width histogram yields area `m * n`.
- **One row:** The method reduces exactly to largest rectangle in a binary histogram.
- **One column:** Heights count the longest vertical run of ones.
- **Zero within a column:** Resetting to zero prevents rectangles from crossing it vertically.
- **Equal histogram heights:** The `>=` pop rule makes boundaries strictly lower and allows spanning the plateau.
- **Non-square matrix:** State size depends on columns and the row loop handles any positive row count.
- **String cells:** Comparisons correctly use `"1"` and `"0"`, not integers.
- **Nonempty guarantee:** Direct `matrix[0]` and nonempty `max` depend on it.
- **Input preservation:** Only derived height and boundary arrays change.
