## General

**Precompute information reused by every cell**

The formula for `diff[i][j]` depends on four counts, but row counts repeat across all columns and column counts repeat across all rows. Computing them separately for every output cell would rescan rows and columns many times.

The first pass counts ones:

- `rows[i]` is the number of ones in row `i`.
- `cols[j]` is the number of ones in column `j`.

Because the grid is binary, zero counts follow from dimensions:

$$
\text{zerosRow}_i=n-\text{rows}[i]
$$

and

$$
\text{zerosCol}_j=m-\text{cols}[j].
$$

No separate zero arrays are necessary.

**Fill each output cell**

For row-one count `r` and column-one count `c`, the assignment is

`r+c-(n-r)-(m-c)`.

This is exactly

$$
\text{onesRow}_i+\text{onesCol}_j
-\text{zerosRow}_i-\text{zerosCol}_j.
$$

It can also be simplified to

$$
2r+2c-n-m,
$$

but the source's unsimplified expression mirrors the statement and makes the zero complements visible.

**Trace one sample cell**

For the first sample's cell `(0,2)`, row 0 has two ones and column 2 has three. Row length is three and column height is three, so zero counts are one and zero. The formula gives `2+3-1-0=4`.

For cell `(2,0)`, row-one count is one and column-one count is one. Each corresponding zero count is two, giving `1+1-2-2=-2`.

Negative output values are allowed because the formula is a difference, even though input entries are only zero and one.


The counting pass visits every grid entry. Whenever it sees one, it increments exactly that entry's row and column counts; zero adds nothing. After the pass, the arrays contain exact one totals.

Every row has $n$ entries, so subtracting its one total gives exact zeros. Every column has $m$ entries, giving the analogous column result.

The second pass substitutes those exact four quantities into the required formula for every coordinate. Thus every returned cell is correct.

**Why the original cell is counted twice when appropriate**

The definition independently includes the cell in its row statistics and in its column statistics. If `grid[i][j]=1`, it contributes once to `onesRow` and once to `onesCol`; if zero, it contributes to both zero counts. The source follows this definition rather than attempting to deduplicate the intersection.

**Rectangular matrices**

Rows use length `n` and columns use height `m`. Swapping these dimensions in the zero formulas would fail for non-square grids. The exact expression uses them correctly.

**Follow the two loops carefully**

The first nested loop uses `enumerate(grid)` to obtain row index `i` and the row itself. Its inner `enumerate(row)` produces column index `j` and value `x`. Adding `x` works because the only permitted values are zero and one: a zero changes neither counter, while a one increases both the appropriate row total and column total. If arbitrary integers were allowed, this shortcut would sum values instead of counting ones, but the binary contract makes it exact.

The second nested loop does not need to read the individual grid value. Once `rows[i]` and `cols[j]` are known, the required result at coordinate $(i,j)$ is fully determined. The source creates `res` with the same shape as `grid`, then writes each calculated difference into its corresponding position. This separation between “summarize the input” and “construct every output” is a common optimization when many queries reuse the same aggregate.

For a concrete rectangular example, suppose a row has length five and contains two ones. Its contribution to every cell in that row is $2-(5-2)=-1$. If a particular column has height three and contains all three ones, its contribution is $3-(3-3)=3$. Every cell at their intersection receives $-1+3=2$. Computing those two reusable balances once is equivalent to repeatedly counting the same entries, but much cheaper.

**An equivalent balance interpretation**

Give every one weight $+1$ and every zero weight $-1$. Then a row's total weight is its number of ones minus its number of zeros, and a column's total weight has the analogous meaning. The requested cell is simply its row balance plus its column balance. The source stores one counts rather than balances, but the complement arithmetic transforms them into exactly these signed sums.

## Complexity detail

Both passes visit all $mn$ cells once, so time is $O(mn)$.

The row and column count arrays use $O(m+n)$ auxiliary space. The returned matrix uses $O(mn)$ output space. The manifest's $O(m+n)$ space convention excludes required output storage.

The constraint $mn\le10^5$ bounds both runtime and output size even though either single dimension may be large.

## Alternatives and edge cases

- **Signed contribution sums:** Treat one as +1 and zero as -1, accumulate row and column balances, then add them per cell. This directly computes one-minus-zero counts.
- **Recount per cell:** Scanning a row and column for every output position costs $O(mn(m+n))$ and repeats work.
- **Separate zero arrays:** They are unnecessary because binary row and column sizes determine zero counts.
- **All ones:** Every cell value is `n+m` because zero counts vanish.
- **All zeros:** Every cell value is `-(n+m)`.
- **Single row:** Column counts describe one cell each, and the same formulas remain valid.
- **Single column:** Row counts describe one cell each with no special case.
- **Negative results:** They correctly indicate more zeros than ones across the combined row and column counts.
- **Intersection cell:** It is intentionally included in both row and column statistics.
- **Output storage:** The result itself is $O(mn)$ even though reusable auxiliary counts are only $O(m+n)$.
