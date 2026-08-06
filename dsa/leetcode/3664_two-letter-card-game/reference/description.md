## Description

You are given a deck of cards represented by a string array `cards`, and each card displays two lowercase letters.

You are also given a letter `x`. You play a game with the following rules:

<ul>
	<li>Start with 0 points.</li>
	<li>On each turn, you must find two **compatible** cards from the deck that both contain the letter `x` in any position.</li>
	<li>Remove the pair of cards and earn **1 point**.</li>
	<li>The game ends when you can no longer find a pair of compatible cards.</li>
</ul>

Return the **maximum** number of points you can gain with optimal play.

Two cards are **compatible** if the strings differ in **exactly** 1 position.
