## General

**Greedy counts are forced once the target is known**

Suppose the common final value is an integer $T$, and scan cells from top to bottom and left to right. At a cell `(i, j)` where a $k \times k$ operation may start, every earlier operation count is already fixed. No later top-left corner can cover `(i, j)`, so the operation count beginning there is forced to be

$$
x_{i,j}=T-\bigl(\texttt{grid}[i][j]+\text{prior coverage at }(i,j)\bigr).
$$

It must be nonnegative. At a cell where no operation may start, prior coverage is final and the cell must already equal $T$. These conditions are both necessary and sufficient for a fixed target.

**Keep the target symbolic**

The target itself may exceed the original maximum. For instance, `[[1,0,1],[1,0,1]]` with $k=2$ needs one increment on each of its two possible squares and finishes at $2$.

Represent every forced operation count as $aT+b$. Coverage remains affine because it is a sum of earlier counts. Nonnegativity of $aT+b$ contributes a lower bound, an upper bound, or an immediate contradiction. A finished cell contributes an equation of the form $cT+d=0$; it may force one integer target, agree for every target, or prove the grid impossible. Also require $T$ to be at least the largest original entry because operations never decrease values.

After the scan, choose the smallest integer satisfying every collected bound and equation. This minimizes the operation count: each operation adds $k^2$ to the grid sum, so any successful target obeys

$$
\text{operations}=\frac{mnT-\sum \texttt{grid}[i][j]}{k^2},
$$

which increases with $T$.

**Maintain affine coverage with rolling windows**

For each possible start column, keep the sum of operation expressions from start rows that still cover the current row. A horizontal window of $k$ such columns gives the expression covering the current cell. A queue retains only the last $k$ rows of start expressions so an expired row can be removed before the next scan line. This supplies every affine coverage value in constant amortized time without a full four-dimensional overlap calculation.

The row-major argument forces every operation for a chosen $T$. The collected constraints therefore describe exactly all feasible targets, and selecting their smallest member gives the global minimum.

## Complexity detail

Every one of the $mn$ cells is processed once, and every stored start expression is added and removed once, for $O(mn)$ time. There are $n-k+1$ possible start columns. The column sums and at most $k$ queued rows use $O(k(n-k+1))$ auxiliary space.

The benchmark defines size as the number of cells in a square grid with $k$ equal to half its side length. The rolling method is linear in that size. A correct symbolic implementation that directly resums every earlier start covering every cell performs $\Theta(mnk^2)$ work, which is quadratic in the benchmark's cell count.

## Alternatives and edge cases

- **Try targets one by one:** A numeric greedy check is useful as an oracle, but the necessary target can exceed the original maximum by a large amount and impossible grids provide no successful stopping point.
- **Resum every covering operation:** The same affine reasoning remains correct, but inspecting up to $k^2$ earlier starts at every cell makes dense large squares quadratic in their cell count.
- **Full two-dimensional difference grids:** They also give $O(mn)$ time and are simpler conceptually, but two affine matrices require $O(mn)$ extra storage instead of retaining only active start rows.
- **Unit square:** When $k=1$, each cell changes independently; raising every entry to the original maximum is optimal.
- **One possible square:** If $k=m=n$, the sole operation changes every cell equally, so an initially unequal grid is impossible and an equal grid needs zero operations.
- **Negative entries:** They need no special treatment; bounds and affine constants are ordinary signed integers.
- **Forced target above the maximum:** Overlapping squares can require overshooting every original value, so testing only the maximum is incorrect.
- **Large answer:** The operation total can exceed 32-bit range even though individual grid entries satisfy the stated bounds.
