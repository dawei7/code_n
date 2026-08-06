## Description

A storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.

The game is represented by an `m x n` grid of characters `grid` where each element is a wall, floor, or box.

Your task is to move the box `'B'` to the target position `'T'` under the following rules:

<ul>
	<li>The character `'S'` represents the player. The player can move up, down, left, right in `grid` if it is a floor (empty cell).</li>
	<li>The character `'.'` represents the floor which means a free cell to walk.</li>
	<li>The character<font face="monospace"> </font>`'#'`<font face="monospace"> </font>represents the wall which means an obstacle (impossible to walk there).</li>
	<li>There is only one box `'B'` and one target cell `'T'` in the `grid`.</li>
	<li>The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a **push**.</li>
	<li>The player cannot walk through the box.</li>
</ul>

Return *the minimum number of **pushes** to move the box to the target*. If there is no way to reach the target, return `-1`.
