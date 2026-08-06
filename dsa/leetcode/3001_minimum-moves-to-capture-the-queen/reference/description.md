## Description

There is a **1-indexed** `8 x 8` chessboard containing `3` pieces.

You are given `6` integers `a`, `b`, `c`, `d`, `e`, and `f` where:

<ul>
	<li>`(a, b)` denotes the position of the white rook.</li>
	<li>`(c, d)` denotes the position of the white bishop.</li>
	<li>`(e, f)` denotes the position of the black queen.</li>
</ul>

Given that you can only move the white pieces, return *the **minimum** number of moves required to capture the black queen*.

**Note** that:

<ul>
	<li>Rooks can move any number of squares either vertically or horizontally, but cannot jump over other pieces.</li>
	<li>Bishops can move any number of squares diagonally, but cannot jump over other pieces.</li>
	<li>A rook or a bishop can capture the queen if it is located in a square that they can move to.</li>
	<li>The queen does not move.</li>
</ul>
