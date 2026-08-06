## Description

On a 2D plane, there are `n` points with integer coordinates `points[i] = [x_i, y_i]`. Return *the **minimum time** in seconds to visit all the points in the order given by *`points`.

You can move according to these rules:

<ul>
	<li>In `1` second, you can either:

	<ul>
		<li>move vertically by one unit,</li>
		<li>move horizontally by one unit, or</li>
		<li>move diagonally `sqrt(2)` units (in other words, move one unit vertically then one unit horizontally in `1` second).</li>
	</ul>
	</li>
	<li>You have to visit the points in the same order as they appear in the array.</li>
	<li>You are allowed to pass through points that appear later in the order, but these do not count as visits.</li>
</ul>
