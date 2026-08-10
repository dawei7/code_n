## General

**Count boundary shapes instead of constructing boards**

Trying every placement branches rapidly. Many different partial placement histories become equivalent once everything except the right boundary is filled.

Dynamic programming keeps only the boundary information that determines how the next one or two columns may be completed. A height-two board has very few relevant boundary shapes, so the exact solution compresses them into four counts.

Let the loop have already processed a board width `i`. Interpret `f` as:

- `f[0]`: `F_i`, the number of completely tiled boards of width `i`;
- `f[1]`: `A_i`, one orientation of a one-cell offset at the right boundary;
- `f[2]`: `B_i`, the vertically mirrored boundary orientation;
- `f[3]`: `F_{i-1}`, the previous complete-board count retained as a one-step lag.

The two partial states are kept separately even though symmetry makes their numeric counts equal. Keeping both makes every local transition explicit and avoids hiding the two orientations inside a multiplication by two.

**Understand the empty-board initialization**

Before processing any columns, there is exactly one way to tile a board of width zero: place nothing. Thus `F_0 = 1`.

No partial boundary exists at width zero, and the lag value before `F_0` contributes zero. This gives:

`f = [1, 0, 0, 0]`.

Counting the empty board as one is a standard dynamic-programming base case. It allows the same transition to create the first real tilings without special logic inside the loop.

**Enumerate the local transition into a complete board**

For the next width `i + 1`, a completely tiled boundary can arise in four disjoint ways:

- From `F_i`, append one vertical domino in the new column.
- From `F_{i-1}`, append two horizontal dominoes spanning the last two columns.
- From boundary state `A_i`, place the corresponding L-shaped tromino that fills its offset.
- From mirrored boundary state `B_i`, place the mirrored tromino.

These cases are disjoint according to the rightmost tile configuration and cover every way a full tiling can end. Therefore:

$$
F_{i+1}=F_i+A_i+B_i+F_{i-1}.
$$

The code writes this directly as:

`g[0] = f[0] + f[1] + f[2] + f[3]`,

followed by reduction modulo $10^9+7$.

**Advance the two partial boundary states**

Enumerating placements that leave boundary orientation `A` at the new right edge gives two sources:

- continue the mirrored partial orientation `B_i` across the new column with the compatible domino placement;
- start the offset from a fully tiled board of width `i - 1` using the appropriate rotated tromino over the final two columns.

Thus:

$$
A_{i+1}=B_i+F_{i-1}.
$$

By vertical symmetry:

$$
B_{i+1}=A_i+F_{i-1}.
$$

These are the assignments:

`g[1] = f[2] + f[3]`

and

`g[2] = f[1] + f[3]`.

The cross-reference between `f[1]` and `g[2]` reflects which boundary orientation remains after the local extension. The two values stay equal from symmetric initialization, but treating them as separate states proves that neither physical orientation has been lost.

**Carry the lagged complete count**

For the next iteration, the value called `F_{(i+1)-1}` must be the current `F_i`. Therefore:

`g[3] = f[0]`.

This fourth entry is not a new kind of tiling. It is rolling memory that makes the two-column transitions possible without storing a length-`n` array.

After all four new values are computed from the old vector, the assignment `f = g` advances the processed width by one.

**Why a separate new vector matters**

Every recurrence for width `i + 1` must read only counts for width `i` and the retained `i - 1` value. If the code overwrote `f` entries one at a time, a later transition could accidentally combine new-width and old-width counts.

Creating `g` freezes the previous state for the whole iteration. Both arrays have length four, so this clarity does not change the constant-space bound.

**Trace the first three widths**

At width zero:

`f = [1,0,0,0]`.

After one iteration:

`f = [1,0,0,1]`.

There is one complete tiling of a `2 x 1` board: one vertical domino. The final entry now remembers `F_0 = 1`.

After the second iteration:

`f = [2,1,1,1]`.

The two full tilings are two vertical dominoes or two horizontal dominoes. Each partial orientation has one configuration, and the lag remembers `F_1 = 1`.

After the third iteration:

`f = [5,2,2,2]`.

The full count five matches the example. The transition computed it as `2 + 1 + 1 + 1`: extend a width-two full tiling vertically, complete either partial orientation, or add the two-horizontal ending to a width-one full tiling.

**Relationship to the usual full-and-partial recurrence**

Because vertical reflection gives `A_i = B_i`, call their common value `P_i`. The four-state equations reduce to:

$$
F_{i+1}=F_i+F_{i-1}+2P_i
$$

and

$$
P_{i+1}=P_i+F_{i-1}.
$$

These are the standard full-board and one-corner-partial recurrences. The exact code simply expands the two symmetric partial orientations and carries `F_{i-1}` in one compact vector.

**Apply the modulus during every transition**

Counts grow exponentially with width. Addition is compatible with modular arithmetic:

$$
(a+b)\bmod M
=
((a\bmod M)+(b\bmod M))\bmod M.
$$

Reducing `g[0]`, `g[1]`, and `g[2]` at each iteration keeps integers bounded while preserving the required final remainder. `g[3] = f[0]` is already reduced from the previous iteration.

**Why the returned component is correct**

The state invariant says `f[0] = F_i` after `i` iterations. Initialization establishes it for zero. The transition enumerates every legal right-boundary completion once and establishes it for `i + 1`.

After exactly `n` iterations, `f[0]` is therefore the number of complete tilings of the `2 x n` board, modulo the required value. Partial states are internal aids and are not returned.

## Complexity detail

The loop executes once per column. Each iteration performs a constant number of additions, modulus operations, and four-element assignments, so time is $O(n)$.

At most two four-element lists, `f` and `g`, coexist. Their size does not depend on `n`, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Two-array full/partial DP:** Store `F_i` and one symmetric `P_i` for every width. It is intuitive but uses $O(n)$ space unless rolled.

- **Three-term full-only recurrence:** Eliminating the partial state yields `F_i = 2F_{i-1}+F_{i-3}` and supports another constant-space $O(n)$ solution.

- **Matrix exponentiation:** Encode the linear recurrence in a fixed matrix to reach $O(\log n)$ time, with greater implementation complexity.

- **Backtracking over placements:** It constructs exponentially many boards and repeatedly solves equivalent boundary states.

- **Width one:** The first transition returns the single vertical-domino tiling.

- **Symmetric partial states:** Their counts are equal, but both orientations contribute separately to a complete tiling.

- **Fresh next-state vector:** It prevents current-iteration updates from contaminating other transitions.

- **Modulo placement:** Reducing every newly computed count is safe and prevents unnecessarily large values.

- **Empty-board base:** Although `n >= 1`, `F_0 = 1` is required to seed the uniform recurrence.
