## General
**Locate the unique rook:** Scan the fixed board until finding `'R'`. Its row and column are the common starting coordinates for all four possible attack rays.

**Inspect the first piece in each direction:** For each of up, down, left, and right, advance one square at a time. Empty squares do not change the ray. On reaching a bishop, stop because it blocks everything beyond it. On reaching a pawn, count one capture and stop because that pawn is itself the first blocking piece. Reaching the board boundary also ends the ray.

A rook attacks at most one pawn in each direction: any nearer piece prevents it from reaching a farther square in the same move. Thus examining the first nonempty square on all four rays counts every attacked pawn exactly once.

## Complexity detail
The board always has 64 cells. Locating the rook examines at most 64 cells, and the four rays inspect at most seven squares each, so both time and auxiliary space are $O(1)$ over the fixed public domain.

## Alternatives and edge cases
- **Scan the rook's full row and column:** This remains constant-time on an 8×8 board, but it must still preserve nearest-blocker order in both directions.
- **Chess move simulation:** Building a general chess engine adds unrelated rules and state without improving this fixed one-move visibility query.
- **Pawn behind a bishop:** The bishop ends the ray, so the pawn cannot be captured.
- **Second pawn on one ray:** The nearer pawn is capturable and blocks the farther pawn.
- **Rook at an edge or corner:** Directions that immediately leave the board contribute no capture.
