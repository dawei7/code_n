## Description

There is a `50 x 50` chessboard with **one** knight and some pawns on it. You are given two integers `kx` and `ky` where `(kx, ky)` denotes the position of the knight, and a 2D array `positions` where `positions[i] = [x_i, y_i]` denotes the position of the pawns on the chessboard.

Alice and Bob play a *turn-based* game, where Alice goes first. In each player's turn:

<ul>
	<li>The player *selects *a pawn that still exists on the board and captures it with the knight in the **fewest** possible **moves**. **Note** that the player can select **any** pawn, it **might not** be one that can be captured in the **least** number of moves.</li>
	<li><span>In the process of capturing the *selected* pawn, the knight **may** pass other pawns **without** capturing them</span>. **Only** the *selected* pawn can be captured in *this* turn.</li>
</ul>

Alice is trying to **maximize** the **sum** of the number of moves made by *both* players until there are no more pawns on the board, whereas Bob tries to **minimize** them.

Return the **maximum** *total* number of moves made during the game that Alice can achieve, assuming both players play **optimally**.

Note that in one **move, **a chess knight has eight possible positions it can move to, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.

<img src="https://assets.leetcode.com/uploads/2024/08/01/chess_knight.jpg" style="width: 275px; height: 273px;" />
