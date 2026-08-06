## Description

On an infinite plane, a robot initially stands at `(0, 0)` and faces north. Note that:

<ul>
	<li>The **north direction** is the positive direction of the y-axis.</li>
	<li>The **south direction** is the negative direction of the y-axis.</li>
	<li>The **east direction** is the positive direction of the x-axis.</li>
	<li>The **west direction** is the negative direction of the x-axis.</li>
</ul>

The robot can receive one of three instructions:

<ul>
	<li>`"G"`: go straight 1 unit.</li>
	<li>`"L"`: turn 90 degrees to the left (i.e., anti-clockwise direction).</li>
	<li>`"R"`: turn 90 degrees to the right (i.e., clockwise direction).</li>
</ul>

The robot performs the `instructions` given in order, and repeats them forever.

Return `true` if and only if there exists a circle in the plane such that the robot never leaves the circle.
