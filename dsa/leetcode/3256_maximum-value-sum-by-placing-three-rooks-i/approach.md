## General

Three non-attacking rooks must occupy three distinct rows and three distinct columns. If their rows are sorted, one rook is in a middle row, one is somewhere above it, and one is somewhere below it. The solution enumerates the exact cell of the middle rook and summarizes the best choices available on each side.

For every row boundary, `prefix[r]` stores the three greatest values obtainable in distinct columns using any row from zero through `r`. A stored pair is `(value,column)`. Similarly, `suffix[r]` stores the three greatest column maxima using rows `r` through the bottom.

The helper `build_summaries` maintains `best_by_column[c]`, the maximum value seen so far in column `c` as rows are processed in the supplied order. After incorporating one row, `heapq.nlargest(3, ...)` selects the three best `(value,column)` pairs across all columns. Processing rows forward builds prefixes; processing them in reverse builds suffixes.

Only the value and column are needed in a side summary. The row that produced a prefix value is guaranteed to lie above the chosen middle row when `prefix[middle_row - 1]` is used. Only one upper rook is selected, so its exact upper row cannot conflict with another upper choice. The same reasoning holds below.

The main loop chooses `middle_row` strictly between the first and last rows, then enumerates every `middle_column`. It tries at most three upper summary candidates and at most three lower candidates. It rejects an upper candidate sharing the middle column and rejects a lower candidate sharing either already chosen column. Row conflicts are impossible because the three candidates come from disjoint row regions.

**Why keeping only three columns on each side is sufficient.** For a fixed middle and lower choice, the upper rook must avoid at most two columns: the middle column and the lower column. Among the three highest upper column maxima, at least one column is not among those two forbidden columns. If an alleged optimal upper value came from a column outside the top three, that available top-three candidate would be at least as valuable and could replace it. The same argument applies symmetrically to the lower side.

The loops explicitly combine all top-three upper and lower candidates, so they discover a pair of compatible representatives for an optimal placement. Keeping only two would be unsafe because both could be blocked by the middle and opposite-side columns.

Every legal placement has three ordered row positions. When the loop reaches its median row and exact middle cell, its upper rook is represented by that column's best prefix value or by an equal-or-better compatible top-three alternative. Its lower rook has the analogous suffix representation. Thus the algorithm considers a placement with value at least the optimum; because every considered combination is itself legal, it cannot exceed the true optimum. Equality follows.

Negative board values require placing rooks anyway. Initializing `answer` and column maxima to negative infinity prevents an implicit zero from being treated as a selectable value. Since both dimensions are at least three, a valid triple always exists and eventually replaces `answer` with an integer sum.

For a three-row board, the only possible middle row is one. The prefix comes solely from row zero and the suffix solely from row two, reducing the enumeration to choosing three distinct columns across the rows. For taller boards, column maxima allow the upper and lower choices to come from any appropriate row.

## Complexity detail

Let the board have $m$ rows and $n$ columns. Each prefix or suffix step scans $n$ cells to update column maxima and scans $n$ column pairs through `nlargest(3)`. Because the requested heap size is the constant three, this is $O(n)$ per row and $O(mn)$ total for both directions.

The main enumeration performs at most nine upper/lower combinations for each of $O(mn)$ middle cells, so it is also $O(mn)$. Total time is $O(mn)$.

Each summary stores at most three pairs for each of $m$ rows, while `best_by_column` stores $n$ values. Prefix and suffix together use $O(m+n)$ space, apart from the board. Constant-size candidate loops add no asymptotic storage.

## Alternatives and edge cases

- **Enumerate all triples of cells:** Direct search has roughly $O(m^3n^3)$ combinations and is unnecessary.
- **Enumerate three rows and columns:** Even reducing to row and column permutations remains much slower than linear in the board size.
- **Dynamic programming over selected columns:** General rook-placement DP can track masks only when the column count is small; here it can reach one hundred.
- **Keep top two side columns:** Two can both conflict with the other two rooks. Top three is the smallest universally safe summary.
- **All values negative:** The algorithm still selects the least harmful legal triple because negative infinity, not zero, initializes the optimum.
- **Equal values:** Tuple ordering may choose particular columns among ties, but retaining any top three tied columns is sufficient and compatibility checks remain exact.
- **Exactly three columns:** Every placement must use all columns. The nested exclusions find the only compatible column permutations.
- **Exactly three rows:** Each rook uses one row, and prefix/suffix boundaries ensure this automatically.
- **Best cells share a column:** The compatibility tests skip attacks and choose the best legal alternatives from the top-three summaries.
- **Middle row enumeration:** The first and last rows cannot be the median of three distinct rook rows, so excluding them loses no placement.
