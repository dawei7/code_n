## General

**Validate consequences of the game rules, not move permutations**

The board has nine cells, so one could try every possible game history. That is unnecessary. Alternating turns and immediate game termination impose a small set of conditions on the final counts and winning lines.

The method checks those conditions directly:

1. `X` must have either the same number of marks as `O` or exactly one more.
2. If `X` has won, `X` must have made the last move, so it must have one more mark.
3. If `O` has won, `O` must have made the last move, so the counts must be equal.

These rules also make simultaneous winners impossible.

**Count the placed marks**

Player `X` always moves first and turns alternate. Therefore every valid prefix of a game has one of exactly two count relationships:

$$
x=o
$$

when zero or more complete pairs of turns have occurred, or:

$$
x=o+1
$$

immediately after an `X` turn.

The nested generator expressions inspect all nine cells and count equalities with `'X'` and `'O'`. Python treats each true equality as one in the sum.

The condition:

`if x != o and x - 1 != o`

rejects every other relationship. It catches an `O` move before the first `X`, two consecutive moves by one player, and any larger imbalance.

**Detect every possible winning line**

Helper `win(mark)` checks the eight Tic-Tac-Toe winning lines.

For each index `i` from zero through two, it checks:

- row `i`: every `board[i][j]` equals the mark;
- column `i`: every `board[j][i]` equals the mark.

After the six row and column checks, it tests the main diagonal `board[i][i]` and the anti-diagonal `board[i][2-i]`.

The helper returns as soon as it finds a line. The number of winning lines is irrelevant; the validation only needs to know whether that player has at least one.

**Connect an `X` win to turn counts**

If `X` wins, the game must end immediately after an `X` placement. Since `X` moves first, that moment has:

$$
x=o+1.
$$

The condition:

`if win('X') and x - 1 != o`

rejects an `X` winning line when counts are equal. Equal counts would mean `O` made a move after `X` had already completed the line, which the rules forbid.

If the count relationship is one extra `X`, the winning line can be regarded as completed by the last `X` move.

**Connect an `O` win to turn counts**

If `O` wins, the last move was by `O`. Every `X` move then has a matching `O` move, so:

$$
x=o.
$$

The final expression rejects exactly:

`win('O') and x != o`.

If `O` has a line while `X` has one more mark, that extra `X` must have been placed after `O` already won, which is illegal.

**Why both winners are rejected**

Suppose both `win('X')` and `win('O')` are true.

If counts are equal, the `X`-win check fails because an `X` win requires one extra `X`. If `X` has one extra mark, the `O`-win check fails because an `O` win requires equal counts.

No count relationship can satisfy both winner conditions, so the code does not need a separate “both win” branch.

**Trace a wrong first move**

For a board containing one `O` and no `X`, counts are `x = 0` and `o = 1`. Neither `x == o` nor `x - 1 == o` holds, so the board is rejected before line checks matter.

This reflects that `X` must always move first.

**Trace an extra same-player move**

If a board has two `X` marks and no `O` marks, `x - o = 2`. The initial count test rejects it because alternating turns never permit a difference greater than one.

**Trace a valid full board**

For `["XOX","O O","XOX"]`, `X` appears four times and `O` appears three times. The count relationship is valid with one extra `X`.

Neither player has three in a row, so both winner-specific restrictions are irrelevant. The position can occur after seven legal moves, and the method returns true.

**Why the conditions are sufficient**

If neither player wins and counts alternate correctly, place the marks in any alternating order that respects their owners. Since the final board has no winning line, no earlier subset can have a winning line that disappears later—marks are only added—so the constructed history never ends prematurely.

If only `X` wins and `x=o+1`, choose an `X` mark whose placement completes a winning line as the final move and alternate all other marks beforehand. Multiple `X` winning lines on a reachable-size board can be completed together by their shared last mark; disjoint winning lines would require too many `X` marks. Before the final mark, no complete `X` line remains, and `O` has no win by assumption.

The symmetric argument applies when only `O` wins and counts are equal. Therefore boards passing the count and winner rules are not merely consistent-looking; a legal move order exists.


Every valid history satisfies the checked count relationship. Its winner, if any, must correspond to the player who just moved, giving the two winner-count conditions.

Conversely, the sufficient-history argument constructs a valid ordering for any board that passes. The method therefore returns true exactly for reachable Tic-Tac-Toe states.

## Complexity detail

The board size is fixed at three by three. Counting marks examines nine cells, and each `win` call checks at most eight lines of three cells. This is a fixed amount of work, so time is $O(1)$.

The method stores two counts, loop indices, and short generator state. It allocates no structure that grows with input, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Enumerate all legal game states:** A DFS from the empty board can precompute reachability, but direct invariants are simpler and constant-time.

- **Check counts only:** Insufficient because a player may have moved after the opponent already won.

- **Check winners only:** Insufficient because turns may have the wrong number of marks even without a win.

- **Both players win:** The two required count relationships conflict, so the board is rejected.

- **No winner:** Only the alternating count relationship is needed.

- **`X` wins:** Require exactly one more `X` than `O`.

- **`O` wins:** Require equal mark counts.

- **Multiple lines for one player:** They can be legal when one final intersection move completes them together.

- **Full board:** It is valid if counts and winner timing are consistent; fullness alone does not decide validity.
