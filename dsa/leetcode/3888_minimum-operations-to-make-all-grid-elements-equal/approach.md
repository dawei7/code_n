## General

The operation adds $1$ to every cell of one $k \times k$ square. Applying the same square several times is therefore equivalent to assigning a nonnegative operation count to that square. The submitted source does not perform those increments one at a time. Instead, it chooses a possible final value, scans the grid once, and determines in bulk how many times every square would have to be used.

There are two separate ideas to understand:

1. for one fixed target value, the row-major greedy scan is forced and valid; and
2. the source tries only two target values, and that restriction is not valid for the complete stated problem.

The distinction is essential. The efficient fixed-target checker is a useful algorithm, but it does not by itself justify the final answer returned by this particular implementation.

**Why a target cannot be smaller than the original maximum**

Let

$$
M = \max_{0 \le r < m,\ 0 \le c < n} \texttt{grid}[r][c].
$$

Every operation only increases values. No cell can ever be reduced, so any common final value $T$ must satisfy $T \ge M$. The source computes `mx` as this maximum and then calls `check` for $T=M$ and $T=M+1$, in that order.

Trying targets in increasing order is sensible. If a target $T$ is reachable with $q$ square operations, summing all grid entries gives

$$
\sum \text{final values}
=
\sum \text{original values} + qk^2.
$$

Because every one of the $mn$ final cells equals $T$,

$$
q = \frac{mnT-\sum \texttt{grid}[r][c]}{k^2}.
$$

Thus, among two reachable targets, the smaller target necessarily uses fewer operations. What is missing is a reason that the smallest reachable target must be either $M$ or $M+1$; that claim is false.

**Why the scan is forced for one fixed target**

Inside `check(target)`, cells are visited from top to bottom and from left to right. Consider the current cell $(i,j)$. All square operations whose top-left corners occur earlier in row-major order have already been decided.

Any operation chosen later cannot repair this cell:

- a square beginning in a later row starts below $(i,j)$;
- a square beginning later in the same row starts to the right of $(i,j)$; and
- a square beginning in an earlier position would touch a cell whose final value has already been fixed.

Consequently, after earlier coverage is included, only one new decision remains possible without disturbing processed cells: start a $k \times k$ square exactly at $(i,j)$. This makes the greedy amount unique.

Let `cur_val` be the cell's original value plus all increments from previously chosen squares.

- If `cur_val > target`, the target is impossible because no operation can decrease the cell.
- If `cur_val == target`, the scan must do nothing here.
- If `cur_val < target`, exactly `target - cur_val` copies of the square starting at $(i,j)$ are required.
- If that square would cross the bottom or right boundary, no future legal square can cover the deficit, so the target is impossible.

This is stronger than saying the greedy choice “looks locally best.” There is no alternative choice for a fixed target. Any valid construction must make the same decision at the first cell where it differs from the scan. Inductively, the checker either reconstructs the unique operation counts for that target or identifies the first contradiction.

**How the two-dimensional difference matrix represents coverage**

Updating all $k^2$ cells after every chosen square would be too slow. The source instead allocates `diff` with extra sentinel rows and columns. When the scan reaches one-based cell $(i,j)$, it converts the stored corner changes into the total active increment at that cell:

$$
\texttt{diff}[i][j]
\mathrel{+}=
\texttt{diff}[i-1][j]
+\texttt{diff}[i][j-1]
-\texttt{diff}[i-1][j-1].
$$

This is a two-dimensional prefix sum. If `needed` copies of the square beginning at $(i,j)$ are forced, the source records the rectangle by changing only four corners:

- add `needed` at $(i,j)$;
- subtract it at $(i+k,j)$;
- subtract it at $(i,j+k)$; and
- add it back at $(i+k,j+k)$.

Later prefix accumulation spreads that value over exactly rows $i$ through $i+k-1$ and columns $j$ through $j+k-1$. The source also adds `needed` directly to the already accumulated current entry, which makes the new square active at its top-left cell immediately. Large operation counts are handled arithmetically; the algorithm never loops once per unit increment.

**The two-target search has a concrete failure**

Consider

```text
grid = [[2, 0, 2],
        [2, 0, 2]]
k = 2
```

There are two possible $2 \times 2$ squares: the left square and the right square. Let their operation counts be $x$ and $y$, and let the common final value be $T$. Looking at the three columns gives

$$
2+x=T,\qquad 0+x+y=T,\qquad 2+y=T.
$$

The outer columns force $x=y=T-2$. Substitution into the middle equation yields $2(T-2)=T$, so $T=4$ and $x=y=2$. Four operations really do make every cell equal to $4$.

The source sets $M=2$ and checks only $T=2$ and $T=3$. Both checks fail, after which the method returns `-1`. It never tests the valid target $T=4$. Therefore, the source file labeled Optimal is not correct for every input allowed by the local problem description. The fixed-target scan remains sound, but the outer target selection is incomplete.

## Complexity detail

Let $m$ and $n$ be the grid dimensions. Finding `mx` examines every cell once, costing $O(mn)$ time.

One call to `check` allocates an $(m+2)\times(n+2)$ matrix and performs constant arithmetic at each of the $mn$ cells. Creating the matrix and scanning it both cost $O(mn)$ time. The source calls `check` at most twice, so its total running time is still

$$
O(mn).
$$

The amount by which a cell is below the target does not multiply the running time. A deficit of one and a deficit of one billion are each represented by one integer `needed` and four difference-matrix updates.

The exact auxiliary space used by this source is

$$
O(mn),
$$

because `diff` stores $(m+2)(n+2)$ integers. The two checks run sequentially, so two such matrices are not simultaneously live. The input grid itself is not modified.

This differs from the Optimal manifest, which states $O(k(n-k+1))$ space and describes rolling square coverage. A rolling implementation could potentially retain only the still-relevant update frontier, but the checked-in Python source does not do that: it materializes the complete two-dimensional matrix. Its space claim must therefore be explained as $O(mn)$ when documenting the code that actually runs.

The complexity bounds describe execution cost, not semantic validity. Running in $O(mn)$ time does not repair the incomplete target search; the counterexample fails within that efficient bound.

## Alternatives and edge cases

- **Derive the feasible target instead of guessing two values:** The fixed-target greedy decisions are affine expressions in $T$, so a complete solution must use the boundary equations and nonnegativity conditions to determine which target values are feasible; merely trying $M$ and $M+1$ is insufficient.
- **Full difference matrix versus rolling coverage:** The source favors a straightforward $(m+2)\times(n+2)$ matrix. A carefully designed rolling structure could reduce storage, but its expiration rules must preserve the same two-dimensional rectangle contributions.
- **Single-cell squares:** When $k=1$, every cell can be raised independently. Target $M$ is always feasible and is optimal, so the first source check succeeds.
- **One square covers the whole grid:** When $k=m=n$, every operation changes every cell equally. Equality is possible only if all cells were equal already; otherwise their pairwise differences never change.
- **Deficit near the bottom or right border:** If the current cell is below $T$ but cannot be the top-left corner of a complete $k\times k$ square, the fixed target is impossible. No later square can reach backward to that cell.
- **Overshooting a cell:** Once accumulated coverage makes `cur_val` exceed $T$, the checker must fail immediately because all permitted changes are nonnegative.
- **Negative starting values:** Negative entries do not change the reasoning. Only relative deficits and the maximum initial value matter, and Python integers safely hold the resulting counts.
- **Repeated selection of one square:** A forced count `needed` may be much larger than one. Storing it as a single rectangle update is exactly equivalent to applying that square `needed` times.
- **Minimum-operation interpretation:** For any reachable target, total operations are fixed by the total-sum equation. The first reachable target is therefore optimal, but a correct search still has to find that first reachable target.
- **Source-status warning:** On `[[2,0,2],[2,0,2]]` with `k=2`, the checked-in method returns `-1` even though four operations work. Any caller requiring full-contract correctness must treat this implementation as defective until its target-selection logic is repaired.
