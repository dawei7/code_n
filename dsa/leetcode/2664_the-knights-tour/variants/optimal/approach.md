## General

**Represent visit order directly on the board**

Matrix `g` starts filled with `-1`, meaning unvisited.

The starting cell receives zero. Every later chosen cell receives one more than the current cell:

`g[x][y] = g[i][j] + 1`.

Thus, if a complete tour is found, board values zero through $mn-1$ encode the exact visit order.

The same matrix serves as both output and visited structure.

**Enumerate all eight knight moves**

The sequence passed to `pairwise` produces:

$$
(-2,-1),(-1,2),(2,1),(1,-2),
(-2,1),(1,2),(2,-1),(-1,-2).
$$

Each offset changes one coordinate by one and the other by two in absolute value, exactly matching a knight move.

For candidate $(x,y)$, the code requires:

- row within zero through $m-1$;
- column within zero through $n-1$;
- `g[x][y] == -1`.

The last condition prevents revisiting a cell.

**Depth-first search tries one path**

At current cell, DFS loops through legal unvisited knight destinations.

It tentatively labels a destination with the next visit number and recursively continues from there.

This extends the current partial tour by exactly one cell. The recursion stack implicitly stores the chosen path.

**Backtrack from a dead end**

If recursive exploration does not complete the board, control returns.

The code resets:

`g[x][y] = -1`.

This erases the tentative choice so another move from the parent can reuse that cell in a different candidate tour.

Without resetting, failed-path cells would remain falsely unavailable and valid tours could be missed.

**Recognize completion**

The starting label is zero. After visiting every one of $mn$ cells, the final label must be $mn-1$.

At the top of DFS:

`if g[i][j] == m * n - 1`

sets global `ok = True` and returns.

No separate count is needed because the label itself equals the number of moves made.

**Preserve the successful path**

After a recursive call, the parent checks `if ok: return` before resetting the child cell.

Once a tour is found, true propagates through every active recursion frame. Each frame returns immediately, leaving all successful labels in `g`.

The outer function then returns the completed board.

**Why backtracking is complete**

At each partial path, the loop considers every legal unvisited knight move in a fixed order.

Every possible knight tour beginning with that partial path must choose one of those moves next. Recursion explores all continuations of each choice, and backtracking restores state between choices.

Therefore, if a full tour exists, exhaustive search eventually reaches it. The input guarantee ensures at least one does.

**Trace the one-cell board**

For $m=n=1$, starting cell is labeled zero.

DFS immediately sees:

$$
0=mn-1.
$$

It sets `ok` and returns `[[0]]` without trying moves.

**Why the board contains a valid tour**

Every nonzero label is assigned from a cell carrying the preceding label via one of the eight knight offsets. No cell receives two labels simultaneously because only `-1` cells are entered.

Completion means all $mn$ distinct cells received labels zero through $mn-1$. Reading cells by increasing label therefore gives a sequence that starts at $(r,c)$, uses legal knight moves, and visits every cell exactly once.

**Exact source versus the manifest summary**

The manifest says moves are prioritized by the fewest remaining exits, known as Warnsdorff's rule.

The exact stored source does not compute onward degrees or sort candidates. It explores the fixed offset order shown above.

This remains correct under exhaustive backtracking but can explore more branches. The explanation and exponential complexity refer to the actual implementation.

**Why constraints make search possible**

There are at most 25 cells. The theoretical search tree is huge, but the guarantee of a solution and early successful return often avoid exploring every path.

Still, no polynomial worst-case guarantee follows from the exact plain backtracking.

**Global flag versus Boolean return**

`ok` is captured with `nonlocal`. A Boolean return from DFS could encode the same success signal.

The flag allows every frame to test one shared completion state and preserve the board without changing the helper's return type.

## Complexity detail

At each of up to $mn$ path positions, at most eight moves are attempted. A coarse worst-case bound is $O(8^{mn})$ time, though visited constraints substantially prune actual search.

Board `g` uses $O(mn)$ space. Recursion depth is at most $mn$, so call-stack space is also $O(mn)$.

## Alternatives and edge cases

- **Warnsdorff ordering:** Try the legal destination with fewest onward moves first; often dramatically faster and matches the manifest summary.
- **Bitmask visited state:** Useful for memoized Hamiltonian-path search, but state space can still be exponential.
- **Iterative backtracking:** Avoids recursion but needs an explicit path stack.
- **One-cell board:** Starting cell already completes the tour.
- **No revisits:** Only cells labeled `-1` are candidates.
- **Failed branch:** Its tentative label must be reset.
- **Successful branch:** Early returns must happen before reset to preserve output.
- **Fixed move order:** Affects runtime and which valid tour is returned, not correctness.
- **Guaranteed solution:** The function relies on it and has no separate failure return.
- **Small board:** At most 25 recursive levels fit comfortably.
