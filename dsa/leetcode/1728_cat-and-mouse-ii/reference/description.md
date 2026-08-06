## Description

A game is played by a cat and a mouse named Cat and Mouse.

The environment is represented by a `grid` of size `rows x cols`, where each element is a wall, floor, player (Cat, Mouse), or food.

<ul>
	<li>Players are represented by the characters `'C'`(Cat)`,'M'`(Mouse).</li>
	<li>Floors are represented by the character `'.'` and can be walked on.</li>
	<li>Walls are represented by the character `'#'` and cannot be walked on.</li>
	<li>Food is represented by the character `'F'` and can be walked on.</li>
	<li>There is only one of each character `'C'`, `'M'`, and `'F'` in `grid`.</li>
</ul>

Mouse and Cat play according to the following rules:

<ul>
	<li>Mouse **moves first**, then they take turns to move.</li>
	<li>During each turn, Cat and Mouse can jump in one of the four directions (left, right, up, down). They cannot jump over the wall nor outside of the `grid`.</li>
	<li>`catJump, mouseJump` are the maximum lengths Cat and Mouse can jump at a time, respectively. Cat and Mouse can jump less than the maximum length.</li>
	<li>Staying in the same position is allowed.</li>
	<li>Mouse can jump over Cat.</li>
</ul>

The game can end in 4 ways:

<ul>
	<li>If Cat occupies the same position as Mouse, Cat wins.</li>
	<li>If Cat reaches the food first, Cat wins.</li>
	<li>If Mouse reaches the food first, Mouse wins.</li>
	<li>If Mouse cannot get to the food within 1000 turns, Cat wins.</li>
</ul>

Given a `rows x cols` matrix `grid` and two integers `catJump` and `mouseJump`, return `true`* if Mouse can win the game if both Cat and Mouse play optimally, otherwise return *`false`.
