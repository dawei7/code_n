## Description

According to <a href="https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life" target="_blank">Wikipedia's article</a>: "The **Game of Life**, also known simply as **Life**, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an `m x n` grid of cells, where each cell has an initial state: **live** (represented by a `1`) or **dead** (represented by a `0`). Each cell interacts with its <a href="https://en.wikipedia.org/wiki/Moore_neighborhood" target="_blank">eight neighbors</a> (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

<ol>
	<li>Any live cell with fewer than two live neighbors dies as if caused by under-population.</li>
	<li>Any live cell with two or three live neighbors lives on to the next generation.</li>
	<li>Any live cell with more than three live neighbors dies, as if by over-population.</li>
	<li>Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.</li>
</ol>

<span>The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the `m x n` grid `board`. In this process, births and deaths occur **simultaneously**.</span>

<span>Given the current state of the `board`, **update** the `board` to reflect its next state.</span>

**Note** that you do not need to return anything.
