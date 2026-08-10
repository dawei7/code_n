## General

**A multi-move score telescopes**

Suppose a path visits values $v_0,v_1,\ldots,v_p$. Its total score is

$$
(v_1-v_0)+(v_2-v_1)+\cdots+(v_p-v_{p-1})=v_p-v_0.
$$

All intermediate values cancel. Therefore, only the starting and ending cells matter.

A cell $(a,b)$ can reach $(i,j)$ exactly when $a\le i$, $b\le j$, and the cells are not identical. Direct moves may jump any positive distance down or right, and a sequence of such moves has the same coordinate relation.

For each ending cell $(i,j)$ with value $x$, the best score ending there is

$$
x-\min\{\texttt{grid}[a][b]:a\le i,\ b\le j,\ (a,b)\ne(i,j)\}.
$$

The task becomes maintaining the minimum value in the reachable upper-left rectangle, excluding the current cell until after its candidate score is computed.

**Meaning of f**

The table `f` is the same size as the grid. After processing cell $(i,j)$,

$$
\texttt{f[i][j]}=\min\{\texttt{grid}[a][b]:0\le a\le i,\ 0\le b\le j\}.
$$

The rectangle above the current cell has minimum `f[i - 1][j]`, and the rectangle to its left has minimum `f[i][j - 1]`. Their union contains every legal predecessor:

- any predecessor in an earlier row lies in the upper rectangle;
- any predecessor in the same row but earlier column lies in the left rectangle.

Their overlap is harmless for a minimum. The code sets `mi` to the smaller available prefix minimum.

Before inserting current value $x$ into the prefix state, it updates `ans` with `x - mi`. This ordering enforces the requirement to make at least one move. If $x$ were included first, a cell could choose itself and create an invalid zero-move score of zero, which would be especially wrong when all legal scores are negative.

After evaluating the endpoint, `f[i][j] = min(x, mi)` extends the prefix minimum to include the current cell for future destinations.

**Boundary cells**

At `(0,0)`, neither an upper nor left predecessor exists, so `mi` remains positive infinity. `x - inf` remains negative infinity and does not create an answer. The cell is still stored in `f[0][0]` for later moves.

In the first row, only the left prefix exists; in the first column, only the upper prefix exists. These exactly match the only legal move directions available there.


Inductively assume the stored upper and left states are their complete rectangle minima. Their union is the current upper-left rectangle with the current cell removed, so `mi` is the minimum value among all legal starting cells that can reach $(i,j)$. Subtracting the smallest start from fixed endpoint $x$ maximizes $x-start$, so the candidate is the best score ending at this cell.

Every legal path has some ending cell, and its telescoped score is no greater than that endpoint's candidate. Conversely, each candidate is achieved by moving directly from the cell holding `mi` to the current cell, because its coordinates are upper-left reachable. Taking the maximum over all endpoints yields the global optimum.

**Example**

In a decreasing grid, every legal destination may be smaller than every predecessor. The answer is then negative. Because the source never compares against the current cell itself and initializes `ans` to `-inf`, it correctly returns the least negative legal move, such as $-1$, rather than an invalid zero.

For the example containing 5 at `(0,1)` and 14 at `(2,2)`, the prefix minimum before 14 is at most 5, so candidate score 9 is found. A two-step path has the same telescoped value as the direct reachable move.

## Complexity detail

Let $m$ and $n$ be the grid dimensions.

Every cell is processed once with constant-time minimum and subtraction operations, so time is $O(mn)$.

The exact source allocates an $m\times n$ table `f`, so auxiliary space is $O(mn)$. This contradicts the manifest's $O(n)$ claim, which would apply to a rolling-row implementation retaining only the previous row and the current row's running prefix minimum.

The input grid is not modified. Scalar state contributes $O(1)$ beyond the table.

Given the source constraint $mn\le10^5$, the full table is feasible, though Python row-list and integer-reference overhead is larger than a compact numeric matrix.

## Alternatives and edge cases

- **Rolling prefix minima:** Keep the previous row's minima and update a current row array, reducing auxiliary space to $O(n)$ while preserving $O(mn)$ time.
- **Modify the grid in place:** Reuse each cell to store the prefix minimum. This saves auxiliary space but destroys the input values needed for clarity and may violate caller expectations.
- **Enumerate all start/end pairs:** There can be $O(m^2n^2)$ reachable pairs, far too many.
- **Dynamic path score:** Tracking best multi-step scores is unnecessary because move differences telescope to final minus initial value.
- **At least one move:** Candidate evaluation must happen before adding $x$ to its own prefix minimum.
- **All scores negative:** `ans = -inf` preserves the best negative move instead of defaulting to zero.
- **First cell:** It has no predecessor and contributes no candidate.
- **First row or column:** Only one prefix direction exists, and the bounds checks select it.
- **Repeated minimum values:** Any reachable occurrence realizes the same candidate; the algorithm needs only the value, not coordinates.
- **Nonadjacent moves:** Prefix rectangles include all upper-left cells, so jumps of arbitrary allowed distance are covered.
- **Intermediate stops:** They cannot improve or worsen the telescoped score for fixed endpoints.
- **Positive grid values:** Infinity sentinels are safe; correctness would also hold for signed values.
