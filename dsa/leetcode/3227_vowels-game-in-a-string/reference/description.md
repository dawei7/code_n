## Description

Alice and Bob are playing a game on a string.

You are given a string `s`, Alice and Bob will take turns playing the following game where Alice starts **first**:

<ul>
	<li>On Alice's turn, she has to remove any **non-empty** <span data-keyword="substring">substring</span> from `s` that contains an **odd** number of vowels.</li>
	<li>On Bob's turn, he has to remove any **non-empty** <span data-keyword="substring">substring</span> from `s` that contains an **even** number of vowels.</li>
</ul>

The first player who cannot make a move on their turn loses the game. We assume that both Alice and Bob play **optimally**.

Return `true` if Alice wins the game, and `false` otherwise.

The English vowels are: `a`, `e`, `i`, `o`, and `u`.
