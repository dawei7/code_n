## Description

You are given an integer `n` representing the number of players in a game and a 2D array `pick` where `pick[i] = [x_i, y_i]` represents that the player `x_i` picked a ball of color `y_i`.

Player `i` **wins** the game if they pick **strictly more** than `i` balls of the **same** color. In other words,

<ul>
	<li>Player 0 wins if they pick any ball.</li>
	<li>Player 1 wins if they pick at least two balls of the *same* color.</li>
	<li>...</li>
	<li>Player `i` wins if they pick at least `i + 1` balls of the *same* color.</li>
</ul>

Return the number of players who **win** the game.

**Note** that *multiple* players can win the game.
