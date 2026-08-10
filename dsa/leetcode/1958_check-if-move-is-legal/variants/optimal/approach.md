## General

**A legal line must leave the move in one of eight directions**

The newly placed piece is one endpoint of a horizontal, vertical, or diagonal line. From its cell, the other endpoint must lie in one of eight direction vectors $(a,b)$ where each component is $-1$, $0$, or $1$, excluding $(0,0)$.

The nested loops enumerate exactly those eight directions. The board is not mutated; the algorithm treats `(rMove, cMove)` conceptually as the first endpoint of `color` and scans outward.

**Require opposite-colored middle cells**

For one direction, `i, j` start at the move cell and `cnt` starts at zero. Each while iteration first increments the distance and steps to the next board cell.

At distance one, finding another `color` piece must not succeed. A good line needs at least three cells, so there must be at least one middle cell. The check requires `cnt > 1` before accepting a same-colored endpoint.

If the visited cell is the same color too early, the second condition breaks. If it is free `"."`, the scan also breaks because a good line cannot contain gaps. The only way the scan continues is when the cell contains the opposite color.

After one or more opposite pieces, encountering `color` at distance two or greater returns true. This describes exactly:

new piece, one or more opponent pieces, same-colored closing piece.

**Why condition order matters**

The success test appears before `if board[i][j] in (color, "."): break`. At a valid far endpoint, the method must return true rather than treating the same color only as a stopping condition.

At the immediate neighbor, `cnt > 1` is false, so the same-color neighbor falls through to the break. That direction cannot skip over it to find a farther endpoint because middle cells must all be the opposite color.

**Why scanning every direction is sufficient**

Any good horizontal, vertical, or diagonal line with the move as an endpoint has a constant step direction among the eight enumerated vectors. The scan in that direction visits its cells consecutively. It passes through the opposite-colored middle and reaches the matching endpoint, returning true.

Conversely, a true return proves the distance is at least two, every earlier visited cell avoided both same color and free status and therefore was the opposite color, and the current cell matches `color`. Those cells form a good line with the move as one endpoint.

If all eight scans stop at an edge, free cell, or invalid same-colored neighbor without success, no possible line orientation qualifies and the function returns false.

**Why there is no explicit opponent-color variable**

The board alphabet is exactly `"."`, `"W"`, and `"B"`, while `color` is one of the two piece colors. After the code rules out `color` and `"."`, the only remaining value is the opposite color. Continuing the while loop therefore implicitly verifies every middle cell without computing a separate opponent variable.

This inference depends on the board contract. With more piece types or invalid symbols, “not my color and not empty” would not necessarily mean the unique opponent, and an explicit comparison would be required.

**A directional trace**

Suppose the played color is black and cells to the right are white, white, black. Distance one sees white and continues. Distance two sees white and continues. Distance three sees black with `cnt > 1` and returns true. If the sequence were white, free, black, the free cell would stop the scan before the distant black because lines cannot jump over it.

## Complexity detail

The board is fixed at $8$ by $8$. There are eight directions, and each scan takes at most seven steps before leaving the board. The operation count is bounded by a small constant, so time is $O(1)$ under the problem constraints.

Only direction variables, coordinates, and a counter are stored. Auxiliary space is $O(1)$.

For a generalized $B$-by-$B$ board, the same method would take $O(B)$ time because there are still eight directions but up to $B-1$ steps per direction.

The board is neither copied nor modified. This keeps working storage constant and avoids needing to restore the free move cell after an early return.

## Alternatives and edge cases

- **Temporarily write the move:** One may set the board cell to `color` and scan lines, then restore it. The exact method avoids mutation because the start color is already known.
- **Generate whole lines:** Extract row, column, and diagonals as strings and search patterns. This allocates unnecessary sequences and complicates endpoint direction.
- **Immediate same-color neighbor:** It cannot close a three-cell line, so that direction fails.
- **Exactly one opponent between endpoints:** Distance two satisfies `cnt > 1` and is the shortest legal line.
- **Several opponents:** The scan continues through all of them until a same-colored endpoint.
- **Free cell in the middle:** It breaks the line and stops that direction.
- **Opponent sequence reaches the edge:** Without a closing same-colored endpoint, that direction is invalid.
- **Board edge:** Leaving bounds simply ends that directional scan.
- **Move at a corner:** Only three directions enter the board, while the other scans terminate immediately.
- **Good line with move in the middle:** It does not qualify; scanning from the move requires the move to be an endpoint.
- **Multiple good directions:** The first found returns true, which is sufficient for legality.
- **Board remains unchanged:** The scan is observational, so callers retain the original free move cell.
- **Guaranteed free move cell:** The code relies on the contract and does not validate it separately.
