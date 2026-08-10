## General

**Convert each one into a vertical height**

Column rearrangement can place chosen columns beside one another, but it cannot change the vertical order of cells within a column. For a rectangle whose bottom lies on row `i`, the important value for each column is how many consecutive ones end at that row.

The source converts `matrix[i][j]` into that height. Starting with row one, if the current cell is one, it sets

`matrix[i][j] = matrix[i - 1][j] + 1`.

If the current cell is zero, it remains zero and resets the vertical streak. Row zero already contains correct heights of zero or one.

**Complete all heights before rearranging any row**

The height-construction loops finish for the entire matrix before the later sorting loop begins. This phase separation is essential.

When computing row `i`, `matrix[i-1][j]` still refers to the same original column `j`. If an earlier row had already been sorted, its values would no longer align with the current row's columns and height accumulation would be wrong.

Only after every vertical streak has been calculated does the source reorder rows for area evaluation.

**Interpret one height row**

Fix a bottom row. A column with height $h$ can support an all-one rectangle of any height at most $h$ ending on this row.

If we choose $w$ columns, the maximum common rectangle height is the smallest height among those columns. Because columns may be globally rearranged, any chosen set of columns can be moved next to one another while preserving each column's vertical streak.

Thus the best width-$w$ rectangle uses the $w$ largest heights.

**Sort heights from largest to smallest**

`row.sort(reverse=True)` rearranges the current height row in descending order. After sorting,

$$
\texttt{row}[0]\ge\texttt{row}[1]\ge\cdots.
$$

At one-based position `j` with value `v`, the first `j` heights are all at least `v`. They can form a rectangle of width `j` and height `v`, with area `j*v`.

The loop `for j, v in enumerate(row, 1)` evaluates exactly these candidate widths and updates `ans = max(ans, j * v)`.

**Why checking each sorted position is exhaustive**

Consider any all-one rectangle ending at this row after some column rearrangement. Let its width be $w$ and height be $h$. It uses $w$ columns whose heights are at least $h$.

The $w$-th largest height is therefore at least $h$. The source's width-$w$ candidate has area

$$
w\cdot\text{(the $w$-th largest height)}
\ge w h.
$$

So no possible rectangle at this bottom row beats all sorted candidates. Conversely, each candidate is realizable by placing its first `j` columns together. The maximum evaluated area is exact.

Taking the maximum across every bottom row covers every possible vertical placement, since every rectangle has one bottom row.

**Trace the first example**

For

`[[0,0,1],[1,1,1],[1,0,1]]`,

the vertical height rows become `[0,0,1]`, `[1,1,2]`, and `[2,0,3]` before sorting.

The last row sorts to `[3,2,0]`. Candidate areas are three times one, two times two, and zero times three: three, four, and zero. The width-two, height-two rectangle gives area four.

**Why independent row sorting is conceptually valid**

The source sorts each stored height row differently, even though one physical matrix rearrangement must use one column order. This is still correct because it is evaluating separate candidate rectangles.

For whichever candidate wins, choose the corresponding bottom row and move exactly its selected columns together in the actual matrix. Other rows' hypothetical sort orders are irrelevant. The algorithm needs prove existence of one optimal rearrangement, not construct a single order that simultaneously realizes every examined candidate.

**Input mutation has two roles**

First, binary cells are replaced by heights. Second, each height row is sorted in place. The returned answer is correct, but callers cannot expect the original binary matrix afterward.

This reuse avoids allocating a separate $m\times n$ height matrix.

## Complexity detail

Let $m$ be the number of rows and $n$ the number of columns. Height accumulation touches every cell in $O(mn)$ time. Sorting each of $m$ rows costs $O(n\log n)$, and scanning areas costs another $O(mn)$.

The exact total is therefore

$$
O(mn\log n),
$$

not the manifest's stated $O(mn)$. The editorial's separate no-sort method can achieve linear time, but this `solution.py` explicitly calls `sort` for every row.

Heights are stored by overwriting the input. Python's in-place Timsort may use $O(n)$ temporary space for one row; scalar state is constant. Auxiliary space is $O(n)$ at peak, matching the manifest if input storage is excluded. The mutated matrix itself occupies $O(mn)$ as it did on input.

## Alternatives and edge cases

- **Maintain sorted height-column pairs:** Extend prior heights while preserving order and append new height-one columns, achieving $O(mn)$ time and $O(n)$ space.
- **Counting sort heights:** Heights range from zero to $m$, so frequency counting per row can replace comparison sorting when dimensions make it attractive.
- **Copy each row before sorting:** It preserves height-column alignment for later accumulation only if done during a one-pass variant, at the cost of $O(n)$ storage.
- **All zeros:** Every height and area is zero.
- **Single row:** Heights are the bits; sorting groups all ones and returns their count.
- **Single column:** Rearrangement has no effect, and the answer is the longest vertical run of ones.
- **Zero cell:** It resets that column's height to zero.
- **Several equal heights:** Any order among them yields the same width-area candidates.
- **Sort after accumulation:** Sorting earlier would corrupt column correspondence for the next row.
- **Global column operation:** Selecting and grouping the winning row's columns realizes its candidate even though other rows were hypothetically sorted differently.
- **Input mutation:** Both binary values and original column ordering are destroyed.
- **Area bound:** `j*v` never exceeds $mn$, the total number of cells.
