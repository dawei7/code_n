## General

At every move, the knight chooses uniformly from all eight geometrically possible knight moves. A move that leaves the board still consumes its probability share; the process then stops off the board and can never contribute to the success probability.

The exact solution uses bottom-up dynamic programming, but its state is easiest to understand backward rather than as probability mass traveling forward.

**The dynamic-programming state**

Define `f[h][i][j]` as:

> the probability that a knight starting on board cell `(i, j)` remains on the board after making exactly `h` further moves.

The coordinates are zero-indexed, and `0 <= i, j < n`.

This state directly matches the requested answer. The knight begins at `(row, column)` with `k` moves left, so the method eventually returns

`f[k][row][column]`.

The state is not the probability of being at `(i, j)` after `h` moves from the original start. That alternative forward interpretation leads to a different initialization and final summation. Here, each cell asks a survival question for a journey that starts there.

**Why every zero-move state equals one**

If the knight has zero moves left and is currently on a board cell, it has already succeeded: it remains on the board after exactly zero additional moves. Therefore,

$$
f[0][i][j]=1
$$

for every board cell.

This is why the code fills the entire `f[0]` layer with ones, not only the original starting cell. Later states for many starting cells depend on these base values.

**Generating the eight knight directions**

The expression

`pairwise((-2, -1, 2, 1, -2, 1, 2, -1, -2))`

takes adjacent pairs from a sequence of nine numbers. It produces these eight offsets:

- `(-2, -1)`
- `(-1, 2)`
- `(2, 1)`
- `(1, -2)`
- `(-2, 1)`
- `(1, 2)`
- `(2, -1)`
- `(-1, -2)`

Together they are exactly the combinations of moving two squares along one axis and one square along the other, with every sign and orientation represented once.

Using `pairwise` is a compact encoding choice. Correctness depends on the generated set containing all eight distinct knight moves, not on the order in which they are processed.

**The recurrence**

Suppose `h >= 1` and the knight starts at `(i, j)`. For an offset `(a, b)`, its chosen destination is

`(x, y) = (i + a, j + b)`.

Each of the eight offsets is selected with probability `1/8`.

If `(x, y)` is inside the board, the conditional probability of surviving the remaining `h-1` moves is `f[h - 1][x][y]`. That choice contributes

$$
\frac{f[h-1][x][y]}{8}
$$

to the current state.

If `(x, y)` lies outside the board, that choice contributes zero. The code simply does not add anything for it.

Summing all valid destinations gives

$$
f[h][i][j]
=
\frac{1}{8}
\sum_{\substack{(a,b)\text{ is a knight move}\\
0\le i+a<n\\
0\le j+b<n}}
f[h-1][i+a][j+b].
$$

The factor remains `1/8` even when fewer than eight moves stay on the board. The knight chooses among all eight moves uniformly, not only among legal destinations. Renormalizing by the number of in-bounds moves would solve a different probability experiment.

In the code, division by eight occurs for each added valid destination:

`f[h][i][j] += f[h - 1][x][y] / 8`.

This is algebraically the same as adding all valid previous values and dividing their sum by eight once.

**Why layers are filled in increasing move count**

Every state in layer `h` depends only on layer `h-1`. The outer loop runs `h` from `1` through `k`, so all prerequisite states are complete before they are read.

Within one layer, cell order does not matter because no state reads another state from the same layer. The nested `i` and `j` loops merely visit every possible starting cell.

**A trace from a corner**

On a `3 x 3` board, start at `(0, 0)` with one move. Only destinations `(1, 2)` and `(2, 1)` are on the board. Since every zero-move destination state equals one,

$$
f[1][0][0]
=
\frac{1}{8}+\frac{1}{8}
=
\frac{1}{4}.
$$

With two moves, the recurrence looks up `f[1][1][2]` and `f[1][2][1]` and again divides each by eight. Each of those edge cells has two surviving next moves, so each value is `1/4`. Therefore,

$$
f[2][0][0]
=
\frac{1}{8}\cdot\frac{1}{4}
+
\frac{1}{8}\cdot\frac{1}{4}
=
\frac{1}{16}
=
0.0625.
$$

This matches the two-stage probability: two of eight first moves survive, and from either surviving cell two of eight second moves survive.

**Why the recurrence is correct**

For zero moves, the base value one is correct for every on-board starting cell.

Assume layer `h-1` correctly gives survival probabilities for every cell. From `(i, j)` with `h` moves remaining, the first chosen move partitions all outcomes into eight equally likely, mutually exclusive cases. Off-board cases have success probability zero. In-board case `(x, y)` has success probability `f[h-1][x][y]` by the induction assumption.

The law of total probability says that the current survival probability is the sum of each case's probability `1/8` times its conditional success probability. That is exactly the recurrence. By induction, all layers through `k` are correct, including the returned starting state.

## Complexity detail

There are `k+1` layers, each containing `n^2` cells. For each of the `k n^2` non-base states, the code examines exactly eight offsets. Eight is constant, so the running time is

$$
O(k n^2).
$$

The exact implementation allocates the full three-dimensional list `f` with `(k+1)n^2` numeric entries. Its auxiliary space usage is therefore

$$
O(k n^2).
$$

This literal space bound is important: although the recurrence needs only the immediately preceding layer and can be optimized to `O(n^2)` space, the checked-in code retains every layer.

The direction tuple and loop variables take constant extra space beyond the DP table.

## Alternatives and edge cases

- **Two-layer bottom-up DP:** Keep only `previous` and `current` `n x n` boards because layer `h` reads only `h-1`. This preserves `O(k n^2)` time and reduces space to `O(n^2)`.

- **Top-down memoization:** Recursively define survival from `(moves, i, j)` and cache states. It computes the same recurrence and may skip unreachable states, but recursion depth is `k` and the cache can still contain `O(k n^2)` entries.

- **Forward probability propagation:** Initialize probability one only at `(row, column)`, distribute each cell's mass to valid destinations with factor `1/8`, and sum the final layer. This is equally correct but uses a different state meaning.

- **Naive enumeration of move sequences:** Exploring all eight choices for every move takes `O(8^k)` time because identical state subproblems are recomputed. DP merges journeys that reach the same cell with the same number of moves remaining.

- **`k = 0`:** The answer is `1` for every valid starting cell. The loops over positive layers do not run, and `f[0][row][column]` is returned.

- **`n = 1` with positive `k`:** Every knight move leaves the board. The first positive layer remains zero at the only cell, and all later layers also remain zero.

- **Corner and edge cells:** They have fewer in-board destinations, but invalid choices retain their zero contribution. The denominator must stay eight.

- **Starting cell validity:** The source guarantees `row` and `column` are within the board, so the final indexing is safe.

- **Floating-point arithmetic:** Repeated division by eight is exactly representable in binary for these dyadic fractions, although summation still uses floating-point values. The returned tolerance allowed by the platform comfortably covers the calculation.

- **Direction completeness:** Omitting or duplicating one pairwise offset would distort probability because every listed move carries a separate `1/8` share.

- **State interpretation:** Filling `f[0]` entirely with ones is correct only for the backward “survival from this cell” definition. Mixing it with a forward “probability at this cell” interpretation would be a fundamental bug.
