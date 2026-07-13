# Knight Probability in Chessboard

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 688 |
| Difficulty | Medium |
| Topics | Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/knight-probability-in-chessboard/) |

## Problem Description
### Goal
A chess knight starts at `(row, column)` on a zero-indexed $n \times n$ board and attempts to make exactly `k` moves. At every move, it chooses uniformly at random among all eight standard knight moves, including choices whose destination lies outside the board.

The knight stops once it moves off the board and cannot return. Return the probability that it remains on the chessboard after completing all `k` moves. For $k = 0$, the starting square is still occupied and the probability is `1`.

### Function Contract
**Inputs**

- `n`: the positive board side length
- `k`: the nonnegative number of moves
- `row`: the starting zero-based row
- `column`: the starting zero-based column

**Return value**

- The probability, between zero and one, that the knight is still on-board after exactly `k` moves

### Examples
**Example 1**

- Input: `n = 3, k = 2, row = 0, column = 0`
- Output: `0.0625`

**Example 2**

- Input: `n = 1, k = 0, row = 0, column = 0`
- Output: `1.0`

**Example 3**

- Input: `n = 1, k = 1, row = 0, column = 0`
- Output: `0.0`

### Required Complexity

- **Time:** $O(KN^2)$
- **Space:** $O(N^2)$

<details>
<summary>Approach</summary>

#### General

**Store probability mass at each current square**

Begin with probability one at the starting cell and zero elsewhere. For one move, every on-board cell distributes one eighth of its mass to each of its eight knight destinations. Add only contributions whose destination remains inside the board; mass sent outside is deliberately lost.

**Roll the board forward one move at a time**

Create a fresh zeroed board for each step, distribute all current mass, then replace the current layer. A cell can receive probability from several predecessors, so contributions are added rather than overwritten. After `k` layers, sum every remaining cell's mass.

**Why the remaining mass is the requested probability**

Inductively, the value at a cell after `t` layers equals the total probability of all length-`t` move sequences that stay on-board and end there. Extending each sequence by each equally likely move transfers exactly one eighth of its probability to the correct next state. Off-board extensions contribute to no future cell. Therefore the sum after layer `k` is exactly the probability of all and only sequences that never left the board.

#### Complexity detail

Each of `K` layers examines $N^{2}$ cells and eight fixed moves per cell, giving $O(KN^2)$ time. Only the current and next probability boards are retained, using $O(N^2)$ space.

#### Alternatives and edge cases

- **Top-down memoization:** cache the survival probability for `(row, column, moves_remaining)`; it has the same $O(KN^2)$ state bound and uses $O(KN^2)$ cache space.
- **Matrix exponentiation:** treats transitions as a linear operator and can reduce dependence on very large $K$, but the $N^2\times N^2$ matrix is excessive for these constraints.
- **Enumerate every valid move sequence:** follows the probability definition directly but grows exponentially without memoization.
- With zero moves, the starting probability remains one.
- Choosing an off-board move consumes its one-eighth probability; probabilities must not be renormalized over only legal moves.
- On a one-cell board, any positive number of knight moves gives probability zero.

</details>
