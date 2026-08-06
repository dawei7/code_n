## Description

<div data-docx-has-block-data="false" data-lark-html-role="root" data-page-id="Rax8d6clvoFeVtx7bzXcvkVynwf">
<div class="old-record-id-Y5dGdSKIMoNTttxGhHLccrpEnaf">There is an endless straight line populated with some robots and walls. You are given integer arrays `robots`, `distance`, and `walls`:</div>
</div>

<ul>
	<li>`robots[i]` is the position of the `i^th` robot.</li>
	<li>`distance[i]` is the **maximum** distance the `i^th` robot's bullet can travel.</li>
	<li>`walls[j]` is the position of the `j^th` wall.</li>
</ul>

Every robot has **one** bullet that can either fire to the left or the right **at most **`distance[i]` meters.

A bullet destroys every wall in its path that lies within its range. Robots are fixed obstacles: if a bullet hits another robot before reaching a wall, it **immediately stops** at that robot and cannot continue.

Return the **maximum** number of **unique** walls that can be destroyed by the robots.

Notes:

<ul>
	<li>A wall and a robot may share the same position; the wall can be destroyed by the robot at that position.</li>
	<li>Robots are not destroyed by bullets.</li>
</ul>
