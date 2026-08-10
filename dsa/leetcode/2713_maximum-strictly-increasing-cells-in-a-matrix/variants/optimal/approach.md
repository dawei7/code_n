## General

**Process cells in increasing value order**

A legal move always goes to a strictly larger value in the same row or column.

This makes cell values a topological order: when processing a value $v$, every legal predecessor has value less than $v$ and can already have a finalized best path length.

The solution groups all coordinates by value in dictionary `g` and iterates `sorted(g.items())`.

**Store the best processed path per row and column**

`rowMax[i]` is the maximum number of cells in a valid increasing path ending at any already processed cell in row $i$.

`colMax[j]` has the analogous meaning for column $j$.

Only these maxima are needed. From cell `(i, j)`, a predecessor may be any smaller cell in its row or column, so the best predecessor length is `max(rowMax[i], colMax[j])`.

**Compute the current cell's DP value**

For position `(i, j)` with current grouped value:

`1 + max(rowMax[i], colMax[j])`

is the longest path ending there.

The one counts the current cell. If no smaller predecessor exists in either line, both maxima are zero and the cell correctly starts a path of length one.

The computed values are stored temporarily in list `mx`.

**Why equal-valued cells must be batched**

Moves require a strictly greater destination, so two cells with equal value cannot follow one another.

If row or column maxima were updated immediately for the first coordinate of value $v$, a later equal-valued coordinate in the same row or column could incorrectly use it as a predecessor.

The solution therefore has two phases for each value:

1. compute every `mx` using only summaries from smaller values;
2. update row and column summaries after all equal cells have been evaluated.

This batching enforces strictness.

**Trace an all-equal matrix**

Every coordinate belongs to the same value group.

During the computation phase, all row and column maxima are zero, so every `mx` is one.

Only afterward are summaries updated. No equal cell sees another, and the answer remains one as required.

**Trace a simple increasing move**

In matrix `[[3,1],[3,4]]`, value one is processed first and receives path length one.

Its row and column summaries are updated. When value three or four is processed, cells sharing a row or column with a smaller processed cell can extend that length.

Value four can obtain length two, while equal threes are evaluated together and cannot chain through each other.

**Why row and column maxima are sufficient**

Suppose several smaller cells occur in row $i$. A move into current cell cares only which predecessor provides the longest valid path.

All other predecessor details are irrelevant to maximizing length. The same holds for column $j$.

Taking the larger of the two line summaries considers the best legal predecessor from either direction without enumerating every cell in those lines.

**The invariant after each value group**

After finishing all coordinates with values up to $v$:

- every processed cell's DP value is correct;
- each `rowMax` and `colMax` is the greatest such DP value in that line;
- no unprocessed larger value has influenced the summaries.

The computation phase uses this invariant to derive exact current lengths. The delayed update phase extends it to include value $v$.

**Track the global answer**

Each newly computed path length is compared with `ans` immediately.

Every valid path ends at some cell, and that cell's DP value is evaluated in its value group. The maximum over all cell-ending values is therefore the maximum number of cells visitable from some start.


Induct on distinct values in ascending order. Every legal predecessor of a current cell has smaller value, so its optimal path is already represented in the appropriate row or column maximum.

The recurrence selects the best such predecessor or starts at length one. Batch-delayed updates prevent illegal equal-value predecessors. Hence every cell DP is exact.

Taking the maximum across exact cell-ending lengths returns the optimal path length.

**No explicit graph is built**

Connecting every pair in a shared row or column could create quadratically many edges.

Row and column summaries compress all smaller predecessors into $m+n$ scalar states, while value grouping supplies the correct processing order.

## Complexity detail

Let $q=mn$ be the number of cells and $u$ the number of distinct values. Building groups takes $O(q)$ time. Sorting the $u$ keys costs $O(u\log u)$, bounded by $O(q\log q)$, and both processing phases visit each cell once.

Total time is $O(q\log q)$. Coordinate groups and temporary DP values use $O(q)$ space, while row and column summaries use $O(m+n)$. Overall space is $O(q)$.

## Alternatives and edge cases

- **Explicit DAG edges:** Correct but can require quadratic edges within dense rows or columns.
- **Sort individual cells instead of groups:** Works only if equal-value updates are delayed as a batch.
- **DFS with memoization:** Needs an efficient way to find greater row/column neighbors and can recreate dense work.
- **One cell:** Its path length is one.
- **All values equal:** No strict move exists, so answer is one.
- **Negative values:** Sorting handles them naturally; only relative order matters.
- **Duplicate value in one row:** Equal cells cannot extend each other because of batching.
- **Best predecessor in the column:** `colMax` is considered equally with `rowMax`.
- **Start anywhere:** The added one permits every cell to start a path.
- **Strictness:** Processing equal values together is the critical safeguard.
- **Input preservation:** The matrix is read into coordinate groups and not modified.
