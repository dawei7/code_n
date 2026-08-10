## General

**A rook has four independent lines of sight**

The rook attacks horizontally and vertically, so only four rays matter: up, right, down, and left from the rook's square. Along each ray, empty squares can be crossed, but the first encountered piece blocks every square beyond it.

Therefore, each direction contributes at most one capturable pawn:

- if the first piece is a black pawn, the rook attacks it;
- if the first piece is a white bishop, that direction contributes nothing;
- if the board edge is reached first, that direction also contributes nothing.

There is no need to simulate actual moves or examine diagonal squares.

**Locate the unique rook**

The nested loops scan the square board until `board[i][j] == "R"`. The statement guarantees exactly one rook, so once it is found, all four directional scans can be performed and the answer can be returned immediately.

The code stores `n = len(board)` and uses it for both row and column bounds. This is valid because the board is guaranteed to be `8 x 8`.

**Generate the four directions compactly**

The tuple

`dirs = (-1, 0, 1, 0, -1)`

combined with `pairwise(dirs)` produces:

- `(-1, 0)` for up;
- `(0, 1)` for right;
- `(1, 0)` for down;
- `(0, -1)` for left.

For direction `(a, b)`, the first examined square is `(i + a, j + b)`. Repeatedly adding the same offset walks along one straight rank or file exactly as a rook moves.

**Stop at bishops before entering their squares**

The directional loop continues while the coordinates remain in bounds and

`board[x][y] != "B"`.

A white bishop cannot be captured by the white rook and blocks all movement beyond itself. Because the condition fails before the loop body runs on the bishop square, that ray ends without increasing the answer.

The algorithm does not skip over bishops, which is the most important obstruction rule in the problem.

**Count a pawn and stop that direction**

Inside the loop, if `board[x][y] == "p"`, the rook can reach that pawn through the empty squares already crossed. The algorithm increments `ans` and executes `break`.

Stopping is essential. A pawn is itself a piece, so the rook cannot attack a second pawn behind the first in the same move. Even if capturing the first pawn would produce a new board position afterward, the question asks which pawns are attacked from the current board, not how many could be captured over multiple moves.

If the square is empty, neither blocking case applies, so `x, y = x + a, y + b` advances to the next square along the same ray.

**Why other board symbols need no branch**

The legal symbols are rook, empty, bishop, and pawn. The scan starts adjacent to the unique rook, so it will not encounter another rook. The while condition handles bishops, the inner condition handles pawns, and the remaining possible symbol is an empty square, which should simply be crossed.

This makes the control flow a direct representation of chess movement.

**Trace a direction**

Suppose the rook is at row three, column three. Looking right:

- column four is empty, so continue;
- column five contains a pawn, so count one and stop;
- any bishop or pawn at columns six or seven is irrelevant because the nearer pawn blocks the ray.

Looking downward, if a bishop occurs before a pawn, the while condition stops at the bishop and that direction contributes zero.

The same logic applies independently to the remaining two directions. The final answer is the sum of these four zero-or-one contributions.

**Why scanning only the first piece is sufficient**

A rook's legal path in one direction is the continuous sequence of squares before the first occupied square. If that first occupied square is an opponent pawn, the rook may move onto it and capture. If it is a friendly bishop, the rook must stop before it. No square after the first piece is reachable in the same move in either case.

Thus no pawn beyond the first piece can be attacked from the current rook position. The ray scan examines exactly the information required and no more.

**Why every attacked pawn is counted exactly once**

Any pawn attacked by the rook must share either its row or its column, placing it on exactly one of the four directional rays. There can be no blocking piece between them, so the scan in that direction reaches the pawn and counts it.

Conversely, every counted pawn is reached after crossing only empty in-bounds squares, so it is legally attackable. Different directions contain disjoint squares, and each direction stops after its first pawn, preventing duplicate counting. Therefore, `ans` equals the number of attacked pawns.

**Early return after the rook**

Once all four rays from the unique rook have been checked, later board cells cannot affect the answer except as cells already observed along those rays. Returning from inside the location scan avoids finishing the remaining search rows unnecessarily.

The guarantee of exactly one rook also ensures the method reaches a return statement. Without that guarantee, the Python function could fall through and return `None`, but such input is outside the contract.

## Complexity detail

The board dimensions are fixed at eight by eight. Scanning for the rook examines at most 64 cells, and the four rays examine at most seven squares each. These are fixed constants, so time complexity is `O(1)` and auxiliary space is `O(1)`.

For a generalized `N x N` board, locating the rook by a full scan would take `O(N^2)` time and the four rays another `O(N)`, still with `O(1)` space. Under the actual fixed-size contract, both are constant.

## Alternatives and edge cases

- **Scan complete rook row and column:** One can inspect all aligned squares and track blockers, but stopping at the first piece in each direction is simpler and avoids irrelevant cells.
- **Simulate rook moves:** Generate every reachable empty square and capture. This reaches the same result but adds state the direct ray scan does not need.
- **Precompute piece coordinates:** Building sets or maps is unnecessary for a fixed 64-cell board and uses extra memory.
- **Bishop immediately adjacent:** The ray loop stops before entering it, contributing zero.
- **Pawn immediately adjacent:** It is counted immediately, and that ray stops.
- **Several pawns in one direction:** Only the nearest pawn is attacked because it blocks every farther pawn.
- **Pawn behind a bishop:** It is not counted because the bishop terminates the ray first.
- **No piece before the edge:** The boundary condition ends the scan with no capture.
- **Rook on an edge or corner:** Some first neighbor coordinates are out of bounds, so those directions perform no iterations.
- **No capturable pawns:** All rays end at bishops or edges, and the initialized answer zero is returned.
- **Maximum result:** At most one pawn can be attacked in each of four directions, so the answer cannot exceed four.
- **Input preservation:** The board is read-only; the method changes only local coordinates and the counter.
