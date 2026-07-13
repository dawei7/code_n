# Valid Tic-Tac-Toe State

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 794 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-tic-tac-toe-state/) |

## Problem Description

### Goal

Given a $3 x 3$ Tic-Tac-Toe board containing `X`, `O`, and empty spaces, determine whether the displayed state can occur during a legal game. Player `X` moves first, and the players then alternate placing one mark in an empty cell.

The game ends immediately when either player completes a full row, column, or diagonal, so no later marks may be played after that win. Return `True` if some legal move sequence reaches exactly the supplied board and `False` otherwise.

### Function Contract

**Inputs**

- `board`: three strings of length three representing the current board.

**Return value**

- `True` if some legal move sequence reaches exactly this state; otherwise `False`.

### Examples

**Example 1**

- Input: `board = ["O  ","   ","   "]`
- Output: `False`
- Explanation: `O` cannot move before `X`.

**Example 2**

- Input: `board = ["XOX"," X ","   "]`
- Output: `False`
- Explanation: Three `X` marks and one `O` mark cannot result from alternating turns.

**Example 3**

- Input: `board = ["XOX","O O","XOX"]`
- Output: `True`
- Explanation: The marks alternate correctly and neither player has already won.

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Check the turn counts**

Because `X` starts and turns alternate, the number of `X` marks must equal the number of `O` marks or exceed it by exactly one. Every other count difference is impossible.

**Check wins against the last mover**

Inspect the three rows, three columns, and two diagonals for each player. If `X` has won, `X` must have made the most recent move, so its count must be one larger. If `O` has won, the counts must be equal. These rules also reject simultaneous winners because they demand incompatible turn counts.

The count condition constructs the only possible next-player parity. With no winner, any ordering of the existing marks that alternates players and places the shown squares is legal because play has not been forced to stop. With a winner, the corresponding count condition places that winning mark on the final turn; its marks can be ordered so the completing square is last. Therefore the count and winner conditions are sufficient as well as necessary.

#### Complexity detail

The board always contains exactly nine cells and eight winning lines. Counting marks and checking those lines takes constant $O(1)$ time and $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Line-sum encoding:** Map `X` and `O` to signed values and inspect row, column, and diagonal sums; this expresses the same constant-time checks.
- **Generate every reachable state:** Simulate all alternating move histories and store their boards; this is feasible only because the board is fixed, but does far more work.
- **Backtrack through occupied squares:** Testing all move orders grows factorially with the number of marks.
- **Empty board:** It is the valid initial state.
- **Only one `X`:** This is a valid state after the opening move.
- **Winner with wrong count:** The game either continued after a win or assigns the win to the wrong turn, so reject it.
- **Both players winning:** No legal game can reach the second win because play stops at the first.

</details>
