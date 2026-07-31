## Description

Use these rules for a tic-tac-toe game played by two players on an $n \times n$ board:

- Every move is guaranteed to be valid and targets an empty cell.
- After a winning condition is reached, no additional moves are made.
- A player wins by placing $n$ of their marks in one horizontal row, one vertical column, or either full diagonal.

Implement the `TicTacToe` class:

- `TicTacToe(int n)` initializes a board of size $n \times n$.
- `int move(int row, int col, int player)` places `player`'s mark at `(row,col)`. Moves are valid and the two players alternate. Return `0` if nobody has won, `1` if player `1` wins on this move, or `2` if player `2` wins on this move.
