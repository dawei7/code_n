## General

**Turn relative order into predecessor constraints**

For a cell, every smaller original value in the same row or column must receive a smaller replacement. Because all original grid values are distinct, there are no equality groups to coordinate. If cells are processed globally from smallest original value to largest, every ordering predecessor of the current cell has already received its final score.

The smallest legal positive score for the current cell is therefore one more than the greatest score already used in its row or column. Assigning exactly that value preserves all required inequalities while keeping the current score as small as possible.

**Sort cells without losing their coordinates**

The list comprehension creates tuples `(v, i, j)` for all cells. Sorting these tuples orders primarily by `v`. Values are distinct, so coordinate tie-breaks never affect processing order.

Let $N=mn$ be the number of cells. The sorted list provides a topological-like order: when processing `(i, j)`, every cell with a smaller original value—particularly every smaller one in row `i` or column `j`—has already been handled. Larger original values have not yet influenced the score.

The solution builds a separate zero-filled matrix `ans`. It does not overwrite `grid`, so original values remain available conceptually throughout processing.

**Summarize processed constraints by row and column**

`row_max[i]` stores the greatest replacement score assigned so far to a processed cell in row `i`. Similarly, `col_max[j]` stores the greatest processed score in column `j`. Both arrays start at zero. Since replacement values must be positive, an empty row or column history then yields a first allowable score of one.

For current cell `(i, j)`, the exact assignment is:

```python
ans[i][j] = max(row_max[i], col_max[j]) + 1
```

The score must exceed `row_max[i]` to be greater than all smaller original cells in its row. It must also exceed `col_max[j]` for its column. Exceeding their maximum satisfies both requirements, and adding exactly one is the smallest positive integer that does so.

The code then updates both summaries:

```python
row_max[i] = col_max[j] = ans[i][j]
```

Because cells are processed in increasing original value and assigned a score above the previous maxima, this new score is indeed the new maximum for both its row and column.

**Trace the two-by-two example**

For `grid = [[3, 1], [2, 5]]`, sorted original values occur at:

```text
1 at (0, 1)
2 at (1, 0)
3 at (0, 0)
5 at (1, 1)
```

The cell containing `1` sees row and column maxima zero, so it receives one. The cell containing `2` is in a different row and column and also receives one. The cell containing `3` shares row zero with score one and column zero with score one, so it receives two. Finally, original `5` shares row and column histories whose maxima are one, so it receives two. The result is `[[2, 1], [1, 2]]`.

It is valid for unrelated cells to share a replacement score. The contract preserves order only for pairs in the same row or column.

**Why tracking only maxima is sufficient**

Suppose a row contains several already processed cells with scores `1, 2, 4`. The current cell must exceed all of them. Exceeding their maximum `4` automatically exceeds the rest; their individual positions and values are no longer needed. The same applies to a column.

There are no equal original values, so the current cell must be strictly above every previously processed cell in its row or column. If equal values existed, simultaneous grouping would be needed to avoid imposing an artificial order among equals. The distinctness guarantee is essential to this simple one-cell-at-a-time update.

**Why the assignment minimizes the global maximum**

Induct over cells in sorted original-value order. The first cell has no smaller row or column predecessor, and score one is the smallest positive value.

Assume all earlier cells received the smallest scores compatible with their processed constraints. For current `(i, j)`, any valid result must assign a value greater than every smaller cell in its row and column. In particular, it must be at least `max(row_max[i], col_max[j]) + 1`. The algorithm assigns exactly this lower bound, so no valid solution can assign the current cell less while retaining the earlier scores.

This componentwise minimal construction never inflates a row or column boundary unnecessarily. By induction, every assigned score is as small as constraints permit given minimal predecessors. Therefore, the largest score in `ans` is also as small as possible. Any alternative reducing that maximum would have to reduce some cell below its proven lower bound.

The result may not be unique: unrelated rows and columns can sometimes use different scores without changing the same maximum. The problem accepts any optimum, and this deterministic greedy ranking returns one.

## Complexity detail

Let $m$ and $n$ be the matrix dimensions and $N=mn$ the number of cells. Creating `nums` takes $O(N)$ time and space. Sorting its $N$ tuples takes $O(N\log N)$ time. The assignment loop takes $O(N)$ time, so sorting dominates and total time is $O(N\log N)$.

`nums` and the result matrix each use $O(N)$ space. `row_max` and `col_max` add $O(m+n)$, which is bounded by $O(N)$ for a nonempty matrix. Auxiliary storage including the constructed result is therefore $O(N)$.

## Alternatives and edge cases

- **Min-heap:** Push all value-coordinate tuples and pop them in increasing order. It has the same $O(N\log N)$ time and $O(N)$ space but sorting once is simpler.
- **Explicit dependency graph:** Add ordering edges between relevant cells and compute longest-path ranks in topological order. It is more complex, and global value sorting already supplies a valid order.
- **Equal original values:** The contract forbids them. If allowed, equal-value cells would need batch processing so same-value updates do not constrain each other.
- **Single cell:** Both maxima are zero, so the only cell receives the optimal positive score one.
- **Single row:** Scores become `1, 2, ...` in original-value order within that row, preserving every pairwise comparison.
- **Single column:** The same rank progression occurs down the column according to original values.
- **Unrelated cells:** Cells sharing neither row nor column may receive equal scores; no constraint relates them.
- **Very large original values:** Only their ordering matters. Replacement scores depend on row and column chains, not numeric gaps.
- **Input preservation:** The exact implementation returns a separate `ans` matrix and does not mutate `grid`.
- **Distinctness and tuple sorting:** Because values are unique, the coordinate fields never determine the processing order.
