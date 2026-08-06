## Description

**Tic-tac-toe** is played by two players `A` and `B` on a `3 x 3` grid. The rules of Tic-Tac-Toe are:

<ul>
	<li>Players take turns placing characters into empty squares `' '`.</li>
	<li>The first player `A` always places `'X'` characters, while the second player `B` always places `'O'` characters.</li>
	<li>`'X'` and `'O'` characters are always placed into empty squares, never on filled ones.</li>
	<li>The game ends when there are **three** of the same (non-empty) character filling any row, column, or diagonal.</li>
	<li>The game also ends if all squares are non-empty.</li>
	<li>No more moves can be played if the game is over.</li>
</ul>

Given a 2D integer array `moves` where `moves[i] = [row_i, col_i]` indicates that the `i^th` move will be played on `grid[row_i][col_i]`. return *the winner of the game if it exists* (`A` or `B`). In case the game ends in a draw return `"Draw"`. If there are still movements to play return `"Pending"`.

You can assume that `moves` is valid (i.e., it follows the rules of **Tic-Tac-Toe**), the grid is initially empty, and `A` will play first.
