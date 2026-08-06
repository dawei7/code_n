## Description

Let's play the minesweeper game (<a href="https://en.wikipedia.org/wiki/Minesweeper_(video_game)" target="_blank">Wikipedia</a>, <a href="http://minesweeperonline.com" target="_blank">online game</a>)!

You are given an `m x n` char matrix `board` representing the game board where:

<ul>
	<li>`'M'` represents an unrevealed mine,</li>
	<li>`'E'` represents an unrevealed empty square,</li>
	<li>`'B'` represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),</li>
	<li>digit (`'1'` to `'8'`) represents how many mines are adjacent to this revealed square, and</li>
	<li>`'X'` represents a revealed mine.</li>
</ul>

You are also given an integer array `click` where `click = [click_r, click_c]` represents the next click position among all the unrevealed squares (`'M'` or `'E'`).

Return *the board after revealing this position according to the following rules*:

<ol>
	<li>If a mine `'M'` is revealed, then the game is over. You should change it to `'X'`.</li>
	<li>If an empty square `'E'` with no adjacent mines is revealed, then change it to a revealed blank `'B'` and all of its adjacent unrevealed squares should be revealed recursively.</li>
	<li>If an empty square `'E'` with at least one adjacent mine is revealed, then change it to a digit (`'1'` to `'8'`) representing the number of adjacent mines.</li>
	<li>Return the board when no more squares will be revealed.</li>
</ol>
