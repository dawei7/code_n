## General

**Use two states for each row**

On a row, a route may arrive from below and then optionally make one horizontal move. It may not make two horizontal moves consecutively.

The source distinguishes:

- `entered[c]`: routes that have just started on or moved upward into column `c`;
- `routes[c]`: routes ready to leave the row upward, including both no horizontal move and exactly one horizontal move.

Applying horizontal spreading only once from `entered` prevents a second same-row step.

**Compute a bounded column sum with prefixes**

`spread(values,row,radius)` returns, for each available destination column `c`, the sum of `values[x]` over

$$
|x-c|\le\texttt{radius}.
$$

A prefix-sum array makes each interval sum constant time. The bounds are clipped to columns zero through `width-1`. Blocked destinations return zero.

The interval includes `x=c`. In a horizontal spread, this center term represents making no same-row move, not a forbidden move that stays in place. Terms with `x\ne c` represent one actual horizontal move.

**Initialize all possible bottom starts**

`entered` begins with one at every available bottom cell and zero at blocked cells. Each one is the route consisting of choosing that starting cell.

`routes = spread(entered,bottom,d)` then counts:

- the unchanged start through the center term;
- every optional final horizontal move of distance at most `d`.

This also handles a one-row grid, where routes may end immediately or after one legal same-row move.

**Derive the upward horizontal radius**

An upward move changes row by exactly one. If its column displacement is $h$, Euclidean distance is

$$
\sqrt{1+h^2}.
$$

The move is legal when $1+h^2\le d^2$, so

$$
|h|\le\left\lfloor\sqrt{d^2-1}\right\rfloor.
$$

The source computes this exactly with `isqrt(d*d-1)`, avoiding floating-point rounding.

**Process each higher row in two phases**

Rows are visited from just above the bottom through the top.

First,

`entered = spread(routes,row,upward_radius)`

counts every legal upward move from the lower row into each available current cell.

Second,

`routes = spread(entered,row,d)`

allows no horizontal move through the center contribution or one horizontal move to another available cell within distance `d`.

Because the second spread reads `entered` rather than its own output, it cannot chain horizontal moves. The next iteration necessarily moves upward, satisfying the turn rule.

**Why routes are neither missed nor duplicated**

Every valid route has a unique state when it first enters each row. Its upward predecessor lies within `upward_radius`, so the first spread counts it exactly once.

On that row, the route either leaves from the entered cell without a horizontal move or chooses one distinct destination within radius `d`. The second spread has exactly one corresponding source-destination term.

Conversely, every counted transition joins available cells, respects the distance bound, moves upward or horizontally as appropriate, and never follows a horizontal move with another horizontal move. The DP therefore has a one-to-one correspondence with legal cell sequences.

At the top row, `routes` includes routes ending immediately after entry and routes whose final move is horizontal, both permitted. Summing all top columns counts every possible endpoint.

**Trace the one-row example**

For grid `[".."]` and `d=1`, `entered=[1,1]`. Horizontal spreading gives `routes=[2,2]`.

At column zero, the two routes are starting there and moving from column one to zero. Column one has the symmetric two. Their sum is four, matching the example.

**Reduce every accumulation modulo the required value**

Prefix entries, interval differences, and the final sum are reduced modulo $10^9+7$. Modular addition and subtraction preserve the final route count residue.

Python's `%` converts a negative prefix difference back into the canonical nonnegative residue.

## Complexity detail

One `spread` builds a prefix array and an output array in $O(M)$ time and $O(M)$ space. The bottom uses one spread, and each of the remaining $N-1$ rows uses two.

Total time is $O(NM)$. Only a constant number of width-$M$ arrays are live, so auxiliary space is $O(M)$.

## Alternatives and edge cases

- **Try every source-destination pair:** This adds an extra factor of `M`; prefix windows reduce each row transition to linear time.
- **Use radius `d` for upward moves:** Vertical distance already consumes one unit squared, so the correct radius is $\lfloor\sqrt{d^2-1}\rfloor$.
- **Exclude the interval center:** The center represents no optional horizontal move and must be counted.
- **Spread `routes` horizontally twice:** That would allow consecutive same-row moves.
- **Blocked destination:** `spread` forces its count to zero regardless of incoming sums.
- **Blocked source:** Its prior DP value is already zero.
- **One-row grid:** Starts and at most one final horizontal move are counted.
- **No available bottom cell:** Initialization is all zero and the answer remains zero.
- **`d=1`:** Upward radius is zero, so upward moves must stay in the same column.
- **Final horizontal move:** It is legal because no following move is required.
- **Move to the same coordinate:** The center term means omitting a move, not adding a duplicate zero-length step.
- **Modulo subtraction:** Python's remainder normalization keeps results nonnegative.
- **Memory:** Rows are processed incrementally; no $N\times M$ DP table is stored.
