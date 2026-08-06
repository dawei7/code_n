## Description

We are playing the Guess Game. The game is as follows:

I pick a number from `1` to `n`. You have to guess which number I picked (the number I picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API `int guess(int num)`, which returns three possible results:

<ul>
	<li>`-1`: Your guess is higher than the number I picked (i.e. `num > pick`).</li>
	<li>`1`: Your guess is lower than the number I picked (i.e. `num < pick`).</li>
	<li>`0`: your guess is equal to the number I picked (i.e. `num == pick`).</li>
</ul>

Return *the number that I picked*.
