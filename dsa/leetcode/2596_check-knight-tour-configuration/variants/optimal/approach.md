## General

**The grid gives visit times, not a path directly**

Each cell stores when the knight visited it. To validate the tour, the useful order is the reverse mapping:

`visit number -> cell coordinates`.

The solution builds array `pos` of length $n^2$. When it sees `grid[i][j] = t`, it stores `pos[t] = (i,j)`. Because the matrix contains every distinct integer from zero through $n^2-1$, every position in `pos` is filled exactly once.

After inversion, `pos[0]` is the starting cell, `pos[1]` is the next cell, and so on. The tour can be validated by checking consecutive coordinate pairs.

**Check the required starting cell first**

A valid tour must begin at the top-left cell. Since visit numbers are zero-indexed, `grid[0][0]` must equal zero.

The condition `if grid[0][0]: return False` uses Python truthiness: zero is false, while every positive visit number is true. Thus any nonzero top-left label is rejected immediately.

The distinct complete-label guarantee then ensures visit zero appears nowhere else when this check passes.

**Recognize one legal knight move**

A knight changes one coordinate by two cells and the other by one. Direction signs do not matter, so the code computes absolute differences:

`dx = abs(x1 - x2)` and `dy = abs(y1 - y2)`.

The move is legal exactly when

$$
(dx,dy)=(1,2)
\quad\text{or}\quad
(dx,dy)=(2,1).
$$

These two cases cover all eight directional moves: each coordinate change can be positive or negative, and the one-step and two-step roles may be exchanged.

A move such as $(2,2)$ is diagonal but not a knight move. A move such as $(0,1)$ is adjacent but also invalid.

**Check every consecutive visit**

`pairwise(pos)` produces

$$(pos[0],pos[1]),(pos[1],pos[2]),\ldots.$$

These are exactly the moves the labeled configuration claims the knight made. If any pair fails the knight-difference test, the function returns false immediately.

If every pair passes, the labels already guarantee that every board cell appears once in the sequence. Therefore the path starts at the required cell, moves legally each time, and visits all cells exactly once. The function returns true.

**Why no visited set is needed**

Normally, validating a tour might require marking cells to detect repetition. Here, the input contract guarantees all labels are distinct and cover the complete range. The inverse array therefore contains every cell exactly once.

That guarantee proves the “visits every cell exactly once” part before movement validation begins. The code needs only coordinate ordering and consecutive-move checks.

**Trace a short failure**

Suppose visit seven is at $(2,1)$ and visit eight is at $(1,1)$. Their absolute differences are $(1,0)$. Neither arrangement is $(1,2)$ or $(2,1)$, so the claimed eighth move is invalid and the configuration is rejected.

It does not matter whether later labels would form legal moves. A tour with one illegal transition cannot be valid, so early return is correct.

**Why checking only consecutive labels is sufficient**

The knight moves from visit $t$ directly to visit $t+1$. There is no movement requirement between nonconsecutive visits such as $t$ and $t+2$ because another cell lies between them.

Validating all $n^2-1$ adjacent time pairs therefore checks every actual edge of the claimed path and no irrelevant pairs.

**Coordinate and label indexing**

Rows and columns are zero-indexed, as are visit labels. `pos` uses the label directly as an array index, avoiding any plus-one conversion. A mismatch here would shift the whole tour, but the exact mapping preserves the statement's convention.

The board size is at least three, but the algorithm does not rely on existence of a valid tour for every size; it simply validates the provided sequence.

## Complexity detail

There are $n^2$ cells. Building `pos` visits each once in $O(n^2)$ time. `pairwise` produces $n^2-1$ transitions, each checked in constant time, so total time is $O(n^2)$.

The inverse coordinate array stores one pair per cell and uses $O(n^2)$ space. Loop variables use constant additional space. The input grid is not modified.

## Alternatives and edge cases

- **Search for each next label:** Repeatedly scanning the grid for visit $t+1$ would take $O(n^4)$ time; inversion makes every lookup direct.
- **Sort coordinate-label triples:** Sorting all cells by label also works in $O(n^2\log n)$ time but ignores the dense complete label range.
- **Wrong starting label:** Any nonzero `grid[0][0]` fails before other work.
- **Illegal final move:** `pairwise` includes the transition to label $n^2-1$, so it is checked.
- **All labels unique:** The contract makes a separate duplicate-cell or missing-label check unnecessary.
- **Reversed knight displacement:** Both $(1,2)$ and $(2,1)$ are accepted.
- **Direction signs:** Absolute differences cover left, right, up, and down variants.
- **Nonconsecutive cells:** They need not be a knight move and are intentionally not compared.
- **Input preservation:** Only the new `pos` array is written.
