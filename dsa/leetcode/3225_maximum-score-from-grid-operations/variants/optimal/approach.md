## General

**Describe a final coloring by one height per column.** An operation colors a prefix of one column black. Repeating operations on that column is equivalent to keeping only the deepest selected row. Therefore every final configuration is described by a height

$$
H_c\in\{0,1,\ldots,n\}
$$

for each column $c$: rows $0$ through $H_c-1$ are black, and rows $H_c$ through $n-1$ are white.

A white cell in column $c$ scores when its row is below the black height of the left neighbor or the right neighbor. Once the three heights $(H_{c-1},H_c,H_{c+1})$ are known, the scoring rows in center column $c$ form

$$
[H_c,\max(H_{c-1},H_{c+1}))
$$

when that upper endpoint exceeds $H_c$. The cell is counted once even if both neighbors are black because the union of the two row intervals is just the interval to their maximum.

**Precompute column prefix sums.** `prefix[column][h]` is the sum of rows $0$ through $h-1$ in that column. The sum of rows from height $a$ through $b-1$ is

`prefix[column][b] - prefix[column][a]`.

This makes any interval contribution constant-time. Since grid values are nonnegative, `max(0, difference)` conveniently returns zero when the neighbor height does not exceed the center height.

**Keep two adjacent heights in the DP state.** After some columns are finalized, `dp[left_height][center_height]` stores the best score so far while the last two chosen column heights have those values. A column cannot be finalized when only its own and left height are known; its right neighbor may also make white cells score. Keeping two heights allows the next choice to reveal the needed triple.

**Initialize the left boundary.** For every possible heights $H_0$ and $H_1$, column zero has no left neighbor. It scores white rows that are black in column one:

$$
[H_0,H_1)
$$

when $H_1>H_0$. The initialization

`prefix[0][right_height] - prefix[0][left_height]`

stores that contribution; otherwise the zero-initialized state remains zero.

For $n=1$, no cell has a horizontal neighbor at all, so the method returns zero immediately.

**Transition by finalizing the center column.** During loop iteration `column`, the old state uses heights

$$
L=H_{column-1},\qquad C=H_{column},
$$

and the new choice is

$$
R=H_{column+1}.
$$

The center column contribution is

$$
\max\left(0,\ prefix[column][\max(L,R)]-prefix[column][C]\right).
$$

A naive transition would try all $L,C,R$, giving $O(n^4)$ across columns. The exact source optimizes the maximum over $L$ for every fixed $C$.

**Split previous heights around the new right height.** For fixed $C$ and candidate $R$, there are two cases:

- If $L\le R$, then $\max(L,R)=R$. The gain depends only on $R$, so use the best `dp[L][C]` among $L\le R$, stored in `prefix_best[R]`, and add `right_gain`.
- If $L>R$, then $\max(L,R)=L$. The gain depends on $L$, so `suffix_best[R+1]` stores the best value of `dp[L][C] + gain(C,L)` among all $L\ge R+1$.

The transition

`max(prefix_best[right_height] + right_gain, suffix_best[right_height + 1])`

therefore considers every previous left height in constant time after the two helper scans.

The new state indices become `[C][R]` because the window shifts one column right.

**Finalize the right boundary.** After all interior columns are processed, `dp[left_height][last_height]` includes scores through column $n-2$. The last column has only its left neighbor. Its contribution is white rows from `last_height` up to `left_height` when the left height is larger:

`max(0, last_prefix[left_height] - last_prefix[last_height])`.

The final double loop adds this boundary contribution and maximizes over the last two heights.

**Why this counts each scoring cell once.** Column zero is finalized during initialization, every interior column is finalized in exactly one transition after both neighbor heights are known, and the last column is finalized at the end. Within a column, using the maximum neighbor height takes the union of left-triggered and right-triggered white rows, avoiding double counting cells adjacent to black on both sides.

Every height vector appears along one chain of states, so the DP considers every obtainable coloring. Each state keeps the greatest score among histories with the same last two heights, which are the only history facts future columns need. Discarding lower-scoring histories is safe.

## Complexity detail

There are $n+1$ possible heights. Prefix construction costs $O(n^2)$ time and space. Initialization and finalization each examine $O(n^2)$ height pairs.

For each of $O(n)$ interior columns, the source loops over $O(n)$ center heights. For each center it builds prefix maxima, suffix maxima, and all right-height transitions, each in $O(n)$ time. This is $O(n^2)$ per column and $O(n^3)$ total time.

`prefix`, `dp`, and `next_dp` each use $O(n^2)$ space. Temporary prefix/suffix arrays use $O(n)$. Peak auxiliary space is $O(n^2)$, matching the manifest.

With values up to $10^9$, scores can exceed 32-bit range; Python integers remain exact.

## Alternatives and edge cases

- **Naive four-loop DP:** Enumerate previous-left, center, right, and column explicitly. It clarifies the recurrence but costs $O(n^4)$.
- **Three-dimensional table over all columns:** Store every column layer instead of rolling `dp`. It uses $O(n^3)$ space without helping future transitions.
- **Enumerate all height vectors:** There are $(n+1)^n$ configurations, far beyond feasible.
- **No operations:** Every height is zero; no adjacent black cell exists and score is zero, so the optimum is never negative.
- **All cells black:** No white cell remains to score, also yielding zero.
- **Single column:** Horizontal adjacency is impossible, and the explicit early return gives zero.
- **Two columns:** Initialization handles column zero and finalization handles column one; the interior loop is empty.
- **Both neighbors black at one white row:** The cell value is counted once through the union endpoint `max(L,R)`.
- **Center taller than both neighbors:** No white center cell lies beside their black prefixes, so contribution is zero.
- **Nonnegative grid guarantee:** It supports zero-initialized maxima and interval clamping. Negative values would require more careful optional-contribution reasoning.
- **Height zero:** The whole column is white.
- **Height $n$:** The whole column is black and contributes no own white cells, though it may make neighbor cells score.
- **Rolling state:** After transition, old left history is irrelevant once its center column contribution has been finalized.
- **Source provenance comment:** The file labels itself AI-generated, but its verified submission and the exact recurrence—not that comment—anchor this explanation.
