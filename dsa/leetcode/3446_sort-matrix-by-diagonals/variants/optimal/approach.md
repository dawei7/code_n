## General

**Every relevant diagonal runs down and right.** Cells on one main-direction diagonal have constant `row - column`. The matrix splits into:

- the main diagonal and diagonals starting on the left edge below it, which belong to the bottom-left triangle and must be non-increasing from top-left to bottom-right;
- diagonals starting on the top edge to the right, which belong to the top-right triangle and must be non-decreasing in that direction.

Single-cell corner diagonals already satisfy either order and need not be processed.

**Process bottom-left diagonals.** The first outer loop chooses starting rows `k` on column zero, from `n - 2` down through zero. Starting at `(k,0)` and incrementing both indices extracts the complete diagonal into `t`.

After `t.sort()`, values are ascending. The write-back traversal again moves down-right, but `t.pop()` removes the largest remaining value. Therefore, the earliest cell receives the largest value, the next receives the next largest, and the diagonal becomes non-increasing.

Including `k = 0` processes the main diagonal. Excluding `k = n - 1` skips the one-cell bottom-left corner diagonal.

**Process top-right diagonals from the opposite end.** The second loop's start `(k,n-1)` lies on the right edge, and its traversal decrements both row and column indices. This walks a top-right diagonal from its bottom-right end toward its top-left end.

The loop values `k = n-2,\ldots,1` cover every top-right diagonal of length at least two. The singleton top-right corner is omitted.

Again `t` is sorted ascending and largest values are popped first. Because write-back travels from bottom-right toward top-left, the larger values go nearer the bottom-right. Reading the finished diagonal in the conventional top-left-to-bottom-right direction therefore gives non-decreasing order.

For the sample diagonal containing `[7,2]` from top-left to bottom-right, extraction in reverse sees `[2,7]`, sorting and popping writes $7$ at the bottom-right and $2$ at the top-left, producing `[2,7]` as required.

**Why the two loop families neither overlap nor miss cells.** Every down-right diagonal intersects exactly one of these boundary sets: column zero if `row >= column`, or row zero if `column > row`. The first family includes the main diagonal; the second strictly excludes it. The source parameterizes the second family through equivalent right-edge starting points rather than top-edge points, but follows the same cells in reverse.

Each diagonal is extracted before its own values are changed and shares no cell with another diagonal. Sorting one cannot affect the multiset or order requirement of another.

The method changes `grid` in place and returns the same outer list. Temporary lists contain only one diagonal at a time.

The unusual outer-loop order—from larger `k` toward smaller `k`—does not affect correctness because diagonals are disjoint. It simply processes shorter boundary diagonals before longer ones. Likewise, extracting the upper-right family from the right edge avoids a separate formula for top-row starting columns. For each omitted boundary case, the corresponding diagonal has length one and is already sorted by definition.
Sorting preserves each diagonal's multiset. The pop direction establishes the exact required monotonic order for that triangle. Since all cells belong to one processed or trivial singleton diagonal and diagonal requirements are independent, the entire returned matrix satisfies the specification.

Negative values and duplicates require no special cases. Python's numeric sort orders negatives normally, and equal adjacent diagonal values satisfy both non-increasing and non-decreasing relations.

## Complexity detail

There are $2n-1$ diagonals and $n^2$ total cells. A diagonal of length $d$ costs $O(d\log d)$ to sort. Since $d\le n$,

$$
\sum O(d\log d)\le O(n^2\log n).
$$

Extraction and write-back total $O(n^2)$ and do not change the bound.

The largest temporary `t` has length $n$. Sort workspace is also bounded by the diagonal length, so auxiliary space is $O(n)$, matching the manifest.

## Alternatives and edge cases

- **Group cells by `row - column`:** A dictionary of all diagonals is simpler conceptually but stores $O(n^2)$ values at once. This source reuses one $O(n)$ list.
- **Use the same write direction for both triangles:** It would sort both the same way. The reversed top-right traversal is what changes the effective order.
- **Main diagonal:** It belongs to the bottom-left group and is processed by `k = 0` in the first loop.
- **Singleton diagonals:** They are skipped because sorting cannot change them.
- **\(n=1\):** Both ranges are empty, and the original one-cell grid is returned.
- **Duplicate values:** Popping equal entries in any order yields the same valid diagonal.
- **Input mutation:** Callers observe the sorted cells in the original grid object.
- **Square-matrix assumption:** Both bounds use the same `n`, relying on the stated square shape.
- **Top-right indexing:** Starting on the right edge and moving up-left is equivalent to starting on the top edge and moving down-right.
- **Pop cost:** Popping from the end of a Python list is $O(1)$; popping from the front would add avoidable shifting.
