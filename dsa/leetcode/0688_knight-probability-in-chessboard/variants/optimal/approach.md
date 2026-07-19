## General
**Store probability mass at each current square**

Begin with probability one at the starting cell and zero elsewhere. For one move, every on-board cell distributes one eighth of its mass to each of its eight knight destinations. Add only contributions whose destination remains inside the board; mass sent outside is deliberately lost.

**Roll the board forward one move at a time**

Create a fresh zeroed board for each step, distribute all current mass, then replace the current layer. A cell can receive probability from several predecessors, so contributions are added rather than overwritten. After `k` layers, sum every remaining cell's mass.

**Why the remaining mass is the requested probability**

Inductively, the value at a cell after `t` layers equals the total probability of all length-`t` move sequences that stay on-board and end there. Extending each sequence by each equally likely move transfers exactly one eighth of its probability to the correct next state. Off-board extensions contribute to no future cell. Therefore the sum after layer `k` is exactly the probability of all and only sequences that never left the board.

## Complexity detail
Each of `K` layers examines $N^{2}$ cells and eight fixed moves per cell, giving $O(KN^2)$ time. Only the current and next probability boards are retained, using $O(N^2)$ space.

## Alternatives and edge cases
- **Top-down memoization:** cache the survival probability for `(row, column, moves_remaining)`; it has the same $O(KN^2)$ state bound and uses $O(KN^2)$ cache space.
- **Matrix exponentiation:** treats transitions as a linear operator and can reduce dependence on very large $K$, but the $N^2\times N^2$ matrix is excessive for these constraints.
- **Enumerate every valid move sequence:** follows the probability definition directly but grows exponentially without memoization.
- With zero moves, the starting probability remains one.
- Choosing an off-board move consumes its one-eighth probability; probabilities must not be renormalized over only legal moves.
- On a one-cell board, any positive number of knight moves gives probability zero.
