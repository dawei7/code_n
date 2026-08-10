## General

**Compress one row into a base-three state**

Each grid cell has three possibilities: empty, occupied by an introvert, or occupied by an extrovert. With `n` columns, one complete row therefore has $3^n$ possible configurations. The source sets `mx = 3^n` and represents every row by an integer from zero through `mx - 1`.

The base-three digits of a row mask describe its cells:

- digit `0` means empty;
- digit `1` means introvert;
- digit `2` means extrovert.

For every mask `i`, the preprocessing loop repeatedly calls `divmod(mask, 3)`. The remainder `x` is the next base-three digit, stored as `bits[i][j]` for column `j`, while the quotient becomes the remaining unprocessed digits. This gives direct access to every occupant type without repeatedly decoding masks during the main search.

The arrays `ix` and `ex` record how many introverts and extroverts each row uses. They let the recursion reject a row configuration immediately if it requires more people than remain.

**Count the complete effect of one adjacent pair**

Happiness is a sum over people, but it is convenient to account for each adjacency as one combined pair contribution. The table `h` is indexed by the two occupant types.

An introvert-introvert pair makes each person lose `30`, for a total of `-60`. An introvert-extrovert pair makes the introvert lose `30` and the extrovert gain `20`, for a net `-10`. An extrovert-extrovert pair lets both gain `20`, for `+40`. Any pair involving an empty cell contributes zero. This produces

`h = [[0, 0, 0], [0, -60, -10], [0, -10, 40]]`.

The matrix is symmetric because the combined effect does not depend on which member is considered first.

For each row mask, `f[mask]` stores all happiness internal to that row. The decoder adds `120` for every introvert and `40` for every extrovert. Whenever `j > 0`, it also adds `h[x][bits[i][j - 1]]` for the horizontal adjacency between the current cell and its left neighbor. Each horizontal edge is counted exactly once, when its right endpoint is decoded.

For every pair of row masks, `g[pre][cur]` stores their vertical interaction. The triple loop adds `h[bits[pre][k]][bits[cur][k]]` for each column `k`. Each vertical edge between these two rows is counted exactly once. Together, `f[cur] + g[pre][cur]` is the full new happiness introduced when row `cur` is placed below row `pre`.

**The cached row-by-row state**

`dfs(i, pre, ic, ec)` returns the maximum additional happiness obtainable from row `i` onward when:

- `pre` is the configuration of row `i - 1`;
- `ic` introverts remain available;
- `ec` extroverts remain available.

The initial call is `dfs(0, 0, introvertsCount, extrovertsCount)`. Mask zero is an entirely empty row, so it correctly represents the nonexistent row above the grid and contributes no vertical interactions.

At a state, the method tries every possible current row `cur`. It considers the row only if `ix[cur] <= ic` and `ex[cur] <= ec`. Its immediate contribution is `a = f[cur] + g[pre][cur]`. The recursive call advances to row `i + 1`, makes `cur` the previous row, and subtracts the people used. Adding the immediate and future values gives the happiness of that complete choice. `ans` keeps the maximum over all feasible rows.

The empty row mask is always feasible. This matters because the problem does not require placing everyone. The recursion can leave individual cells or entire remaining rows empty whenever additional people would lower the result.

The `@cache` decorator memoizes results by the full tuple `(i, pre, ic, ec)`. Different earlier layouts that lead to the same previous row and remaining counts have identical choices from this point onward; rows above `pre` can no longer interact with future rows. Reusing the stored result avoids recomputing that suffix problem.

**Why only the previous row is needed**

A person interacts only with north, east, south, and west neighbors. Horizontal interactions inside the current row are already included in `f[cur]`. When adding the row, its north interactions are exactly `g[pre][cur]`. Its south interactions are intentionally postponed until the next row is chosen. No cell in a row two levels above is adjacent to the current row, so older row masks cannot affect future happiness.

This locality is what makes row-profile dynamic programming possible. The state remembers precisely the boundary through which the processed and unprocessed grid portions can still interact.

**Why the recurrence reaches the global maximum**

Every grid placement corresponds to exactly one sequence of `m` row masks. At each recursion level, the loop includes that placement’s current mask if its remaining-person counts make the placement legal. The recurrence adds every person’s base happiness once, every horizontal edge once through `f`, and every vertical edge once through `g`. Thus it calculates that placement’s exact total happiness.

Conversely, every sequence considered by the recursion defines a legal placement: each cell digit has one occupant type, the count tests prevent using too many people, and choosing zero leaves cells unused. Taking the maximum over all feasible row masks at every state therefore compares all legal grids. The base case returns zero after row `m - 1` because no cells remain.

The second base condition, `ic == 0 and ec == 0`, is also safe. With no people available, every remaining row would be empty and add zero, so recursion can end early. By exhaustive choice plus exact scoring, the initial call returns the maximum possible grid happiness.

## Complexity detail

Let `R = m`, `C = n`, `I = introvertsCount`, and `E = extrovertsCount`. There are $P = 3^C$ row patterns.

Decoding row masks and computing `f`, `ix`, and `ex` costs $O(CP)$. Precomputing every vertical compatibility score `g[pre][cur]` examines $P^2$ row pairs and `C` columns, costing $O(CP^2) = O(C9^C)$ time and $O(P^2) = O(9^C)$ space.

The memoized recursion has at most $O(RP(I+1)(E+1))$ states. Each state loops over all `P` current row patterns, so its worst-case transition time is $O(RP^2(I+1)(E+1))$, or $O(R9^C(I+1)(E+1))$. The preprocessing term is subsumed by this bound for nontrivial counts.

The cache uses $O(RP(I+1)(E+1))$ space. Including `g`, `bits`, and the row arrays, total auxiliary space is $O(R3^C(I+1)(E+1) + 9^C)$. Recursion depth is at most `R`.

The manifest’s displayed $O(RC3^C(I+1)(E+1))$ time omits the exact source’s loop over every `cur` pattern inside each cached `pre` state. The implementation shown here has the $9^C$ worst-case transition factor just derived. With `C <= 5` and both people counts at most six, it remains practical.

## Alternatives and edge cases

- **Cell-by-cell profile DP:** Process one cell at a time while keeping the previous `n` cell types as a ternary mask. This can reduce some row-pair preprocessing, but transitions and mask shifting are more intricate.
- **Backtracking over all cells:** Trying empty, introvert, and extrovert choices without memoization explores roughly $3^{RC}$ layouts and repeats many suffix problems. The cached boundary state is the essential optimization.
- **Precompute only compatible row pairs:** Filtering pairs by remaining counts or storing transition lists can reduce constants, but the same row-profile recurrence and exponential dependence on the column count remain.
- **Transpose the grid:** A profile algorithm is usually fastest when the number of columns is the smaller dimension because the exponent is `C`. This exact source does not swap `m` and `n`, though both are bounded by five.
- **No available people:** The initial state satisfies the early base condition and correctly returns zero.
- **People may remain unused:** Empty digits and empty rows are always options; the recurrence never forces a harmful placement merely because someone remains.
- **One row:** Only `f[cur]` matters because the initial previous mask is empty and there are no later vertical edges.
- **One column:** Horizontal contributions in `f` vanish, while `g` handles the vertical chain exactly.
- **Introvert next to introvert:** The pair contribution is `-60`, not `-30`, because both people lose `30`.
- **Introvert next to extrovert:** The net is `-10`, combining one loss of `30` with one gain of `20`.
- **Extrovert next to extrovert:** The pair contributes `+40` because both extroverts gain `20`.
- **Counts exceed profitable placements:** The ≤ checks cap usage, while the empty configuration lets the optimum stop placing people.
- **Cache identity:** Omitting `pre` would be incorrect because the same remaining counts can have different vertical effects depending on the row directly above.
