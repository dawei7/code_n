## General
**Check the turn counts**

Because `X` starts and turns alternate, the number of `X` marks must equal the number of `O` marks or exceed it by exactly one. Every other count difference is impossible.

**Check wins against the last mover**

Inspect the three rows, three columns, and two diagonals for each player. If `X` has won, `X` must have made the most recent move, so its count must be one larger. If `O` has won, the counts must be equal. These rules also reject simultaneous winners because they demand incompatible turn counts.

The count condition constructs the only possible next-player parity. With no winner, any ordering of the existing marks that alternates players and places the shown squares is legal because play has not been forced to stop. With a winner, the corresponding count condition places that winning mark on the final turn; its marks can be ordered so the completing square is last. Therefore the count and winner conditions are sufficient as well as necessary.

## Complexity detail
The board always contains exactly nine cells and eight winning lines. Counting marks and checking those lines takes constant $O(1)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Line-sum encoding:** Map `X` and `O` to signed values and inspect row, column, and diagonal sums; this expresses the same constant-time checks.
- **Generate every reachable state:** Simulate all alternating move histories and store their boards; this is feasible only because the board is fixed, but does far more work.
- **Backtrack through occupied squares:** Testing all move orders grows factorially with the number of marks.
- **Empty board:** It is the valid initial state.
- **Only one `X`:** This is a valid state after the opening move.
- **Winner with wrong count:** The game either continued after a win or assigns the win to the wrong turn, so reject it.
- **Both players winning:** No legal game can reach the second win because play stops at the first.
