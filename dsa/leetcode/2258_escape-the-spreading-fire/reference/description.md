## Description

You are given a **0-indexed** 2D integer array `grid` of size `m x n` which represents a field. Each cell has one of three values:

<ul>
	<li>`0` represents grass,</li>
	<li>`1` represents fire,</li>
	<li>`2` represents a wall that you and fire cannot pass through.</li>
</ul>

You are situated in the top-left cell, `(0, 0)`, and you want to travel to the safehouse at the bottom-right cell, `(m - 1, n - 1)`. Every minute, you may move to an **adjacent** grass cell. **After** your move, every fire cell will spread to all **adjacent** cells that are not walls.

Return *the **maximum** number of minutes that you can stay in your initial position before moving while still safely reaching the safehouse*. If this is impossible, return `-1`. If you can **always** reach the safehouse regardless of the minutes stayed, return `10^9`.

Note that even if the fire spreads to the safehouse immediately after you have reached it, it will be counted as safely reaching the safehouse.

A cell is **adjacent** to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
