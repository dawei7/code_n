## Description

You are given two **0-indexed** integer arrays `<font face="monospace">player1</font>` and `player2`, representing the number of pins that player 1 and player 2 hit in a bowling game, respectively.

The bowling game consists of `n` turns, and the number of pins in each turn is exactly 10.

Assume a player hits `x_i` pins in the i^th turn. The value of the i^th turn for the player is:

<ul>
	<li>`2x_i` if the player hits 10 pins **in either (i - 1)^th or (i - 2)^th turn**.</li>
	<li>Otherwise, it is `x_i`.</li>
</ul>

The **score** of the player is the sum of the values of their `n` turns.

Return

<ul>
	<li>1 if the score of player 1 is more than the score of player 2,</li>
	<li>2 if the score of player 2 is more than the score of player 1, and</li>
	<li>0 in case of a draw.</li>
</ul>
