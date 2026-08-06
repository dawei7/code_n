## Description

<p data-end="324" data-start="147">You are given an `m x n` grid `classroom` where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:

<ul>
	<li>`'S'`: Starting position of the student</li>
	<li>`'L'`: Litter that must be collected (once collected, the cell becomes empty)</li>
	<li>`'R'`: Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be used multiple times)</li>
	<li>`'X'`: Obstacle the student cannot pass through</li>
	<li>`'.'`: Empty space</li>
</ul>

You are also given an integer `energy`, representing the student's maximum energy capacity. The student starts with this energy from the starting position `'S'`.

Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student can only continue if they are on a reset area `'R'`, which resets the energy to its **maximum** capacity `energy`.

Return the **minimum** number of moves required to collect all litter items, or `-1` if it's impossible.
