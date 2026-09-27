# Guided Example: Maximum Sum of an Hourglass

## 1. The shape and the instance

An **hourglass** is a seven-cell figure that occupies a full $3 \times 3$ bounding
box but omits the two middle-row side cells. It cannot be rotated, and it must lie
entirely inside the matrix. We trace the four-by-four grid whose four rows are
`[6, 2, 1, 3]`, `[4, 2, 1, 5]`, `[9, 2, 8, 7]` and `[4, 1, 2, 9]`, so $m = 4$ and
$n = 4$. Its required answer is `30`.

## 2. Anchors: one integer pair per hourglass

Every hourglass has exactly one cell in its middle row, and call that cell the
**anchor** `grid[i][j]`. The figure then needs one row above and below the anchor,
and one column to the left and right, so a fully contained hourglass exists at
anchor $(i, j)$ exactly when

$$
1 \le i \le m - 2, \qquad 1 \le j \le n - 2 .
$$

Because the mapping from placement to anchor is a bijection, enumerating anchors
enumerates placements — each exactly once, with no duplicates and no omissions.
For the four-by-four grid there are $m - 2 = 2$ valid rows and $n - 2 = 2$ valid
columns, so four anchors: $(1,1)$, $(1,2)$, $(2,1)$, $(2,2)$.

| | col 0 | col 1 | col 2 | col 3 |
|---|---|---|---|---|
| **row 0** | 6 | 2 | 1 | 3 |
| **row 1** | 4 | **2** | 1 | 5 |
| **row 2** | 9 | 2 | 8 | 7 |
| **row 3** | 4 | 1 | 2 | 9 |

The bold `2` at row 1, column 1 is the first anchor. Row 0, row 3, column 0 and
column 3 are *not* excluded from the matrix — they may contain hourglass cells —
but they can never hold an anchor, because an anchor needs a full ring of
neighbours around it.

## 3. The fixed mask and the "square minus two" identity

Relative to the anchor, the seven included offsets are the whole $3 \times 3$
block apart from the two horizontal neighbours of the anchor. That mask is fixed
by the definition, which is what "cannot be rotated" means concretely: the
excluded cells are always the ones sharing the anchor's row, never the ones
sharing its column.

| Offset $(di, dj)$ | Cell | In the hourglass? |
|---|---|---|
| $(-1, -1), (-1, 0), (-1, 1)$ | top row of the box | yes, all three |
| $(0, -1)$ | left neighbour of the anchor | no |
| $(0, 0)$ | the anchor | yes |
| $(0, 1)$ | right neighbour of the anchor | no |
| $(1, -1), (1, 0), (1, 1)$ | bottom row of the box | yes, all three |

This gives a convenient way to evaluate a placement: add all **nine** cells of the
bounding box, then subtract the two cells that do not belong.

$$
\text{hourglass}(i, j)
= \Bigl(\sum_{di=-1}^{1} \sum_{dj=-1}^{1} \texttt{grid}[i+di][j+dj]\Bigr)
- \texttt{grid}[i][j-1] - \texttt{grid}[i][j+1] .
$$

The two excluded cells appear once positively and once negatively, so they cancel
exactly. The identity is an algebraic rearrangement, not an approximation: reading
a rectangular block is cheaper to describe, and the subtraction removes precisely
the two unwanted readings.

## 4. Worked trace of the four anchors

Each row below is a complete placement evaluation. The "box total" column is the
sum of all nine cells of the $3 \times 3$ bounding box, and the "excluded" column
names the two cells the mask removes.

| Anchor $(i, j)$ | Box rows, columns | Box total | Excluded cells | Hourglass sum | Running maximum |
|---|---|---|---|---|---|
| $(1, 1)$ | rows 0–2, cols 0–2 | 35 | `grid[1][0] = 4`, `grid[1][2] = 1` | $35 - 4 - 1 = 30$ | 30 |
| $(1, 2)$ | rows 0–2, cols 1–3 | 31 | `grid[1][1] = 2`, `grid[1][3] = 5` | $31 - 2 - 5 = 24$ | 30 |
| $(2, 1)$ | rows 1–3, cols 0–2 | 33 | `grid[2][0] = 9`, `grid[2][2] = 8` | $33 - 9 - 8 = 16$ | 30 |
| $(2, 2)$ | rows 1–3, cols 1–3 | 37 | `grid[2][1] = 2`, `grid[2][3] = 7` | $37 - 2 - 7 = 28$ | 30 |

The maximum over the four placements is **30**, achieved at anchor $(1,1)$, whose
seven cells are $6, 2, 1$ in row 0, the anchor $2$ in row 1, and $9, 2, 8$ in
row 2:

$$
6 + 2 + 1 + 2 + 9 + 2 + 8 = 30 .
$$

Two features of this trace matter. First, the largest *box* total (37, at anchor
$(2,2)$) does **not** produce the largest hourglass, because that box hides the
large values $2$ and $7$ in positions the mask discards. Second, the leftovers
$9$ and $8$ at row 2 are the largest values in the grid, and they are dropped by
every placement whose anchor sits in row 2; only anchors in row 1 can reach them.

The second official instance makes the anchor count obvious: for the $3 \times 3$
grid $[[1,2,3],[4,5,6],[7,8,9]]$ the ranges $1 \le i \le 1$ and $1 \le j \le 1$
admit exactly one anchor, whose box totals 45 and whose excluded cells are 4 and
6, giving $45 - 4 - 6 = 35$.

## 5. Why the reasoning is correct

**Invariant of the accumulator.** Process anchors in row-major order and keep a
single running maximum. After every processed anchor, the running maximum equals
the largest hourglass sum over the anchors visited so far. It starts at `0`; the
initial value is safe because every matrix entry is non-negative, so every
hourglass sum is non-negative and the supremum over an empty set cannot
accidentally become the answer. Each step replaces the running value by
$\max(\text{running}, \text{hourglass}(i,j))$, which preserves the invariant by
construction.

**Soundness of one evaluation.** For a fixed anchor, the nine-cell sum includes
every hourglass cell exactly once (they all lie in the bounding box) and the two
excluded cells exactly once. Subtracting each excluded cell once leaves the seven
hourglass cells with coefficient 1 and every other cell with coefficient 0. The
computed value is therefore exactly the hourglass sum, never an over- or
under-count.

**Completeness.** The loops over $1 \le i \le m-2$ and $1 \le j \le n-2$ visit every
legal anchor exactly once. Since anchors and placements are in bijection, every
hourglass in the matrix is evaluated. When both loops finish, the invariant's
"anchors visited so far" is the whole set, so the running maximum is the global
maximum — the value to return.

**Boundary safety.** Every read uses offsets in $\{-1, 0, 1\}$ from an anchor that
satisfies $1 \le i \le m-2$ and $1 \le j \le n-2$, so the row indices stay in
$[0, m-1]$ and the column indices in $[0, n-1]$. No placement is ever evaluated
partially outside the matrix.

## 6. Boundary conditions this instance family exposes

| Situation | Instance | Answer | Reason |
|---|---|---|---|
| Minimum square grid | `[[1,2,3],[4,5,6],[7,8,9]]` | 35 | Exactly one anchor exists; the loops admit index 1 only. |
| Large cells deliberately excluded | `[[1,1,1],[100,2,100],[1,1,1]]` | 8 | The two middle side cells are absent from the shape, so 100 and 100 do not count; the box total 208 minus 200 gives 8. |
| All zeros | any all-zero $3 \times 3$ grid | 0 | Every hourglass sums to zero, and the accumulator's starting value is already correct. |
| Three rows, five columns | `[[9,0,1,2,3],[1,8,1,8,1],[7,0,6,0,5]]` | 31 | Row range collapses to a single index while the column range keeps three anchors; the best is $(1,1)$ with $33 - 1 - 1$. |
| Five rows, three columns | `[[1,1,1],[0,1,0],[1,1,1],[0,9,0],[2,2,2]]` | 18 | The answer appears only at the last anchor, $(3,1)$, so an early-exit heuristic would fail it. |
| Maximum cell values | seven cells at $10^{6}$ | $7 \times 10^{6}$ | A single hourglass contains seven cells, so the largest possible answer is $7 \cdot 10^{6}$; no overflow risk in ordinary integer types. |
| Border anchor | any cell in row 0, row $m-1$, column 0 or column $n-1$ | not legal | Such a cell has no complete ring of neighbours, and the loop bounds exclude it. |
| Rotated shape | vertical neighbours removed instead | invalid | The definition fixes which two cells are omitted; swapping the mask would describe a different figure. |

## 7. Alternative methods and their trade-offs

| Method | Time | Auxiliary space | Why it is not used here |
|---|---|---|---|
| Spell out all seven additions per anchor | $O(mn)$ | $O(1)$ | Correct and slightly cheaper in constant factors, but it hides the fact that the shape is a rectangle with a fixed two-cell hole. |
| Two-dimensional prefix sums, then two row queries | $O(mn)$ | $O(mn)$ | The top and bottom segments have fixed length 3, so a prefix matrix buys no asymptotic improvement while adding a full-grid table. |
| Sliding three-row strip sums | $O(mn)$ | $O(n)$ | Maintains length-three column sums to avoid re-adding, at the cost of bookkeeping for a shape of only seven cells. |
| Enumerate anchors, sum the bounding box, subtract the two excluded cells | $O(mn)$ | $O(1)$ | Chosen. Exactly $(m-2)(n-2)$ anchors with a constant nine-cell read each, and no size-dependent storage. |

## 8. Cost of the method: complexity derivation

Let $m$ and $n$ be the grid dimensions.

*Time.* The anchor loops iterate over $m - 2$ rows and $n - 2$ columns, so there
are $(m-2)(n-2)$ placements. Each placement reads exactly nine cells — a fixed
number — and performs a constant number of additions and comparisons. Hence

$$
T(m, n) = 9 \cdot (m-2)(n-2) + O(1) = O(mn).
$$

The constant 9 is the shape's size, not a function of the input. This bound is also
tight for the problem: a constant fraction of the grid's cells participate in some
hourglass, and in a zero-filled grid a correct algorithm cannot know the maximum
without inspecting them, so $\Omega(mn)$ inspections are necessary in the worst
case and the method matches that lower bound.

*Auxiliary space.* The computation holds a running maximum, two loop indices, and
the temporary nine-cell total; nothing is allocated per row or per placement. The
input grid is read but never modified. Therefore

$$
S(m, n) = O(1).
$$

A prefix-sum or sliding-strip variant would raise this to $O(mn)$ or $O(n)$
respectively without changing the time bound, which is why the constant-space form
is preferred here.
