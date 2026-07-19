## General
**Measure the vertical run ending at each row**

Let `heights[column]` be the number of consecutive `1`s ending at the current row in that original column. A current `1` extends the previous height by one, while a current `0` resets it to zero. If $w$ columns have heights of at least $h$, one global column permutation can place those complete columns together, creating an all-ones rectangle of height $h$ and width $w$ ending at this row.

It is valid to evaluate a different best permutation for each possible bottom row: the answer needs only one rectangle. Whichever row produces the maximum also supplies one concrete set of columns that can be moved together by a single permutation.

**Preserve descending height order without sorting again**

Maintain `order`, a list of column indices arranged by non-increasing height after the previous row. Scan those indices in that order for the current row. Put columns containing `1` into a `positive` list and increment their heights; put columns containing `0` into a `zero` list and reset their heights.

Filtering an already ordered sequence preserves the relative order of the selected positive columns. Adding one to every selected height preserves their comparisons as well. All reset columns have height zero, so `order = positive + zero` is again ordered by non-increasing height. This maintains the same information that sorting the height array would provide, using only linear work per row.

**Turn each ordered prefix into a rectangle**

Within `positive`, the height at position `width - 1` is the smallest height among the first `width` columns. Those columns can therefore form a rectangle with area `width * heights[column]`. Evaluate every positive prefix. Every feasible all-ones rectangle ending at this row corresponds to some height threshold and selected-column count, so one of these prefixes attains at least its area.

## Complexity detail
Each of the $m$ rows scans all $n$ columns once to update the stable order and at most $n$ positive columns once to evaluate areas. The total time is $O(mn)$. The height array, column order, and two temporary column lists each contain at most $n$ indices or values, so the auxiliary space is $O(n)$.

## Alternatives and edge cases
- **Sort heights on every row:** Updating vertical heights and sorting them in descending order is simpler and correct, but takes $O(mn\log n)$ time instead of preserving their order in $O(mn)$.
- **Enumerate column subsets:** Testing which columns can be made adjacent explores exponentially many subsets and ignores that only each column's current height matters.
- **All zeros:** Every height remains zero, so no positive prefix exists and the answer is zero.
- **All ones:** Heights increase on every row and all columns remain positive, yielding the entire matrix area $mn$.
- **Single row:** The answer is the number of `1`s, because all such columns can be placed together.
- **Single column:** Rearrangement has no effect; the answer is the longest vertical run of `1`s.
- **Column integrity:** Reordering cannot combine a top portion of one column with a bottom portion of another; vertical heights always belong to original complete columns.
