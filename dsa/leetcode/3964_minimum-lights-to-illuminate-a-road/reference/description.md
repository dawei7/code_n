## Description

You are given an integer array `lights` of length `n`, representing positions 0 through `n - 1` on a road.

For each position `i`:

<ul>
	<li>If `lights[i] = v`, where `v > 0`, there is a working bulb at position `i` that **illuminates** every position from `max(0, i - v)` to `min(n - 1, i + v)`, inclusive.</li>
	<li>If `lights[i] = 0`, there is no working bulb at position `i`.</li>
</ul>

A position is **visible** if it is illuminated by **at least** one working bulb.

You may install **additional** bulbs at **any** positions. Each additional bulb installed at position `j` **illuminates** positions from `max(0, j - 1)` to `min(n - 1, j + 1)`, inclusive.

Return the minimum number of additional bulbs required to make **every** position on the road visible.
