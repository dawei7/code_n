## Description

You are given two integers `m` and `n` representing the number of rows and columns of a grid. Your goal is to reach cell `(m - 1, n - 1)`. You are also given a 2D integer array `penalty`.

The cost to enter cell `(i, j)` is `(i + 1) * (j + 1)`.

You begin at cell `(0, 0)` and initially pay its entrance cost. Actions performed after entering `(0, 0)` are numbered starting from 1.

On each action, you may move to an **adjacent** cell or wait in the current cell. A move follows the parity rule if:

<ul>
	<li>On an **odd-numbered** action, you move **right** or **down**.</li>
	<li>On an **even-numbered** action, you move **left** or **up**.</li>
</ul>

The cost of an action is determined as follows:

<ul>
	<li>If you move according to the parity rule, pay only the entrance cost of the destination cell.</li>
	<li>If you move in a direction that **violates** the parity rule, pay the entrance cost of the destination cell plus `penalty[i][j]`, where `(i, j)` is the cell you move from.</li>
	<li>If you **wait** in cell `(i, j)`, pay `penalty[i][j]`.</li>
</ul>

After every move or wait, the action number increases by 1. Therefore, the required parity alternates after every action, regardless of whether a penalty was paid.

Return the **minimum** total cost required to reach `(m - 1, n - 1)`.
