## General

The wall is built one complete row at a time. Two facts determine whether a row may sit above another:

- each row's brick widths must sum exactly to `width`;
- their internal brick boundaries, called seams, must not occur at the same horizontal position.

The exact solution first enumerates every legal single-row brick sequence, then builds a compatibility graph between row patterns, and finally uses dynamic programming across the wall's height.

Although the manifest describes seam masks, the stored source keeps each pattern as a list of brick widths and compares cumulative sums directly.

**Enumerate every exact-width row**

The recursive helper `dfs(v)` tracks the total width `v` already filled, while list `t` stores the chosen brick widths in order.

If `v > width`, the partial sequence has overshot the row and can never become valid because all brick widths are positive. The helper returns immediately.

If `v == width`, the current sequence fills the row exactly. A copy `t[:]` is appended to `s`. Copying matters because backtracking will continue modifying `t`; storing the same list object would corrupt all recorded patterns.

Otherwise, the helper tries every brick width `x`. It appends `x`, recursively explores total `v + x`, and then pops the choice so the next brick starts from the same prefix.

Because the brick supply is infinite, a width may be selected repeatedly. Because brick order changes seam positions, sequences such as `[1,2]` and `[2,1]` are correctly treated as different row patterns.

**Represent seams as cumulative widths**

For a row `a = [a0, a1, ...]`, its internal seams occur after cumulative sums `a0`, `a0 + a1`, and so on, excluding the final total `width`.

Helper `check(a, b)` walks these cumulative seams without constructing separate sets. Variables `s1` and `s2` begin at the first brick width of each row. Indices `i` and `j` identify the next brick to add.

If `s1 == s2` while both rows still have internal seams to consider, the rows join bricks at the same non-end position and are incompatible.

If `s1 < s2`, the helper advances row `a`'s seam by adding `a[i]`. Otherwise it advances row `b`. This is the standard merge of two sorted cumulative-position sequences: always move the smaller seam until a match is found or one sequence ends.

The loop stops when either row has no further internal seam. The common wall endpoint is deliberately not compared, because joins at the two ends are allowed. Reaching the end without a match returns true.

**Build a symmetric compatibility graph**

For each pattern index `i`, the code first checks whether the pattern is compatible with itself. That is possible only when it has no internal seam, such as a row made from one full-width brick. A multi-brick row shares every seam with itself and fails.

For each distinct pair `i < j`, one compatibility check is enough because the relation is symmetric. When it succeeds, `j` is added to `g[i]` and `i` to `g[j]`.

The adjacency list `g[j]` therefore contains exactly the row patterns that may be placed next to pattern `j`.

**Define the height dynamic program**

`dp[r][j]` is the number of sturdy partial walls of height `r + 1` whose newest row uses pattern `j`.

For the first row, every enumerated pattern is legal because there is no row below it. The initialization `dp[0][j] = 1` records one wall consisting solely of that pattern.

For every later level `i` and current pattern `j`, the code visits compatible previous patterns `k in g[j]` and adds `dp[i - 1][k]`. Each previous wall can be extended by row `j`, and no incompatible wall is admitted.

Modulo $10^9+7$ is applied after each addition, keeping numbers bounded while preserving the final remainder.

**Why the transition counts every sturdy wall once**

Any sturdy wall of height $r+1$ has one definite top-row pattern `j` and one definite pattern `k` directly below it. Sturdiness means `k` appears in `g[j]`. Removing the top row leaves a sturdy height-$r$ wall counted in `dp[r - 1][k]`, so the transition includes the original wall.

Conversely, every transition starts with a sturdy shorter wall and appends a compatible row. All older adjacent pairs remain unchanged, and the new adjacent pair has no shared seam, so the extended wall is sturdy.

The top pattern distinguishes transition destinations, so no wall is counted twice. Summing the last DP row over all possible top patterns counts every full-height sturdy wall exactly once.

If no exact-width row exists, `s` is empty, the DP rows are empty, and the final sum is zero, as required for a wall that cannot be built.

## Complexity detail

Let $W$ be `width`, $H$ be `height`, $R$ be the number of legal row patterns, and $E$ be the number of directed compatibility edges stored in `g`.

Enumerating and copying patterns costs at most $O(RW)$ plus failed recursive prefixes. A compatibility check merges two seam sequences in $O(W)$ time because a row contains at most $W$ unit-width bricks. Checking all pattern pairs therefore costs $O(R^2W)$. The height DP traverses compatibility edges for each later row, costing $O(HE)$. The dominant exact bound is $O(R^2W+HE)$ after pattern generation.

Stored pattern lists use $O(RW)$ space, the graph uses $O(E)$, and the exact full DP table uses $O(HR)$. Total auxiliary space is $O(RW+E+HR)$, plus recursion depth $O(W)$.

Because $W\le10$, the manifest suppresses the seam-comparison factor and states $O(R^2+HE)$. Its $O(R^2)$ space is a broad dense-graph view, but the exact source also retains all $H$ DP rows rather than rolling two rows.

## Alternatives and edge cases

- **Seam bitmasks:** Encode each internal boundary as one bit. Compatibility becomes `maskA & maskB == 0` in constant bitwise time, matching the manifest summary more literally.
- **Rolling DP rows:** Only the previous height is needed, so two length-$R$ arrays can reduce DP storage from $O(HR)$ to $O(R)$.
- **Matrix exponentiation:** Treat compatibility as a transition matrix and raise it to `height - 1`. This can help for enormous heights but is unnecessary for `height <= 100`.
- **No valid row pattern:** The answer is zero because no first row can be constructed.
- **Height one:** Every exact-width row is a valid wall, and the initialized DP row is summed directly.
- **One-brick row:** It has no internal seams and is compatible with itself.
- **Repeated row pattern:** It is permitted only when that pattern has no seam shared with itself, which means no internal seam.
- **Common endpoint:** The checker stops before treating `width` as a forbidden seam because wall ends may align.
- **Infinite supply:** DFS may reuse the same brick width any number of times.
- **Unique brick widths:** Different DFS choices are unambiguous, though ordering still creates distinct patterns.
- **Overshoot:** Positive widths mean a total above `width` can be pruned permanently.
- **Modulo arithmetic:** Reducing after every addition gives the same final remainder as reducing only at the end.
- **Pattern-copy requirement:** `t[:]` prevents later backtracking pops from changing stored rows.
- **Manifest discrepancy:** The implementation stores width lists and uses a full DP table, so exact time and space retain width and height factors.
