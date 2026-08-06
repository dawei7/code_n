## Description

A robot on an infinite XY-plane starts at point `(0, 0)` facing north. The robot receives an array of integers `commands`, which represents a sequence of moves that it needs to execute. There are only three possible types of instructions the robot can receive:

<ul>
	<li>`-2`: Turn left `90` degrees.</li>
	<li>`-1`: Turn right `90` degrees.</li>
	<li>`1 <= k <= 9`: Move forward `k` units, one unit at a time.</li>
</ul>

Some of the grid squares are `obstacles`. The `i^th` obstacle is at grid point `obstacles[i] = (x_i, y_i)`. If the robot runs into an obstacle, it will stay in its current location (on the block adjacent to the obstacle) and move onto the next command.

Return the **maximum squared Euclidean distance** that the robot reaches at any point in its path (i.e. if the distance is `5`, return `25`).

**Note:**

<ul>
	<li>There can be an obstacle at `(0, 0)`. If this happens, the robot will ignore the obstacle until it has moved off the origin. However, it will be unable to return to `(0, 0)` due to the obstacle.</li>
	<li>North means +Y direction.</li>
	<li>East means +X direction.</li>
	<li>South means -Y direction.</li>
	<li>West means -X direction.</li>
</ul>
