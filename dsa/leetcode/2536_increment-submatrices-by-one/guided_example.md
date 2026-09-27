# Guided Example: Increment Submatrices by One

## 1. The instance, and why the obvious method is too slow

Take the first official instance: `n = 3` with
`queries = [[1,1,2,2],[0,0,1,1]]`. The matrix starts as three rows of three
zeros, and each query adds `1` to every cell of the submatrix whose top-left
corner is $(\text{row1}, \text{col1})$ and whose bottom-right corner is
$(\text{row2}, \text{col2})$, both corners **inclusive**. The declared result is
`[[1,1,0],[1,2,1],[0,1,1]]`.

The direct method touches every cell of every rectangle. On this instance that is
cheap — the first query covers a $2 \times 2$ block and the second another
$2 \times 2$ block, eight cell updates in total — but the documented limits are
`n` up to $500$ and up to $10^4$ queries, and a query may cover the entire
matrix. In the worst case the direct method performs
$10^4 \cdot 500 \cdot 500 = 2.5 \times 10^{9}$ cell increments, which no
reasonable time limit tolerates. The rest of this lesson replaces that work by
$O(1)$ marking per query followed by a single reconstruction sweep over the
$n^2 = 250{,}000$ cells.

## 2. The key identity: a rectangle is an outer product of two intervals

Work in one dimension first. Suppose a value $v$ must be added to every position
$y$ with $\text{col1} \le y \le \text{col2}$. Instead of writing $v$ into each
position, record two markers: $+v$ at `col1` and $-v$ at `col2 + 1`. Taking a
running prefix sum of the markers then reproduces the intended array exactly,
because the $+v$ switches the running total on and the $-v$ switches it off again
one position after the interval ends.

| 1D goal | Markers written | Prefix sum afterwards |
|---|---|---|
| add $v$ to positions $4 \dots 6$ of a length-9 row | $+v$ at 4, $-v$ at 7 | $0,0,0,v,v,v,0,0,0$ |
| add $v$ to positions $0 \dots 8$ | $+v$ at 0 only, since position 9 does not exist | $v$ everywhere |

In two dimensions, the rectangle indicator factors as a product of two 1D
indicators:

$$
\bigl[\text{row1} \le x \le \text{row2}\bigr] \cdot \bigl[\text{col1} \le y \le \text{col2}\bigr].
$$

Marking the two dimensions independently means writing the four cross terms of
that product, with the sign of each term inherited from the 1D markers:

| Marker position | Sign | Why |
|---|---|---|
| $(\text{row1}, \text{col1})$ | $+1$ | both intervals start here |
| $(\text{row2} + 1, \text{col1})$ | $-1$ | the row interval ends, the column interval has not |
| $(\text{row1}, \text{col2} + 1)$ | $-1$ | the column interval ends, the row interval has not |
| $(\text{row2} + 1, \text{col2} + 1)$ | $+1$ | both intervals end, cancelling the double subtraction |

A marker is written only if its coordinate exists inside the matrix; when
$\text{row2} + 1 = n$ or $\text{col2} + 1 = n$ that marker is simply omitted,
because there is no cell beyond the boundary to switch anything off in. This is
the first place a careless implementation breaks on the boundary.

## 3. Marking the two queries of the instance

| Query | $(\text{row1}, \text{col1})$ | $(\text{row2} + 1, \text{col1})$ | $(\text{row1}, \text{col2} + 1)$ | $(\text{row2} + 1, \text{col2} + 1)$ |
|---|---|---|---|---|
| `[1,1,2,2]` | `+1` at `(1,1)` | omitted, since $2 + 1 = 3 = n$ | omitted, since $2 + 1 = 3 = n$ | omitted |
| `[0,0,1,1]` | `+1` at `(0,0)` | `-1` at `(2,0)` | `-1` at `(0,2)` | `+1` at `(2,2)` |

Note that the second query behaves differently from the first only because it
touches the far boundary. Adding the marks into a single difference grid, with
rows top to bottom and columns left to right, gives the state that the
reconstruction will consume:

| Row / Column | col 0 | col 1 | col 2 |
|---|---|---|---|
| row 0 | $+1$ | $0$ | $-1$ |
| row 1 | $0$ | $+1$ | $0$ |
| row 2 | $-1$ | $0$ | $+1$ |

Every number in this grid is a marker, not an answer. The pattern is a signed
"switch board": each query contributed one positive switch at its top-left
corner and, where the boundary allowed, negative switches along the two edges
that leave the rectangle.

## 4. Reconstructing the answers with a two-dimensional prefix sum

The reconstruction replaces every marker by the sum of all markers in the
rectangle from `(0,0)` to that cell. Writing $P[i][j]$ for the value after the
sweep and $D[i][j]$ for the marker grid, the recurrence is

$$
P[i][j] = D[i][j] + P[i-1][j] + P[i][j-1] - P[i-1][j-1],
$$

where a term with a negative index is $0$. The subtraction of $P[i-1][j-1]$ is
plain inclusion-exclusion: the prefix of the cell above and the prefix of the
cell to the left overlap exactly in the prefix of the diagonal cell, so that
region has been added twice and must be removed once. Sweeping in row-major order
guarantees that the three neighbours a cell reads are already final, so one pass
suffices.

| Cell $(i,j)$ | Marker $D[i][j]$ | Above $P[i-1][j]$ | Left $P[i][j-1]$ | Diagonal $P[i-1][j-1]$ | Result $P[i][j]$ |
|---|---|---|---|---|---|
| $(0,0)$ | $1$ | — | — | — | $1$ |
| $(0,1)$ | $0$ | — | $1$ | — | $1$ |
| $(0,2)$ | $-1$ | — | $1$ | — | $0$ |
| $(1,0)$ | $0$ | $1$ | — | — | $1$ |
| $(1,1)$ | $1$ | $1$ | $1$ | $1$ | $1 + 1 + 1 - 1 = 2$ |
| $(1,2)$ | $0$ | $0$ | $2$ | $1$ | $0 + 0 + 2 - 1 = 1$ |
| $(2,0)$ | $-1$ | $1$ | — | — | $0$ |
| $(2,1)$ | $0$ | $2$ | $0$ | $1$ | $0 + 2 + 0 - 1 = 1$ |
| $(2,2)$ | $1$ | $1$ | $1$ | $2$ | $1 + 1 + 1 - 2 = 1$ |

Reading the rightmost column as a matrix,

| Row / Column | col 0 | col 1 | col 2 |
|---|---|---|---|
| row 0 | 1 | 1 | 0 |
| row 1 | 1 | 2 | 1 |
| row 2 | 0 | 1 | 1 |

which matches the declared `[[1,1,0],[1,2,1],[0,1,1]]`. The centre cell is the
most informative one: it lies inside both rectangles and ends at $2$, while the
four corners of the first rectangle reach only $1$, and cells outside every
rectangle such as `(0,2)` and `(2,0)` end at $0$.

## 5. The correctness argument

Define the *coverage* of a cell as the number of queries whose rectangle contains
it; that is exactly what the answer must be. Two claims establish the method.

**Claim 1: prefix sums of the marker grid reproduce per-query indicators.** For a
single query, consider the 1D intervals as switch functions. The running prefix of
the row markers is $1$ exactly for $\text{row1} \le x \le \text{row2}$ and $0$
outside, and likewise for the column markers. Taking the 2D prefix sum of the
outer product of these two switch functions yields the product of their running
prefixes, which is $1$ exactly on the rectangle and $0$ elsewhere. Markers beyond
the last row or column would switch the value off after the boundary, but there
is no such cell, so omitting them changes nothing inside the matrix.

**Claim 2: the recurrence computes the 2D prefix sum.** By induction on
row-major order, assume $P[i-1][j]$, $P[i][j-1]$ and $P[i-1][j-1]$ already equal
the sum of markers in their respective prefix rectangles. The union of the
rectangles of the first two cells is the prefix rectangle of $(i,j)$ together
with the prefix rectangle of $(i-1,j-1)$ counted twice, so
$P[i-1][j] + P[i][j-1] - P[i-1][j-1]$ equals the marker sum of everything before
$(i,j)$ in both coordinates, and adding $D[i][j]$ completes the prefix.

By linearity, summing the per-query indicators over all queries gives the
coverage of every cell, so the final grid is the required answer. The invariant
carried by the sweep is therefore: *after the cell $(i,j)$ is processed, it holds
the total number of queries covering $(i,j)$*, and each query is represented by
exactly four markers regardless of how large its rectangle is.

## 6. Cost, and the alternative that loses

| Method | Work per query | Total work | Auxiliary space |
|---|---|---|---|
| add `1` to every covered cell | $O(\text{area})$ | $O\bigl(\sum_i \text{area}_i\bigr)$, up to $2.5 \times 10^{9}$ here | $O(1)$ beyond the output |
| difference markers plus one prefix sweep | $O(1)$, at most four writes | $O(q + n^2)$ | $O(1)$ beyond the output when the grid is reused |

The two methods compute the same quantity, and the difference grid is itself the
object that later becomes the answer: the marker grid is overwritten in place by
its own prefix sums, so no second matrix is allocated. The price is that the
markers are destroyed during the sweep, so nothing can inspect the marker grid
afterwards.

## 7. Traps and boundary behaviour

| Situation | Symptom if mishandled | Correct behaviour |
|---|---|---|
| $\text{row2} + 1 = n$ or $\text{col2} + 1 = n$ | writing a marker outside the matrix, or wrapping into the next row | omit that marker entirely; there is nothing beyond the boundary to switch off |
| the diagonal marker $(\text{row2}+1, \text{col2}+1)$ | using $-1$ there leaves every rectangle's interior short by one in its bottom-right region | its sign is $+1$: it cancels the double subtraction of the two edge markers |
| a single-cell query, such as `[0,0,0,0]` | the four markers are skipped as "degenerate" and the cell stays $0$ | the top-left marker is still written; on a $1 \times 1$ matrix the other three are out of bounds |
| a query covering the whole matrix, such as `[0,0,1,1]` on `n = 2` | expecting three extra marks and finding none | only the top-left marker exists, and the prefix sweep spreads it over all four cells |
| repeated identical queries | expecting a boolean instead of a count | markers accumulate, so the count is the coverage, not a flag |
| sweep order | computing cells in the wrong order reads neighbours that are not yet prefix sums | row-major order, top-left to bottom-right, always reads finished neighbours |
| the overlap subtraction | forgetting $P[i-1][j-1]$ inflates every cell below the first row and right of the first column | the diagonal prefix is double counted by the up and left prefixes and must be subtracted exactly once |
| `n = 1` | bounds checks that assume at least two rows or columns | the single cell receives one marker per query covering it, and all other markers are out of bounds |

One further check is worth running mentally on every instance: on a matrix with
`r` queries, the sum of all entries of the answer must satisfy
$\sum_{i,j} \text{mat}[i][j] = \sum_{k} \text{area}_k$, because the prefix sweep
only rearranges the markers, never changes their total. For the instance above,
the two rectangles have areas $4$ and $4$, and the final grid sums to
$1+1+0+1+2+1+0+1+1 = 8$.

## 8. Time and auxiliary space

Let $q$ be the number of queries. Marking writes at most four grid entries per
query, so it costs $O(q)$. The reconstruction visits each of the $n^2$ cells once
and does constant work there, so it costs $O(n^2)$. The total is
$O(q + n^2)$, which under the documented limits is dominated by the sweep at
about $250{,}000$ cell operations, compared with the $2.5 \times 10^{9}$ of the
direct method.

Auxiliary space beyond the returned matrix is $O(1)$: the grid is allocated once
as the output, used as the marker board, and then overwritten by its own prefix
sums, so no additional $n \times n$ structure is needed. If the markers were kept
for later inspection, a second matrix would be required and auxiliary space would
become $O(n^2)$; the in-place sweep deliberately trades that away.