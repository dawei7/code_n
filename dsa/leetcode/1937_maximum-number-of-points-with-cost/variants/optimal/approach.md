## General

**Dynamic programming by the last chosen column**

After processing a row, future decisions need to know the best score for each possible column chosen in that row. Let `f[k]` be the maximum score after the previous row when its selected cell is column $k$.

For the current row `p`, ending at column $j$ should give

$$
g[j]=p[j]+\max_k\left(f[k]-\lvert k-j\rvert\right).
$$

A direct implementation would inspect all previous columns $k$ for every current column $j$, taking $O(N^2)$ time per row. The key optimization is to split the absolute value according to whether $k$ lies left or right of $j$.

**Left-to-right sweep**

When $k\le j$,

$$
f[k]-\lvert k-j\rvert=f[k]-(j-k)=f[k]+k-j.
$$

For a fixed $j$, the part depending on $k$ is $f[k]+k$. During a left-to-right scan, `lmx` stores the maximum of that quantity over all $k\le j$. The update

`lmx = max(lmx, f[j] + j)`

first includes the current previous-row column. The candidate

`p[j] + lmx - j`

is therefore the best transition into current column $j$ from any previous column at or to its left.

**Right-to-left sweep**

When $k\ge j$,

$$
f[k]-\lvert k-j\rvert=f[k]-(k-j)=f[k]-k+j.
$$

Scanning from right to left, `rmx` stores the maximum of $f[k]-k$ over all $k\ge j$. The candidate `p[j] + rmx + j` is the best transition from the right. Taking the maximum of the left and right candidates covers every possible previous column.

The code initializes `lmx` and `rmx` to negative infinity so that no nonexistent predecessor can win before a real `f` value is included.

**Base row and row updates**

For the first row there is no movement penalty. The solution copies it into `f` with `points[0][:]`, so `f[j]` is simply the score from choosing column $j$ there.

For each later row, a fresh `g` receives both sweeps, then `f = g` advances the state. The input values are nonnegative and previous scores are nonnegative, so initializing `g` with zero is safe; every real candidate is at least as large. After the last row, any ending column is allowed, and `max(f)` returns the best complete score.

**Why the transition is exact**

Fix a current column $j$. Every previous column belongs to exactly one of the sets $k\le j$ or $k\ge j$; column $j$ belongs to both, which is harmless because both formulas give the same zero-penalty transition there. The left sweep computes the maximum transition over the first set, and the right sweep computes it over the second. Their maximum is therefore exactly the maximum over all $k$ in the original recurrence.

By induction, the initial `f` is correct for one row. If `f` is correct for the processed rows, the exact transition adds the current cell's value and the correct movement penalty to every possible prior ending, then keeps the best. Thus `g` is correct for one more row. The final maximum is consequently the optimal score.

For the first sample, this process allows the path through columns $2$, $1$, and $0$. Each sweep accounts for the one-column movement penalties without enumerating all nine previous-current pairs per transition.

## Complexity detail

Let $M$ be the number of rows and $N$ the number of columns.

Each later row receives one left-to-right scan and one right-to-left scan, both $O(N)$. Copying the first row and taking the final maximum also cost $O(N)$. Total time is $O(MN)$.

The DP arrays `f` and `g` each contain $N$ integers, so the core algorithm uses $O(N)$ auxiliary space. At row replacement the old and new arrays coexist briefly, still $O(N)$.

The exact loop `for p in points[1:]` first creates an outer-list slice containing $M-1$ row references, which adds $O(M)$ temporary space. Thus strict peak auxiliary allocation is $O(M+N)$ for this Python source, although the standard algorithmic bound and manifest report $O(N)$. Iterating by row index or with an iterator that skips the first row would remove that slice.

## Alternatives and edge cases

- **Quadratic transition:** Evaluate every previous column for every current column. It follows the recurrence directly but costs $O(MN^2)$ time.
- **Prefix and suffix arrays:** Explicitly build best-left and best-right arrays for each row, then combine them. This has the same $O(MN)$ time and $O(N)$ space with more arrays.
- **In-place sweep variant:** The previous DP array can hold left-sweep maxima before a right sweep combines them with the current row, reducing constants but requiring careful update order.
- **One row:** No transition occurs, and the maximum cell in that row is returned.
- **One column:** Both sweeps always use the only column, movement cost is zero, and the result is the sum down the column.
- **Staying in the same column:** It appears in both sweeps with distance zero and is considered normally.
- **Large column jump:** Repeated subtraction is encoded algebraically by the index terms, so no per-step simulation is needed.
- **Tied optimal predecessors:** Either sweep may find the same maximum; only the score is requested.
- **Nonnegative points:** This guarantee makes zero initialization of `g` safe in the exact code.
- **Negative infinity dependency:** The source assumes `inf` is available and uses `-inf` as the initial running maximum.
- **Input preservation:** `f` begins as a copy of the first row, so DP updates do not alter `points`.
- **Outer slice allocation:** `points[1:]` costs $O(M)$ extra references; an indexed loop would preserve the textbook $O(N)$ space bound exactly.
